from PyQt5.QtCore import QEasingCurve, QPropertyAnimation
from PyQt5.QtWidgets import QPushButton, QFrame
from qgis.core import (QgsProject, QgsVectorLayer)
from ..processes.infomessages.messages import SHP_layer_not_present
from ..config.settings import flags
from PyQt5.QtCore import QTimer

background_green = "background-color: #607D3B"
background_red = "background-color: #D32F2F"
background_gray = "background-color: #404957"
background_for_not_available = "background-color: #838ea2"
background_standard_button = "background-color:#40414f"

button_padding = 6

class WidgetAnimator:

    def __init__(self, parent_widget,  animation_duration=500, default_height=40, button_padding=6):
        self.parent_widget = parent_widget
        
        self.animation_duration = animation_duration
        self.default_height = default_height
        self.button_padding = button_padding
        self.button_labels = {}

    def toggle_Frame_height_level_2_frames(self, widget, push_button):
        #print(f"push button {push_button}")
        main_widget = WidgetAnimator.buttons_sliderFrame_name(self, push_button)
        #print(f"name of main_widget {main_widget.objectName()}")
        main_widget_name = main_widget.objectName()
        main_widgets_height = main_widget.height()
        aditional_height = WidgetAnimator.buttons_sliderFrame_height(self,push_button, button_padding)
        ##print(f"Aditional height {aditional_height}")
        #print(f"Main widget {main_widget_name} heightcurrent: {main_widgets_height}")
        collapsed_height = 0
        if collapsed_height < main_widgets_height:
            #print("Started to collapse_phase2")
            new_height = collapsed_height
            #defines the TOP_LEVEL Max height!
            widget.setMaximumHeight(0)
            easing_curve = QEasingCurve.InBounce
        
        else:
            #print("Started to expand")
            new_height = aditional_height
            #print(f"Expanding height {aditional_height}")
            widget.setMaximumHeight(16777215)
            easing_curve = QEasingCurve.OutBounce
        
        self.animation = QPropertyAnimation(main_widget, b"minimumHeight")
        self.animation.setDuration(250)
        self.animation.setStartValue(main_widgets_height)
        self.animation.setEndValue(new_height)
        self.animation.setEasingCurve(easing_curve)
        self.animation.start()
    
    def toggle_Frame_height(self, widget, push_button):
#        print("Toggle started")
#        print(f"Widget {widget}")
        height = widget.height()
#       print(f"Initial height: {height}")
        
        if height == 0:

            new_height = self.calculate_total_widget_max_height_needed(widget, push_button)
            print(f"new height {new_height}")
            #widget.setMaximumHeight(16777215)
            easing_curve = QEasingCurve.OutBounce

        else:
#            print("Started to collapse")
            new_height = 0
            widget.setMaximumHeight(0)
            easing_curve = QEasingCurve.InBounce
            
        self.animation = QPropertyAnimation(widget, b"minimumHeight")
        self.animation.setDuration(250)
        self.animation.setStartValue(height)
        self.animation.setEndValue(new_height)
        self.animation.setEasingCurve(easing_curve)  # Set the easing curve here
        self.animation.start()

