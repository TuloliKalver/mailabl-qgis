from .checkable_comboboxes import ComboBoxFunctions, ComboBoxMapTools
from .ui_controllers import WidgetAnimator, FrameHandler
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus


comboboxes =ComboBoxFunctions
tools_shp = ComboBoxMapTools


# muutujate määramine koodi ühtlustamieseks
    # maa-ameti andmed

mk_nimi_field = Katastriyksus.mk_nimi #'MK_NIMI'
ov_nimi_field = Katastriyksus.ov_nimi #'OV_NIMI'
ay_nimi_field = Katastriyksus.ay_nimi #"AY_NIMI"




class RemoveProcess:
    #def __init__(self):
        #self.combobox_name = comboboxes_name  # Store comboboxes as a dictionary


    def Remove_process_stage_1(self,insetrToComboBox,layer, parentWidget):
        #print(layer)
        field = mk_nimi_field
        data = tools_shp.create_item_list(layer,field)
        combobox = comboboxes.get_combobox_by_name(self,insetrToComboBox,parentWidget)
        comboboxes.insert_values_to_combobox(self, combobox, data)
        comboboxes.increase_popup_size(self, combobox, 5)

    def Remove_process_stage_next(self,inputComboBox,insetrToComboBox,Mailabllayer, parentWidget):
        #print(layer)
        field = mk_nimi_field
        where_field = ov_nimi_field
        input = comboboxes.get_combobox_by_name(self,inputComboBox,parentWidget)
        insert = comboboxes.get_combobox_by_name(self,insetrToComboBox,parentWidget)
        restriction = input.itemText() 
        print(restriction)
        data = tools_shp.create_item_list_with_where(self, input, where_field, field)
        comboboxes.insert_values_to_combobox(self, insert, data)
        comboboxes.increase_popup_size(self, insert, 5)


        expression = "{} IN ('{}')".format(ov_nimi_field, restriction)
        print(f"Expression: {expression}")
        #layer = QgsProject.instance().mapLayersByName(Mailabllayer)[0]
        #layer.setSubsetString(expression)
        #layer.triggerRepaint()
        #layer.updateExtents()
        #graph_tools.zoom_to_layer_extent(layer)
        #item_count = graph_tools.count_items_in_layer(input_layer_name)
        #self.lblCount.setText(f"{item_count}")





    def Remove_process_stage_2(self,inputComboBox, insetrToComboBox, layer, parentWidget):
        where_field = mk_nimi_field
        print(f"input - Where field value: {where_field}")
        field = ov_nimi_field
        print (f"input - field value: {field}")
        insetrToComboBox = comboboxes.get_combobox_by_name(self,insetrToComboBox,parentWidget) 

        print(f"input - combobox value {inputComboBox} ")
        data = tools_shp.create_item_list_with_where(self, inputComboBox, layer, where_field, field)
        print(data)
        add_space = 5       
        comboboxes.insert_values_to_combobox(self, insetrToComboBox, data)
        comboboxes.increase_popup_size(self, insetrToComboBox, add_space)
        
