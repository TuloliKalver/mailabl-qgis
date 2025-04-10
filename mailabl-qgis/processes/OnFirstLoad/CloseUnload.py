from ...queries.python.access_credentials import clear_UC_data
from ...queries.python.FileLoaderHelper import GraphQLQueryLoader
from ...queries.python.query_tools import requestBuilder



class Unload:

    def handle_dialog_closed():
        #clear_UC_data()
        
        # This method will be called when the dialog is about to be closed
        # Perform any necessary cleanup and resource management here
        # Reset the plugin's state and variables here
        
        pass

    def closeEvent(self, event):
        # This method will be called when the user tries to close the dialog
        # Perform cleanup and reset operations here before closing the dialog
        self.handle_dialog_closed()
        event.accept()  # Accept the close event


    # logout functionality needs to be developed
    def log_out(self):

        #query_loader = GraphQLQueryLoader()
        #query = query_loader.load_query(query_loader.Projects_statuses)
        #print(f"query: {query}")
        # Construct the request payload
        query =  {"mutation"
                        :{
             "logout" :{
                "status",
        		"message"
                      }
                    }
                    }
        variables = {}
        response = requestBuilder.construct_and_send_request(query, variables)
        print(response)
        #clear_UC_data()