#Run this to change frame width
    def toggle_Frame_width(self, widget):
        print("Toggle started")
        print(f"Widget {widget}")
        width = widget.width()
        print(f"Initial width: {width}")
        
        if width == 40:
            #print("Started to expand")
            new_width = 200
            easing_curve = QEasingCurve.OutBounce
        else:
            #print("Started to collapse")
            new_width = 40
            easing_curve = QEasingCurve.InBounce

        self.animation = QPropertyAnimation(widget, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(easing_curve)  # Set the easing curve here
        self.animation.start()
        
    def buttons_sliderFrame_name(self, push_button):
        print(f"button name {push_button.objectName()}")       
        #Step 1: Find the frame in which the button is inside
        button_frame = push_button.parentWidget()
        print(f"Button Frame: {button_frame.objectName()}")
        if button_frame is None:
            #print("Button Frame not found")
            return None
        # Step 2: Find the frame of the button frame
        button_frame_parent = button_frame.parentWidget()
        #print(f"Button Frame Parent: {button_frame_parent.objectName()}")
        if button_frame_parent is None:
            #print("Button Frame Parent not found")
            return None
        # Step 3: Find all the frame names within the same hierarchy level as the button
        all_frame_names = [frame.objectName() for frame in button_frame_parent.findChildren(QFrame) if frame.parentWidget() == button_frame_parent]
        #print(f"All Frame Names within the same level: {all_frame_names}")
        # Step 4: Exclude the button frame to find the Slider Frame
        remaining_frames = [frame_name for frame_name in all_frame_names if frame_name != button_frame.objectName()]
        if len(remaining_frames) != 1:
            #print("Slider Frame not found")
            return None

        slider_frame_name = remaining_frames[0]
        slider_frame = button_frame_parent.findChild(QFrame, slider_frame_name)
        print(f"Slider frame name {slider_frame}")
        return slider_frame

    def buttons_sliderFrame_height(self, push_button, padding):
        button_frame = push_button.parentWidget()
        print(f"Button Frame: {button_frame.objectName()}")
        if button_frame is None:
            #print("Button Frame not found")
            return None

        # Step 2: Find the frame of the button frame
        button_frame_parent = button_frame.parentWidget()
        print(f"Button Frame Parent: {button_frame_parent.objectName()}")
        
        if button_frame_parent is None:
            #print("Button Frame Parent not found")
            return None

        # Step 3: Find all the frame names within the same hierarchy level as the button
        all_frame_names = [frame.objectName() for frame in button_frame_parent.findChildren(QFrame) if frame.parentWidget() == button_frame_parent]
        #print(f"All Frame Names within the same level: {all_frame_names}")

        # Step 4: Exclude the button frame to find the Slider Frame
        remaining_frames = [frame_name for frame_name in all_frame_names if frame_name != button_frame.objectName()]
        #print(f"remaining frame {remaining_frames}")
        if len(remaining_frames) != 1:
            #print("Slider Frame not found - too few values!")
            return None

        slider_frame_name = remaining_frames[0]
        slider_frame = button_frame_parent.findChild(QFrame, slider_frame_name)
        #print(f"Slider frame name {slider_frame.objectName()}")
        if slider_frame is None:
            #print(f"Slider Frame '{slider_frame_name}' not found")
            return None

    # Count second-level Main frames
        second_level_main_frames = len([frame for frame in button_frame_parent.findChildren(QFrame) if frame.objectName().endswith("_MainFrame")])
        #print(f"Number of Second-Level Main Frames: {second_level_main_frames}")

        # Step 5: Calculate the buttons inside slider_frame within the same hierarchy level
        
        child_buttons = [button for button in slider_frame.findChildren(QPushButton) if button.parentWidget() == slider_frame]
        
        #print(child_buttons)
        buttons_total_height = sum(button.height() for button in child_buttons)
        #print(f"Button Total_height: {buttons_total_height}")
        single_button_height = buttons_total_height / len(child_buttons) if len(child_buttons) > 0 else 0
        #print(f"Single button height {single_button_height}")
        #total_height += (second_level_main_frames)* single_button_height
        #print(f"Total height2 {second_level_main_frames}*{single_button_height}={total_height}")
        buttons_total_height += len(child_buttons) * padding
        return buttons_total_height

#This is curretly temporary and sets height based on hardcore value for height!
    def toggle_Frame_height_for_settings(self, widget):
        height = widget.height()
        #print(f"Wideget in 'toggle_Frame_height_for_settings': {widget}")
        if height == 0:
            #print(f"widgets heigt was in 'toggle_Frame_height_for_settings': {height}")
            new_height = 60
            easing_curve = QEasingCurve.OutBounce
        else:
            #print(f"widgets heigt was in 'toggle_Frame_height_for_settings': {height}")
            new_height = 0
            widget.setMaximumHeight(0)
            easing_curve = QEasingCurve.InBounce
        
        duration_in_milliseconds = 250    
        self.animation = QPropertyAnimation(widget, b"minimumHeight")
        self.animation.setDuration(duration_in_milliseconds)
        self.animation.setStartValue(height)
        self.animation.setEndValue(new_height)
        self.animation.setEasingCurve(easing_curve)
        self.animation.start()
        QTimer.singleShot(duration_in_milliseconds+250, lambda: WidgetAnimator.animationFinished(animation=self.animation))
        duration_in_seconds = duration_in_milliseconds / 1000.0
        return duration_in_seconds

    @staticmethod
    def animationFinished(animation):
        # Access class variables or methods using cls
        if animation.state() != QPropertyAnimation.Stopped:
            # Stop the animation if it's not already stopped
            animation.stop()

    def calculate_total_widget_max_height_needed(self, widget,push_button):
        print(f"widget {widget}")
        print(f"Push button name {push_button}")
        total_height = 0
        parent_widget = push_button.parentWidget().objectName()
        print(f"Parent widget: {parent_widget}")
        child_buttons = widget.findChildren(QPushButton)
        top_level_frames = widget.findChildren(QFrame)

        print("=== All child buttons ===")
        print(f"children count: {len(child_buttons)}")

        # Create a set to store the object names of top-level frames
        top_level_frame_names = set(frame.objectName() for frame in top_level_frames)
        print(f"Top level names: {top_level_frame_names}")
        for button in child_buttons:
            # Check if the button's parent frame is a top-level frame
            if button.parentWidget().objectName() in top_level_frame_names:
                print("Button in first level frame:", button.objectName())
                total_height += button.height()
                total_height += self.button_padding

        print("Total buttons height in first level frames:", total_height)
        return total_height

class secondLevelButtonsHandler:
    @staticmethod
    def toggle_Frame_height_DataLoading(self):
        push_button = self.pbUpdateData
        widget = self.pbUpdateData_SliderFrame
        main_widget = self.pbSettings_SliderFrame
        widgets_height = widget.height()
        aditional_height = WidgetAnimator.buttons_sliderFrame_height(self,push_button, button_padding)
        if flags.Flag_SliderButton_LoadData:
            new_height = 0
            widget.setMaximumHeight(0)
            easing_curve = QEasingCurve.InBounce

        else:
            #print("Started to expand")
            new_height = aditional_height
            #print(f"Expanding height {aditional_height}")
            widget.setMaximumHeight(16777215)
            main_widget.setMaximumHeight(16777215)
            easing_curve = QEasingCurve.OutBounce

        duration_in_milliseconds = 250
        self.animation_2 = QPropertyAnimation(widget, b"minimumHeight")
        self.animation_2.setDuration(duration_in_milliseconds)
        self.animation_2.setStartValue(widgets_height)
        self.animation_2.setEndValue(new_height)
        self.animation_2.setEasingCurve(easing_curve)
        self.animation_2.start()
        QTimer.singleShot(duration_in_milliseconds+250, lambda: WidgetAnimator.animationFinished(animation=self.animation_2))
        flags.Flag_SliderButton_LoadData = not flags.Flag_SliderButton_LoadData

    @staticmethod
    def toggle_Frame_height_Cadaster_functions(self):
        push_button = self.pbCadasters
        widget = self.pbCadastraActions_SliderFrame
        main_widget = self.pbSettings_SliderFrame
        widgets_height = widget.height()
        aditional_height = WidgetAnimator.buttons_sliderFrame_height(self,push_button, button_padding)

        if flags.Flag_SliderButton_LoadData:
            new_height = 0
            widget.setMaximumHeight(0)
            easing_curve = QEasingCurve.InBounce
            
        else:
            new_height = aditional_height
            widget.setMaximumHeight(16777215)
            main_widget.setMaximumHeight(16777215)
            easing_curve = QEasingCurve.OutBounce

        duration_in_milliseconds = 250
        self.animation_2 = QPropertyAnimation(widget, b"minimumHeight")
        self.animation_2.setDuration(duration_in_milliseconds)
        self.animation_2.setStartValue(widgets_height)
        self.animation_2.setEndValue(new_height)
        self.animation_2.setEasingCurve(easing_curve)
        self.animation_2.start()
        QTimer.singleShot(duration_in_milliseconds+250, lambda: WidgetAnimator.animationFinished(animation=self.animation_2))
        flags.Flag_SliderButton_LoadData = not flags.Flag_SliderButton_LoadData


class FrameHandler:
    def __init__(self, frames):
        self.frames = frames  # Store frames as a dictionary
        
    def show_frame(self, frame_name):
        if frame_name in self.frames:
            self.frames[frame_name].setVisible(True)

    def hide_frame(self, frame_name):
        if frame_name in self.frames:
            self.frames[frame_name].setVisible(False)
    
    def on_load(self, frames):
        self.hide_frame("frame1") 
        self.hide_frame("frame2") 
        self.hide_frame("frame4")
        self.hide_frame("frame5")   
    def password_correct(self):
        self.show_frame("frame1")
        self.show_frame("frame2")
        self.hide_frame("frame3")
        self.show_frame("frame4")
        self.show_frame("frame5")

class LayerChecker:
    def SHP_Layer_Checker(self, input_layer_name):
        # Check if a virtual layer is present and has features
        input_layers = QgsProject.instance().mapLayersByName(input_layer_name)
        if input_layers:
            input_layer = input_layers[0]  # Get the first layer from the list
            if isinstance(input_layer, QgsVectorLayer):
                feature_count = input_layer.featureCount()
                #print("Feature Count:", feature_count)  # Print the feature count for debugging

                if feature_count > 0:
                    pass
                else:
                    SHP_layer_not_present()
            else:
                SHP_layer_not_present()
        else:
            SHP_layer_not_present()

class color_handler:

    def changeButtonColor(self, pbCadasters, pbExpand, pbRefresh, pbSyncMailabl, pbAvaMaaameti_veebikas, pbAdd_SHP_To_Project, input_layer_name, Start_update):
        # Check if a virtual layer is present and has features
        input_layers = QgsProject.instance().mapLayersByName(input_layer_name)
        if input_layers:
            input_layer = input_layers[0]  # Get the first layer from the list
            if isinstance(input_layer, QgsVectorLayer):
                feature_count = input_layer.featureCount()
                #print("Feature Count:", feature_count)  # Print the feature count for debugging

                if feature_count > 0:
                    Start_update.setStyleSheet(background_green)
                    pbAvaMaaameti_veebikas.setStyleSheet(background_green)
                    pbAdd_SHP_To_Project.setStyleSheet(background_green)
                    pbAdd_SHP_To_Project.setText("Katastrid laetud")
                    #activate buttons
                    pbExpand.blockSignals(False)
                    pbRefresh.blockSignals(False)
                    pbSyncMailabl.blockSignals(False)
                    pbExpand.setStyleSheet(background_standard_button)
                    pbRefresh.setStyleSheet(background_standard_button)
                    pbSyncMailabl.setStyleSheet(background_standard_button)                    
                    
                else:
                    #SHP_layer_not_does have data on_layer.
                    Start_update.setStyleSheet(background_red)
                    pbAdd_SHP_To_Project.setStyleSheet(background_red)
                    pbAvaMaaameti_veebikas.setStyleSheet(background_red)
                    pbAdd_SHP_To_Project.setText("Katastrite laadimine")
                    #isolate buttons                    
                    pbExpand.blockSignals(True)
                    pbRefresh.blockSignals(True)
                    pbSyncMailabl.blockSignals(True)
                    pbExpand.setStyleSheet(background_for_not_available)
                    pbRefresh.setStyleSheet(background_for_not_available)
                    pbSyncMailabl.setStyleSheet(background_for_not_available)

                    
            else:
                Start_update.setStyleSheet(background_red)
                pbAdd_SHP_To_Project.setStyleSheet(background_red)
                pbAvaMaaameti_veebikas.setStyleSheet(background_red)
                pbAdd_SHP_To_Project.setText("Katastrite laadimine")
                #isolate buttons
                pbExpand.blockSignals(True)
                pbRefresh.blockSignals(True)
                pbSyncMailabl.blockSignals(True)
                pbExpand.setStyleSheet(background_for_not_available)
                pbRefresh.setStyleSheet(background_for_not_available)
                pbSyncMailabl.setStyleSheet(background_for_not_available)

        else:
            Start_update.setStyleSheet(background_red)
            pbAdd_SHP_To_Project.setStyleSheet(background_red)
            pbAvaMaaameti_veebikas.setStyleSheet(background_red)
            pbAdd_SHP_To_Project.setText("Katastrite laadimine")
            #isolate buttons
            pbExpand.blockSignals(True)
            pbRefresh.blockSignals(True)
            pbSyncMailabl.blockSignals(True)
            pbExpand.setStyleSheet(background_for_not_available)
            pbRefresh.setStyleSheet(background_for_not_available)
            pbSyncMailabl.setStyleSheet(background_for_not_available)


class stackedWidgetsSpaces:
    #Stacked_widgets
    
    EMPTY_PAGE = "Empty"
    SETTINGS_MAIN_PAGE = "SettingsMain"
    LOAD_DATA_PAGE = "LoadData"
    PROPERTIES_ACTIONS_MAIN_PAGE = "PropertiesActionsMain"
    

    sw_helpMenu_mapping = {
        EMPTY_PAGE: 0,
        SETTINGS_MAIN_PAGE: 1,
        LOAD_DATA_PAGE: 2,
        PROPERTIES_ACTIONS_MAIN_PAGE: 3
        }
    
    def change_help_content(self,stacked_widget, page_name):
        print(f"page_name {page_name}")
        print(f"Stacked widget {stacked_widget}")
        if page_name in self.sw_helpMenu_mapping:
            index = self.sw_helpMenu_mapping[page_name]
            print(f"index {index}")
            stacked_widget.setCurrentIndex(index)
        else:
            print(f"Page '{page_name}' not found in the mapping.")
            
class alter_containers():
    
    def toggle_right_menu(self, length, buttons, original_texts, new_texts, help_menu, container, container_width):
        if length == 0:
            for button in buttons:
                button.setText(original_texts[button])
                help_menu.show()
                new_width = 250
    #            print(f"new height {new_height}")
                easing_curve = QEasingCurve.OutBounce

        else:
            for button in buttons:
                button.setText(new_texts[button])
                new_width = 65
                #print(f"new width {new_width}")
                easing_curve = QEasingCurve.OutBounce
                help_menu.hide()
                
        self.animation = QPropertyAnimation(container, b"minimumWidth")
        self.animation.setDuration(350)
        self.animation.setStartValue(container_width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(easing_curve)  # Set the easing curve here
        self.animation.start()

    def toggle_left_menu(self, length, buttons, original_texts, new_texts, help_menu, container, container_width):
        if length == 0:
            for button in buttons:
                button.setText(original_texts[button])
                #help_menu.show()
                new_width = 197
    #            print(f"new height {new_height}")
                easing_curve = QEasingCurve.OutBounce

        else:
            for button in buttons:
                button.setText(new_texts[button])
                new_width = 63
                #print(f"new width {new_width}")
                easing_curve = QEasingCurve.OutBounce
                #help_menu.hide()
                
        self.animation = QPropertyAnimation(container, b"minimumWidth")
        self.animation.setDuration(350)
        self.animation.setStartValue(container_width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(easing_curve)  # Set the easing curve here
        self.animation.start()
