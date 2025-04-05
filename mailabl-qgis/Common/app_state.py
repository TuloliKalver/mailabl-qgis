# app_state.py

from typing import Dict, Any
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus

class PropertiesProcessStage:
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
    current_flow_stage = None

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
        cls.current_flow_stage = None
        cls.current_process = None

    @classmethod
    def clear_flow_and_processes (cls):
        cls.active_process = None
        cls.loaded_layers = {}
        cls.active_layer = None
        cls.current_flow_stage = None
        cls.current_process = None


class Processes:
    """
    Enumerates the possible states of the processes.
    """
    ADD = "Kinnistute lisamine"
    EDIT = "Andmete muutmine"
    REMOVE = "Kinnistute eemaldamine"

class Layers_NEED_CENTRALIZING:
    from ..config.settings import StoredLayers

    IMPORT_LAYER_NAME = StoredLayers.import_layer_name()
    USER_LAYER_NAME = StoredLayers.users_properties_layer_name()


class MainVariables:
    NAME = "name"
    ACTIVATE = "activated"
    CLEANUP = "cleanup"
    Layer = "layer"
    MAX_ID = "max_fid"
    IS_ARCHIVE = "is_archive"
    
class FlowStages:
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
    def forward_stage(cls):
        # Store the current state
        stage = PropertiesProcessStage.current_flow_stage
        mapping = Expressions.FLOW_EXPRESSION_MAPPING.get(stage, {})
        next_flow = mapping.get("next_flow")
        #print(f"Process when started is set to {state}")        
        #print(f"Planned next flow {next_flow}")        
        PropertiesProcessStage.current_flow_stage = next_flow



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
        FlowStages.COUNTY: {
            'field': Katastriyksus.mk_nimi,
            'next_flow': FlowStages.PRE_STATE,
            'attribute': 'selected_counties',
            'builder': lambda cache: Expressions.build_in_expression(
                Katastriyksus.mk_nimi, cache.get('selected_counties', [])
            ),
            'buttons_enable': [],
            'buttons_disable': ['pbConfirmAction']
        },
        FlowStages.PRE_STATE: {
            'field': Katastriyksus.mk_nimi,
            'next_flow': FlowStages.STATE,
            'attribute': 'selected_municipalities',
            'builder': lambda cache: Expressions.build_in_expression(
                Katastriyksus.mk_nimi, cache.get('selected_counties', [])
            ),
            'buttons_enable': [],
            'buttons_disable': ['pbConfirmAction', 'pbCancelAction'],
            'list_widget_input': 'lvCounty',
            'list_widget_target': 'lvState',
        },
        FlowStages.STATE: {
            'field': Katastriyksus.mk_nimi,
            'target_field': Katastriyksus.ov_nimi,
            'next_flow': FlowStages.PRE_MUNICIPALITY,
            'attribute': 'selected_state',
            'builder': lambda cache: Expressions.combine_expressions([
                Expressions.build_in_expression(Katastriyksus.mk_nimi, cache.get('selected_counties', [])),
                Expressions.build_in_expression(Katastriyksus.ov_nimi, cache.get('selected_state', []))
            ]),

            'buttons_enable': ['pbCancelAction'],
            'buttons_disable': ['pbConfirmAction'],
            'list_widget_input': 'lvCounty',
            'list_widget_target': 'lvState',
        },
        FlowStages.PRE_MUNICIPALITY: {
            'field': Katastriyksus.ay_nimi,
            'target_field': Katastriyksus.ov_nimi,
            'next_flow': FlowStages.MUNICIPALITY,
            'attribute': 'selected_municipalities',
            # Combine the county and municipality expressions from the cache
            'builder': lambda cache: Expressions.combine_expressions([
                Expressions.build_in_expression(Katastriyksus.mk_nimi, cache.get('selected_counties', [])),
                Expressions.build_in_expression(Katastriyksus.ov_nimi, cache.get('selected_state', []))
            ]),
            'buttons_enable': [],
            'buttons_disable': ['pbConfirmAction'],
            'list_widget_input': 'lvState',
            'list_widget_target': 'lvSettlement',
        },

        FlowStages.MUNICIPALITY: {
            'field': Katastriyksus.ay_nimi,
            'target_field': Katastriyksus.ay_nimi,
            'next_flow': FlowStages.PREVIEW,
            'attribute': 'selected_municipalities',
            'builder': lambda cache: Expressions.combine_expressions([
                Expressions.build_in_expression(Katastriyksus.mk_nimi, cache.get('selected_counties', [])),
                Expressions.build_in_expression(Katastriyksus.ov_nimi, cache.get('selected_state', [])),
            ]),
            'buttons_enable': [],
            'buttons_disable': ['pbConfirmAction'],
            'list_widget_input': 'lvState',
            'list_widget_target': 'lvSettlement',
        },
        FlowStages.PREVIEW: {
            'field': Katastriyksus.ov_nimi,
            'extra_field': Katastriyksus.ay_nimi,
            'target_field': Katastriyksus.ay_nimi,
            'next_flow': FlowStages.PREVIEW,
            'attribute': None,
            'builder': lambda cache: Expressions.combine_expressions([
                Expressions.build_in_expression(Katastriyksus.mk_nimi, cache.get('selected_counties', [])),
                Expressions.build_in_expression(Katastriyksus.ov_nimi, cache.get('selected_state', [])),
                Expressions.build_in_expression(Katastriyksus.ay_nimi, cache.get('selected_settlements', [])),    
            ]),
            
            'buttons_enable': [],
            'buttons_disable': [],
        },
        FlowStages.COMPLETE: {
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
        FlowStages.CANCEL: {
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
        flow = PropertiesProcessStage.current_flow_stage
        mapping = cls.FLOW_EXPRESSION_MAPPING.get(flow, {})
        return mapping.get('field', '')
