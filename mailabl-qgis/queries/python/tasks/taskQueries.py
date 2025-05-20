from PyQt5.QtCore import Qt

from ....KeelelisedMuutujad.modules import Module
from ....utils.ProgressHelper import ProgressDialogModern    
from ....queries.python.FileLoaderHelper import GraphqlTasks, GraphQLQueryLoader
from ....queries.python.query_tools import requestBuilder

class CreateTask:

    @staticmethod
    def Create_Task (variables):
        
        module = Module.TASK
        progress = ProgressDialogModern(title=f"Lisan", value=0)
        progress.update(1, purpouse="Töötlen", text1="Palun oota...")

        query_name =  GraphqlTasks.CREATE_TASK
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)
        
    
        response = requestBuilder.construct_and_send_create_request(query, variables) 
        # Get the task ID if available
        task_data = response.get("data", {}).get("createTask", {})
        #print("create Task Data:")
        #print(task_data)
        task_id = task_data.get("id")
        
        if task_id:
            print(f"✅ Task created with ID: {task_id}")
        else:
            print("⚠️ No task ID found. Possible GraphQL error.")
            print("Errors:", response.get("errors", []))

        progress.update(98)
        progress.close()
        return task_id

    @staticmethod
    def prepare_associate_variable(checkable_combobox, responsible_id=None): 
        # Build the members.associate list
        associate_members = []

        # Step 1: Add all checked users
        for i in range(checkable_combobox.count()):
            if checkable_combobox.itemData(i, Qt.CheckStateRole) == Qt.Checked:
                user_id = checkable_combobox.itemData(i, Qt.UserRole)
                associate_members.append({"id": user_id})

        # Step 2: Ensure responsible is added and flagged
        if responsible_id:
            # Check if already in associate list
            found = False
            for member in associate_members:
                if member["id"] == responsible_id:
                    member["isResponsible"] = True
                    found = True
                    break
            if not found:
                # Not in the list yet, add with responsible flag
                associate_members.append({
                    "id": responsible_id,
                    "isResponsible": True
                })
        
        return associate_members