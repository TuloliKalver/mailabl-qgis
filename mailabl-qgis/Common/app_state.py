# app_state.py

from typing import Dict, Any
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus

class AppState:
    # Current active process (e.g., "add", "edit", "remove").
    active_process = None  

    # Dictionary to store loaded layers and their metadata.
    loaded_layers: Dict[str, Dict[str, Any]] = {}

    # Currently active QGIS layer.
    active_layer = None

    # Application-wide configuration settings (could be loaded from a config file).
    config: Dict[str, Any] = {}

    # Cache for frequently accessed data or computed results.
    cache: Dict[str, Any] = {}

    # This can be set to one of the states defined in FlowStates.
    current_flow_state = None

    current_process = None

    @classmethod
    def clear_all_app_states(cls):
        """
        Reset all stored variables to their initial empty or None state.
        """
        cls.active_process = None
        cls.loaded_layers = {}
        cls.active_layer = None
        cls.config = {}
        cls.cache = {}
        cls.current_flow_state = None
        cls.current_process = None

    @classmethod
    def clear_flow_and_processes (cls):
        cls.active_process = None
        cls.loaded_layers = {}
        cls.active_layer = None
        cls.current_flow_state = None
        cls.current_process = None


class Processes:
    """
    Enumerates the possible states of the processes.
    """
    ADD_MAPFEATURES = "add"
    EDIT_MAPFEATURES = "edit"
    REMOVE_MAPFEATURES = "remove"

class Layers:
    # Define layer names for consistency across the project
    IMPORT_LAYER_NAME = "Eesti"
    USER_LAYER_NAME = "uus_kiht"
    ARCHIVE_PRE_LAYER_NAME = "Arendatav_arhiiv"
    ARCHIVE_LAYER_NAME = "Minu_arhiiv"

class LayerGroups:
    ARCHIVE = "Arhiiv"
    TEMPORARY_LAYERS = "Ajutised kihid"
    ARCHIVED_PROPERTIES = "Arhiveeritud kinnistud"


class MainVaiables:
    NAME = "name"
    ACTIVATE = "activated"
    CLEANUP = "cleanup"
    Layer = "layer"
    MAX_ID = "max_fid"
    IS_ARCHIVE = "is_archive"
    
class FlowStates:
    """
    Enumerates the possible states of the application flow.
    """
    COUNTY = "county"
    PRE_STATE = "pre_state"
    STATE = "state"
    PRE_MUNICIPALITY = "pre_municipality"
    MUNICIPALITY = "municipality"
    PREVIEW = "preview"
    COMPLETE = "complete"
    CANCEL = "cancel"


    @classmethod
    def forward_flow(cls):
        # Store the current state
        state = AppState.current_flow_state
        mapping = Expressions.FLOW_EXPRESSION_MAPPING.get(state, {})
        next_flow = mapping.get("next_flow")
        #print(f"Process when started is set to {state}")        
        #print(f"Planned next flow {next_flow}")        
        AppState.current_flow_state = next_flow



