from qgis.core import QgsProject,  QgsSpatialIndex
from qgis.utils import iface
from ...python.property_data import PropertiesGeneralQueries
import time
import os
import re
import json
import requests
from requests.exceptions import Timeout
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QHeaderView
from ..DataLoading_classes import GraphQLQueryLoader, Graphql_project
from ..responses import handleResponse
from ..query_tools import requestBuilder
from ....config.ui_directories import PathLoaderSimple



class visibleSelector:
    @staticmethod
    def get_visible_features(layer_name):
        #print(f"layer name: '{layer_name}'")
        # Get the layer by name
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        # Get the current extent of the map canvas
        canvas = iface.mapCanvas()
        extent = canvas.extent()
        # Create a spatial index for the layer
        index = QgsSpatialIndex(layer.getFeatures())
        # Get the features that intersect with the current extent
        intersecting_ids = index.intersects(extent)
        # Get the values of the 'Tunnus' column for the visible features
        visible_features = []
        for feature in layer.getFeatures():
            if feature.id() in intersecting_ids:
                visible_features.append(feature['TUNNUS'])
        #print(f"feature(s): '{visible_features}'")
        return visible_features
    
    
    def get_projects_list_connected_with_view_properties(self, id_values):
        #print(f"id_value: '{id_values}'")
        query_loader = Graphql_project()
        query = GraphQLQueryLoader.load_query_for_projects(self, query_loader.Q_Properties_related_projects)
        #print(f"query: {query}")
        items_for_page = 50
        end_cursor = None

        projects_list = []
        
        variables =        {
                    "first": items_for_page,
                    "after": "",
                    "where": {
                        "AND": [
                            {
                                "column": "CADASTRAL_UNIT_NUMBER",
                                "operator": "IN",
                                "value": id_values
                            }
                        ]
                    }
                }
        #print(f"variable: '{variables}'")
        while True:
            response = requestBuilder.construct_and_send_request(self, query, variables)
            
            if response.status_code == 200:
                edge = handleResponse.response_properties_data_edges(response)
                #print("edge")
                #print(edge)
                # Extract project IDs from the response
                for item in edge:
                    for project in item['node']['projects']['edges']:
                        if project['node']['id']:
                            projects_list.append(project['node'])
                            #print(f"projects_list: '{projects_list}'")
                    # Check pageInfo for pagination
                    page_info = item['node']['projects']['pageInfo']
                
                    if page_info['hasNextPage']:
                        end_cursor = page_info['endCursor']
                        variables['after'] = end_cursor
                    
                        break
                else:
                    break  # Exit loop if there are no more pages
        return projects_list