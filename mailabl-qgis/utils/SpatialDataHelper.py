
import gc
from qgis.core import QgsProject, QgsSpatialIndex, QgsRectangle, QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY
from qgis.utils import iface
from ..queries.python.FileLoaderHelper import GraphQLQueryLoader, GraphqlProjects
from ..queries.python.responses import HandlePropertiesResponses
from ..queries.python.query_tools import requestBuilder
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ..KeelelisedMuutujad.modules import Module
from ..config.settings import SettingsDataSaveAndLoad
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ..queries.python.projects_pandas import ProjectModelBuilders
from ..utils.TableUtilys.MainModuleTaibleBiulder import ModuleTableBuilder
from ..utils.messagesHelper import ModernMessageDialog



class ZoomForModuleData:
    def __init__(self):
        self.zoom_functions = {
            Module.CONTRACT: self.WRAPPER_find_module_items_by_map_zoom,
            Module.PROJECT: self.WRAPPER_find_module_items_by_map_zoom,   
            Module.EASEMENT: self.WRAPPER_find_module_items_by_map_zoom,
        }
    def WRAPPER_find_module_items_by_map_zoom(self, instance: object, module=None, language="et") -> None:
        tables = {
            Module.PROJECT: instance.tblMailabl_projects,
            # Add more module-table mappings as needed
        }

        table = tables.get(module)
        if not table:
            print(f"❗ Module {module} not mapped to any table")
            heading = Headings().error_simple
            message = f"❗ Tabelit moodulile {module} ei leitud."
            ModernMessageDialog.Info_messages_modern(heading,message)
            return

        layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        element_feature_name = Katastriyksus.tunnus

        selected_features = MapExtentFeatureReader._get_visible_features_with_zoom(
            layer_name, element_feature_name
        )

        if not selected_features:
            ModernMessageDialog.Info_messages_modern(Headings().warningSimple, HoiatusTexts().zoom_siin_ei_ole_midagi)
            return

        model = ProjectModelBuilders()._model_for_module_zoomed_map_properties(
            selected_features, language, module
        )

        if model is None:

            ModernMessageDialog.Info_messages_modern( Headings().warningSimple, "Mudeli loomine ebaõnnestus.")
            return

        ModuleTableBuilder.setup(table, model, module, language)


