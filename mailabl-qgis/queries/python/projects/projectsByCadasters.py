from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
from ..DataLoading_classes import Graphql_project, GraphQLQueryLoader
from ..query_tools import requestBuilder
from ....config.ui_directories import PathLoaderSimple

class projectsWhereCadasters:
    @staticmethod
    def QueryProjects_Parent_Active_Open(self, cadasters):
        widgets_path = PathLoaderSimple.widget_statusBar_path(self)
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        label_2 = progress_widget.label_2
        progress_bar.setMaximum(100)
        progress_widget.setWindowTitle("Laen projekte")
        progress_widget.show()
        
        # Load the project query using the loader instance
        query_loader = Graphql_project()
        query = GraphQLQueryLoader.load_query(self,query_loader.Q_Where_By_status_Projects)
        # Set the desired total number of items to fetch
        desired_total_items = None  # Adjust this to your desired value
        items_for_page = 50  # Adjust this to your desired value
        projects_end_cursor = None  # Initialize end_cursor before the loop
        #properties_end_cursor = None
        total_fetched = 0        # Initialize an empty list to store fetched items
        fetched_items = []
                
        while (desired_total_items is None or total_fetched < desired_total_items):#(total_fetched < limit):
            # Construct variables for the GraphQL query
            variables = {
                "first": items_for_page,
                "after": projects_end_cursor if projects_end_cursor else None,
                #"propertiesFirst": items_for_properties_page,
                #"propertiesAfter": properties_end_cursor if properties_end_cursor else None,
                "where": {
                    "AND": [
                        {
                            "column": "STATUS",
                            "operator": "IN",
                            "value": cadasters
                        },
                        {
                            "column": "PARENT_ID",
                            "value": None
                        },
                        {
                            "column": "IS_PUBLIC",
                            "value": True
                        }
                    ]
                }
            }

            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                data = response.json()
                #print("data")
                #print(data)
                fetched_data = data.get("data", {}).get("projects", {}).get("edges", [])
                projects_pageInfo = data.get("data", {}).get("projects", {}).get("pageInfo", {})
                #print(projects_pageInfo)
                projects_end_cursor = projects_pageInfo.get("endCursor")
                projects_hasNextPage = projects_pageInfo.get("hasNextPage")
                last_page = projects_pageInfo.get("lastPage")
                current_page = projects_pageInfo.get("currentPage")
                total = projects_pageInfo.get("total")
                fetched_items.extend(fetched_data)
                total_fetched += len(fetched_data)
                text = "Projekte kokku"
                #label_2.setText(text)
                if current_page == 1:
                    label_2.setText(f"{text}: {total}")
                    progress_bar.setMaximum(last_page)
                label_2.setText(f"{text}: {total}")
                progress_bar.setValue(current_page)
                QCoreApplication.processEvents()
                # Check whether the last page of projects has been reached
                if not projects_end_cursor or (desired_total_items is not None and total_fetched >= desired_total_items) or not projects_hasNextPage:
                    break

            else:
                print(f"Error: {response.status_code}")
                return None
            QCoreApplication.processEvents()

        # Return only the desired number of items
        return fetched_items[:desired_total_items]