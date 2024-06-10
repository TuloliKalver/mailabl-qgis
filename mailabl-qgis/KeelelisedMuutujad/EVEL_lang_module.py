class UICheckboxes:
    water_checkbox = "Vesi"
    sewage_checkbox = "Kanal"
    rainwater_checkbox = "Sademevesi"
    pumpstation_checkbox = "Pumpla"
    treatment_checkbox = "Reoveepuhastid"
    connectionpoint_checkbox = "Liitumispunktid"
    easement_checkbox = "Servituudid"
    services_checkbox = "Võrgusündmused"
    snconstant_checkbox = "SN-väärtused"
    

class EvelGroupLayersNames:
    # Grupi kihtide nimetused
    EVEL_MAIN = 'EVEL_Mudel'
    EASEMENT = 'Servituut'
    SERVICES = 'Töökäsud'
    ATTACHED_DOC = 'Dokumendid'
    SEWER = 'Kanalisatsioon'
    WATER = 'Vesi'
    CONSUMER_POINT = 'Tarbimispunktid'
    DEVICE = 'Seadmed'
    DEMARCATION_POINT = 'Piiritluspunktid'
    CUSTOMER = 'Kliendid'
    CONTRACT = 'Lepingud'
    EXTERNAL_DOC = 'Välisdokumendid'
    FLOW_METER = 'Voolumõõturid'
    FIRE_PLUG = 'Tuletõrjehüdrandid'
    OPERATION = 'Operatsioonid'
    ERROR = 'Veateated'
    PROGRAM = 'Programmid'
    MANHOLE = 'Kaevud'
    PUMP = 'Pumbad'
    PUMPING_STATION = 'Pumbajaamad'
    VALVE = 'Ventiilid'
    PRESSURE_STATION = 'Survejaamad'
    TANK = 'Paagid'
    BUILDING_AREA = 'Hooneala'
    APARTMENT = 'Korterid'

    



    @classmethod
    def EVEL_group_layers(cls):
        return [cls.EVEL_MAIN, 
                cls.EASEMENT, 
                cls.SERVICES]