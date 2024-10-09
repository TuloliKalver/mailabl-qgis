class MailablGroupLayers:
    MAILABL_MAIN_GROUP_NAME = 'Mailabl settings'  # Main group name
    IMPORT_LAYER_NAME = 'Imporditavad kinnistud'  # Name for importable properties
    NEW_PROPERTIES_NAME = 'Uued kinnistud'  # Name for new properties
    #CHANGED_PROPERTIES_NAME = 'Muutunud andmed'  # Name for changed properties
    TEMP_GRPUP_NAME = 'Ajutised kihid'  # Name for tools layer
    PROPERTIES_ARCHIVE = "Arhiiv"

    GropupLayers = {IMPORT_LAYER_NAME,
                    NEW_PROPERTIES_NAME,
                    #CHANGED_PROPERTIES_NAME,
                    #TEMP_GRPUP_NAME,
                    PROPERTIES_ARCHIVE}

class MailablLayers:
    PROPERTIES_ARCHIVE = "Arhiveeritud kinnistud"