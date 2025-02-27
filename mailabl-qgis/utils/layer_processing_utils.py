from ..app.View_tools import shp_tools, LayerProcessor


def retrieve_and_process_layer(layer_name, filter_function, process_function):
    """
    Helper function to retrieve a layer and process it using LayerProcessor.
    """
    processor = LayerProcessor()
    return processor.process_layer_with_progress(
        layer_name=layer_name,
        filter_function=filter_function,
        process_function=process_function
    )


def apply_subset_filter(layer, layer_name, county_field=None, state_field=None, city_field=None,
                        county_restriction=None, state_restrictions=None):
    """
    Applies a subset filter to the layer. Fields and restrictions can be optional.
    """
    expression_parts = []

    if county_field and county_restriction:
        expression_parts.append(f"\"{county_field}\" = '{county_restriction}'")

    if state_field and state_restrictions:
        states = "', '".join(state_restrictions)
        expression_parts.append(f"\"{state_field}\" IN ('{states}')")

    if city_field:
        expression_parts.append(f"\"{city_field}\" IS NOT NULL")

    # Combine expressions if there are any
    expression = " AND ".join(expression_parts) if expression_parts else ""

    # Apply the expression to the layer
    layer.setSubsetString(expression)
    layer.triggerRepaint()
    layer.updateExtents()
    shp_tools.activateLayer_zoomTo(layer)


def no_filter(feature):
    """
    Helper function that always returns True, used when no filtering is needed.
    """
    return True