class Expressions:
    
    clear = ''


    @staticmethod
    def build_in_expression(field_name, values):
        """
        Build an expression to select features where the field's value is in a list.
        """
        if not values:
            return Expressions.clear
        values_str = ",".join(f"'{v}'" for v in values)
        expression = f'"{field_name}" IN ({values_str})'
        #print("Built In Expression:")
        #print(expression)
        return expression

    @staticmethod
    def build_like_expression(field_name, pattern):
        """
        Build a LIKE expression for pattern matching.
        """
        expression = f'"{field_name}" LIKE \'{pattern}\''
        #print("Built LIKE Expression:")
        #print(expression)
        return expression

    @staticmethod
    def build_between_expression(field_name, lower, upper):
        """
        Build a BETWEEN expression for filtering values between two bounds.
        """
        expression = f'"{field_name}" BETWEEN {lower} AND {upper}'
        #print("Built BETWEEN Expression:")
        #print(expression)
        return expression

    @staticmethod
    def combine_expressions(expressions, operator="AND"):
        """
        Combine multiple expressions with a specified logical operator.
        """
        filtered_expr = [expr for expr in expressions if expr]
        if not filtered_expr:
            return Expressions.clear
        combined_expression = f" {operator} ".join(filtered_expr)
        #print("Combined Expression:")
        #print(combined_expression)
        return combined_expression



    FLOW_EXPRESSION_MAPPING = {
        FlowStates.COUNTY: {
            'field': Katastriyksus.mk_nimi,
            'next_flow': FlowStates.PRE_STATE,
            'attribute': 'selected_counties',
            'builder': lambda cache: Expressions.build_in_expression(
                Katastriyksus.mk_nimi, cache.get('selected_counties', [])
            ),
            'buttons_enable': [],
            'buttons_disable': ['btnConfirmAction']
        },
        FlowStates.PRE_STATE: {
            'field': Katastriyksus.mk_nimi,
            'next_flow': FlowStates.STATE,
            'attribute': 'selected_municipalities',
            'builder': lambda cache: Expressions.build_in_expression(
                Katastriyksus.mk_nimi, cache.get('selected_counties', [])
            ),
            'buttons_enable': [],
            'buttons_disable': ['btnConfirmAction', 'btnCancelAction'],
            'list_widget_input': 'lvCounty',
            'list_widget_target': 'lvState',
        },
        FlowStates.STATE: {
            'field': Katastriyksus.mk_nimi,
            'target_field': Katastriyksus.ov_nimi,
            'next_flow': FlowStates.PRE_MUNICIPALITY,
            'attribute': 'selected_state',
            'builder': lambda cache: Expressions.combine_expressions([
                Expressions.build_in_expression(Katastriyksus.mk_nimi, cache.get('selected_counties', [])),
                Expressions.build_in_expression(Katastriyksus.ov_nimi, cache.get('selected_state', []))
            ]),

            'buttons_enable': ['btnCancelAction'],
            'buttons_disable': ['btnConfirmAction'],
            'list_widget_input': 'lvCounty',
            'list_widget_target': 'lvState',
        },
        FlowStates.PRE_MUNICIPALITY: {
            'field': Katastriyksus.ay_nimi,
            'target_field': Katastriyksus.ov_nimi,
            'next_flow': FlowStates.MUNICIPALITY,
            'attribute': 'selected_municipalities',
            # Combine the county and municipality expressions from the cache
            'builder': lambda cache: Expressions.combine_expressions([
                Expressions.build_in_expression(Katastriyksus.mk_nimi, cache.get('selected_counties', [])),
                Expressions.build_in_expression(Katastriyksus.ov_nimi, cache.get('selected_state', []))
            ]),
            'buttons_enable': [],
            'buttons_disable': ['btnConfirmAction'],
            'list_widget_input': 'lvState',
            'list_widget_target': 'lvSettlement',
        },

        FlowStates.MUNICIPALITY: {
            'field': Katastriyksus.ay_nimi,
            'target_field': Katastriyksus.ay_nimi,
            'next_flow': FlowStates.PREVIEW,
            'attribute': 'selected_municipalities',
            'builder': lambda cache: Expressions.combine_expressions([
                Expressions.build_in_expression(Katastriyksus.mk_nimi, cache.get('selected_counties', [])),
                Expressions.build_in_expression(Katastriyksus.ov_nimi, cache.get('selected_state', [])),
            ]),
            'buttons_enable': [],
            'buttons_disable': ['btnConfirmAction'],
            'list_widget_input': 'lvState',
            'list_widget_target': 'lvSettlement',
        },
        FlowStates.PREVIEW: {
            'field': Katastriyksus.ov_nimi,
            'extra_field': Katastriyksus.ay_nimi,
            'target_field': Katastriyksus.ay_nimi,
            'next_flow': FlowStates.PREVIEW,
            'attribute': None,
            'builder': lambda cache: Expressions.combine_expressions([
                Expressions.build_in_expression(Katastriyksus.mk_nimi, cache.get('selected_counties', [])),
                Expressions.build_in_expression(Katastriyksus.ov_nimi, cache.get('selected_state', [])),
                Expressions.build_in_expression(Katastriyksus.ay_nimi, cache.get('selected_settlements', [])),    
            ]),
            
            'buttons_enable': [],
            'buttons_disable': [],
        },
        FlowStates.COMPLETE: {
            'field': Katastriyksus.mk_nimi,
            'target_field': Katastriyksus.ov_nimi,
            'extra_field': Katastriyksus.ay_nimi,
            
            'attribute': None,
            'builder': lambda cache: Expressions.combine_expressions([
                Expressions.build_in_expression(Katastriyksus.mk_nimi, cache.get('selected_counties', [])),
                Expressions.build_in_expression(Katastriyksus.ov_nimi, cache.get('selected_state', [])),
                Expressions.build_in_expression(Katastriyksus.ov_nimi, cache.get('selected_settlements', [])),    
            ]),
            'buttons_enable': [],
            'buttons_disable': [],
        },
        FlowStates.CANCEL: {
            'field': None,
            'target_field': None,
            'extra_field': None,
            'attribute': None,
            'builder': None,
            'buttons_enable': []
        }
    }

    @classmethod
    def get_mapped_field(cls):
        """
        Retrieve the field name based on the current flow state.
        """
        flow = AppState.current_flow_state
        mapping = cls.FLOW_EXPRESSION_MAPPING.get(flow, {})
        return mapping.get('field', '')
