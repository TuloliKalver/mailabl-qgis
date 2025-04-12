import gc
from PyQt5.QtCore import QCoreApplication
from qgis.core import QgsFeatureRequest
from ...queries.python.property_data import deleteProperty
from ...KeelelisedMuutujad.messages import Headings
from ...KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ...utils.LayerFeaturehepers import LayerFeaturehepers
from ...queries.python.property_data import MyLablChecker
from ...Common.app_state import PropertiesProcessStage
from ...utils.ProgressHelper import ProgressDialogModern


pealkiri = Headings()

class ReomoveProcessController:
    @staticmethod
    def reomve_process_controller(delete_anyway = False):
        active_layer = next((info['layer'] for info in PropertiesProcessStage.loaded_layers.values() if info.get('activated')), None)
        if not active_layer or not active_layer.selectedFeatureCount():
            print("❌ No features selected.")
            return False

        field_name = Katastriyksus.tunnus
        selected_ids = active_layer.selectedFeatureIds()

        heading = "Kinnistute eemaldamine..."
        progress = ProgressDialogModern(maximum=len(selected_ids), title=heading)

        for count, fid in enumerate(selected_ids, start=1):
            progress.update(value=count)

            # Use feature request to only pull the single feature
            feature = next(active_layer.getFeatures(QgsFeatureRequest(fid)), None)
            if not feature:
                print(f"⚠️ Feature ID {fid} not found.")
                continue

            tunnus = feature[field_name]
            res, data = MyLablChecker._get_propertie_ids_by_cadastral_numbers_EQUALS(item=tunnus)

            delete_successful = False
            if res is False and data:
                print(f"🟠 item {tunnus} found in Mylabl")
                node_ids = [entry['node']['id'] for entry in data]

                delete_successful = True
                for item in node_ids:
                    result = deleteProperty.delete_single_item(item)
                    if not result:
                        print(f"❌ SaaS deletion failed for {item}")
                        delete_successful = False
                        break

            if delete_successful or delete_anyway:
                delete_res = LayerFeaturehepers._delete_feature_object(feature=feature, layer=active_layer)
                if not delete_res:
                    print(f"⚠️ Failed to delete feature {fid} from local layer")

            gc.collect()

        gc.collect()
        progress.close()
        QCoreApplication.processEvents()
        return True