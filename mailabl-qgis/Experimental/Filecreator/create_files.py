#use this line to create multiple files in same folder




import os
class creator:
    def create_files(filenames):
        # Get the current directory of the script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        for filename in filenames:
            # Create the full path for each file
            file_path = os.path.join(current_dir, f"{filename}.py")
            
            # Check if the file already exists
            if not os.path.exists(file_path):
                # Create an empty file if it does not exist
                with open(file_path, 'w') as file:
                    pass
                print(f"Created: {file_path}")
            else:
                print(f"File already exists: {file_path}")

    # List of filenames
    filenames = [
        "evel_attached_doc_customer",
        "evel_apartment_data",
        "evel_attached_doc_land_prem_area",
        "evel_attached_doc_plan",
        "evel_attached_doc_sn_consumer_point",
        "evel_attached_doc_sn_error_report",
        "evel_attached_doc_sn_sewer_duct",
        "evel_attached_doc_sn_sewer_node",
        "evel_attached_doc_sn_water_duct",
        "evel_attached_doc_sn_water_node",
        "evel_sn_sewer_duct",
        "evel_consumer_point",
        "evel_device",
        "evel_demarcation_point",
        "evel_customer_consumerpoint",
        "evel_customer",
        "evel_contract",
        "evel_external_doc",
        "evel_external_doc_type",
        "evel_flow_meter",
        "evel_sn_constant",
        "evel_sn_fire_plug",
        "evel_sn_operation",
        "evel_sn_sewer_branch",
        "evel_sn_sewer_duct_error",
        "evel_sn_sewer_duct_program",
        "evel_sn_sewer_manhole",
        "evel_sn_sewer_node",
        "evel_sn_sewer_node_error",
        "evel_sn_sewer_node_program",
        "evel_sn_sewer_other_node",
        "evel_sn_sewer_pump",
        "evel_sn_sewer_pumping_station",
        "evel_sn_sewer_valve",
        "evel_sn_sewer_valve_state_log",
        "evel_sn_water_branch",
        "evel_sn_water_duct",
        "evel_sn_water_duct_error",
        "evel_sn_water_duct_program",
        "evel_sn_water_manhole",
        "evel_sn_water_node",
        "evel_sn_water_node_error",
        "evel_sn_water_node_program",
        "evel_sn_water_other_node",
        "evel_sn_water_pressure_station",
        "evel_sn_water_pump",
        "evel_sn_water_pumping_station",
        "evel_sn_water_tank",
        "evel_sn_water_valve",
        "evel_sn_water_valve_state_log",
        "evel_building_area",
        "evel_sn_operation"
    ]