class MapExtentFeatureReader():
    scale_limit = 1500
    @staticmethod
    #@log_test_entry("get_visible_features")
    def _get_visible_features_with_zoom(layer_name: str, get_feature: str) -> list[str] :
        canvas = iface.mapCanvas()
        scale = canvas.scale()
        if scale > MapExtentFeatureReader.scale_limit:
            canvas.zoomScale(MapExtentFeatureReader.scale_limit)
        features= MapExtentFeatureReader._fetch_features_by_layer_name_and_field(layer_name, get_feature)
        return features

    @staticmethod
    def _fetch_features_by_layer_name_and_field(layer_name: str, get_feature: str)->list[str] :
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        extent = iface.mapCanvas().extent()
        index = QgsSpatialIndex(layer.getFeatures())
        intersecting_ids = index.intersects(extent)
        visible_features = []
        for feature in layer.getFeatures():
            if feature.id() in intersecting_ids:
                visible_features.append(feature[get_feature])
        gc.collect()  # Force garbage collection
        return visible_features

    @staticmethod
    def _fetch_with_filter(layer_name: str,field_name: str,filter_field: str = None,filter_value: str = None,extent_only: bool = True, return_feature_ids: bool = False) -> list:
        """
        Fetches features from a layer based on current extent and optional attribute filter.

        :param layer_name: Name of the layer to query
        :param field_name: The field to return values from
        :param filter_field: Optional field name to filter by
        :param filter_value: Optional value to match for filtering
        :param extent_only: If True, restrict to current map extent
        :param return_feature_ids: If True, return feature IDs instead of field values
        :return: List of feature values or IDs

        Example usage:
            # Get visible counties where STATE_NAME == 'Tartumaa'
            MapExtentFeatureReader.fetch_with_filter(
                layer_name="EestiOmavalitsused",
                field_name="NIMI",
                filter_field="STATE_NAME",
                filter_value="Tartumaa"
            )

            # Get all features, not filtered, return IDs
            MapExtentFeatureReader.fetch_with_filter(
                layer_name="ParcelLayer",
                field_name="ID",
                extent_only=False,
                return_feature_ids=True
            )

        """
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        canvas_extent = iface.mapCanvas().extent() if extent_only else None

        index = QgsSpatialIndex(layer.getFeatures())
        intersecting_ids = index.intersects(canvas_extent) if extent_only else []

        results = []

        for feature in layer.getFeatures():
            if extent_only and feature.id() not in intersecting_ids:
                continue

            if filter_field and filter_value is not None:
                if feature[filter_field] != filter_value:
                    continue

            if return_feature_ids:
                results.append(feature.id())
            else:
                results.append(feature[field_name])

        return results

    @staticmethod
    def _get_visible_feature_ids(layer_name: str) -> list[int]:
        """
        Returns IDs of features currently visible in the map canvas extent.
        """
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        extent = iface.mapCanvas().extent()

        index = QgsSpatialIndex(layer.getFeatures())
        return index.intersects(extent)

    @staticmethod
    def _get_features_in_bbox(layer_name: str, bbox: QgsRectangle) -> list[QgsFeature]:
        """
        Returns all features within a given bounding box (QgsRectangle).
        """
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        index = QgsSpatialIndex(layer.getFeatures())
        ids = index.intersects(bbox)

        features = []
        for f in layer.getFeatures():
            if f.id() in ids:
                features.append(f)
        return features

    @staticmethod
    def _get_features_by_geometry(layer: QgsVectorLayer, geometry: QgsGeometry) -> list[QgsFeature]:
        """
        Returns features that intersect a given geometry.
        """
        index = QgsSpatialIndex(layer.getFeatures())
        ids = index.intersects(geometry.boundingBox())

        features = []
        for f in layer.getFeatures():
            if f.id() in ids and f.geometry().intersects(geometry):
                features.append(f)
        return features

    @staticmethod
    def _get_nearest_feature(layer: QgsVectorLayer, point: QgsPointXY) -> QgsFeature:
        """
        Returns the nearest feature to a given QgsPointXY.
        """
        index = QgsSpatialIndex(layer.getFeatures())
        nearest_ids = index.nearestNeighbor(point, 1)

        if not nearest_ids:
            return None

        for f in layer.getFeatures():
            if f.id() == nearest_ids[0]:
                return f

        return None

    @staticmethod
    def _get_features_by_attribute(layer: QgsVectorLayer, field_name: str, value) -> list[QgsFeature]:
        """
        Returns all features where field == value.
        """
        return [f for f in layer.getFeatures() if f[field_name] == value]

    @staticmethod
    def get_module_feature_conneted_with_propertie_list_CHEK_FOR_MODULE_USAGE(cadastral_numbers, module=None):
        #print(f"cadastral_numbers: {cadastral_numbers}")
        
        my_module = Module.PROJECT
        query_name = GraphqlProjects.Q_Properties_related_projects
        query = GraphQLQueryLoader.load_query_by_module(my_module, query_name)
        #print(f"query: {query}")
        items_for_page = 50
        end_cursor = None
        data = []
        variables =        {
                    "first": items_for_page,
                    "after": "",
                    "where": {
                        "AND": [
                            {
                                "column": "CADASTRAL_UNIT_NUMBER",
                                "operator": "IN",
                                "value": cadastral_numbers
                            }
                        ]
                    }
                }
        while True:
            response = requestBuilder.construct_and_send_request( query, variables)
            
            module = (f"{module}s")
            if response.status_code == 200:
                #print(f"YES WE ARE DEVELOPING IN THE RIGHT DIRECTION!")
                edge = HandlePropertiesResponses._response_properties_data_edges(response)
                for item in edge:
                    for i in item['node'][module]['edges']:
                        if i['node']['id']:
                            data.append(i['node'])
                    page_info = item['node'][module]['pageInfo']
                    if page_info['hasNextPage']:
                        end_cursor = page_info['endCursor']
                        variables['after'] = end_cursor
                        break
                else:
                    break  # Exit loop if there are no more pages
        return data