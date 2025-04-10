import gc
from PyQt5.QtCore import QCoreApplication
from ...queries.python.property_data import deleteProperty
from ...KeelelisedMuutujad.messages import Headings
from ...KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ...utils.LayerFeaturehepers import LayerFeaturehepers
from ...queries.python.property_data import MyLablChecker
from ...utils.LayerHelpers import LayerProcessHandlers

pealkiri = Headings()

class ReomoveProcessController:
    @staticmethod
    def reomve_process_controller(delete_anyway = False):
        from ...Common.app_state import PropertiesProcessStage
        active_layer = next((info['layer'] for info in PropertiesProcessStage.loaded_layers.values() if info.get('activated')), None)
        tunnus = Katastriyksus.tunnus

        features = LayerProcessHandlers._get_selected_objects_from_layer(active_layer)
        #print(f"features: {features}")
        if not features:
            print("No features selected.")
            return False
        from ...utils.ProgressHelper import ProgressDialogModern
        heading = "Eemaldamine"
        max_items = len(features)
        progress = ProgressDialogModern(maximum=max_items, title=heading)
        count = 1
        for feature in features:
            progress.update(value=count)
            layer_data = LayerFeaturehepers._get_feature_attributes_as_dict(feature=feature)
            #print (f"layer_data: {layer_data}")
            tunnus = layer_data.get(Katastriyksus.tunnus)
            #print (f"Tunnus: {tunnus}")            
            res, data = MyLablChecker._get_propertie_ids_by_cadastral_numbers_EQUALS(item=tunnus)
            #print(f"res: {res}" )
            #print(f"data: {data}")
            # If a duplicate is found
            delete_successful = False
            if res is False:
                print("Duplicate found!")
                node_ids = [entry['node']['id'] for entry in data]

                # ✅ Try deleting from SaaS first
                delete_successful = True
                for item in node_ids:
                    result = deleteProperty.delete_single_item(item)
                    if not result:
                        #print(f"❌ Failed to delete item {item} from SaaS")
                        delete_successful = False
                        break  # Optional: stop processing if any SaaS deletion fails

            # ✅ Only delete from QGIS layer if SaaS deletion worked
            if delete_successful or delete_anyway:
                delete_res = LayerFeaturehepers._delete_feature_object(feature=feature, layer=active_layer)
                if not delete_res:
                    print(f"⚠️ Failed to delete feature from local layer")

            count += 1
            gc.collect()

        gc.collect()
        progress.close()
        QCoreApplication.processEvents()       
        return True