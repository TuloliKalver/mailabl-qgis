# Example formatter functions
from PyQt5.QtCore import QDate

def default_formatter(value):
    """Default formatter: convert any value to string."""
    return str(value)

def text_formatter(value):
    """Formatter for text fields: convert to string, replace underscores with spaces, then capitalize."""
    text = str(value).replace("_", " ")
    return text.capitalize()

def date_formatter(value):
    """Helper function to format QDate values to a string format."""
    if isinstance(value, QDate):
        return value.toString("dd.MM.yyyy")
    return value

def date_formatter_for_Mailabl_insertion(value):
    if isinstance(value, QDate):
        return value.toString("yyyy-MM-dd")
    return value


def number_formatter(value):
    """Formatter for numeric fields: convert to string (or use more elaborate formatting)."""
    return str(value)

def percentage_formatter(value):
    """Formatter for percentage values: format as float with a percent sign."""
    try:
        return f"{float(value)}%"
    except (ValueError, TypeError):
        return str(value)

def area_formatter(value):
    """Formatter for area values: format as a float with two decimals."""
    try:
        return f"{float(value)}"
    except (ValueError, TypeError):
        return str(value)

# Mapping field names to their corresponding formatter functions.
# The keys (right-hand side of the "=" in your definitions) are used here.
formatters = {
    "fid": default_formatter,         # Base ID, likely numeric
    "tunnus": text_formatter,         # Text field
    "hkood": text_formatter,          # Text field
    #"mk_nimi": text_formatter,        # Region name, text
    #"ov_nimi": text_formatter,        # Municipality name, text
    #"ay_nimi": text_formatter,        # Settlement name, text
    #"l_aadress": text_formatter,      # Address, text
    "registr": date_formatter,        # Registration date
    "muudet": date_formatter,         # Last modification date
    "siht1": text_formatter,          # Text field
    "siht2": text_formatter,          # Text field
    "siht3": text_formatter,          # Text field
    "so_prts1": percentage_formatter, # Percentage field
    "so_prts2": percentage_formatter, # Percentage field
    "so_prts3": percentage_formatter, # Percentage field
    "pindala": area_formatter,        # Area, numeric
    "haritav": text_formatter,        # Text field
    "rohumaa": text_formatter,        # Text field
    "mets": text_formatter,           # Text field
    "ouemaa": text_formatter,         # Text field
    "muumaa": text_formatter,         # Text field
    "kinnistu": text_formatter,       # Plot number, text (or numeric)
    "omvorm": text_formatter,         # Ownership form, text
    "maks_hind": number_formatter,    # Maximum price, numeric
    "marked": text_formatter,         # Text field
    "eksport": text_formatter         # Text field
}

# A helper function to apply formatting to a field value.
def format_field(field_name, value):
    """
    Returns a formatted value for a given field name.
    If the value is None or a string "NULL" (case insensitive), returns a placeholder.
    """
    if value is None or str(value).upper() == "NULL":
        return "---"
    
    # Retrieve the appropriate formatter; default to default_formatter if not found.
    formatter = formatters.get(field_name, default_formatter)
    return formatter(value)

# Usage Example:
# Assuming field_indices is a dictionary mapping field names to their respective indices:
# field_indices = {'fid': 0, 'tunnus': 1, 'hkood': 2, ...}


"""
data = []
for feature in layer.getFeatures(request):
    row = [
        format_field(field_name, feature[field_idx])
        for field_name, field_idx in field_indices.items()
    ]
    data.append(row)
"""