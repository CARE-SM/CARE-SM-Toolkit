from copy import deepcopy

class Template_OBO:

    base_template = dict(
        pid=None,
        role_type=None,
        process_type=None,
        attribute_type=None,
        organisation_id=None,
        organisation_type=None,
        input_type=None,
        target_type=None,
        output_type=None,
        unit_type=None,
        specific_method_type=None,
        specification_type=None,
        protocol_type=None,
        protocol_id=None,
        cause_type=None,
        functional_specification_type=None,
        frequency_type=None,
        frequency_value=None,
        notation_id=None,
        notation_type=None,
        value_date=None,
        value_integer=None,
        value_string=None,
        value_float=None,
        value_datatype=None,
        value_id=None,
        comments=None,
        startdate=None,
        enddate=None,
        age=None,
        uniqid=None,
        event_id=None,
        value=None,
        valueIRI=None,
        activity=None,
        target=None,
        agent=None,
        input=None,
        unit=None,
        # protocol=None
    )

    @classmethod
    def build_entry(cls, **overrides):
        entry = deepcopy(cls.base_template)
        entry.update(overrides)
        return entry

TEMPLATE_MAP_OBO = {

        "Birthdate": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C142470",
            attribute_type="http://purl.obolibrary.org/obo/NCIT_C68615",
            output_type="http://purl.obolibrary.org/obo/NCIT_C70856",
            value_datatype="xsd:date"
        ),
        "Birthyear": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C142470",
            attribute_type="http://purl.obolibrary.org/obo/NCIT_C83164",
            output_type="http://purl.obolibrary.org/obo/NCIT_C70856",
            value_datatype="xsd:integer"
        ),
        "Country": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C142470",
            output_type="http://purl.obolibrary.org/obo/NCIT_C20108",
            value_datatype="xsd:string"
        ),
        "Deathdate": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C142470",
            attribute_type="http://purl.obolibrary.org/obo/NCIT_C70810",
            output_type="http://purl.obolibrary.org/obo/NCIT_C70856",
            specification_type="http://purl.obolibrary.org/obo/NCIT_C163970",
            value_datatype="xsd:date"
        ),
        "First_visit": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C142470",
            attribute_type="http://purl.obolibrary.org/obo/NCIT_C164021",
            output_type="http://purl.obolibrary.org/obo/NCIT_C70856",
            value_datatype="xsd:date"
        ),
        "Symptoms_onset": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C142470",
            attribute_type="http://purl.obolibrary.org/obo/NCIT_C124353",
            output_type="http://purl.obolibrary.org/obo/NCIT_C70856",
            value_datatype="xsd:date"
        ),
        "Sex": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C142470",
            output_type="http://purl.obolibrary.org/obo/NCIT_C160908",
            value_datatype="xsd:string"
        ),
        "Status": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C142470",
            output_type="http://purl.obolibrary.org/obo/NCIT_C164628",
            value_datatype="xsd:string"
        ),
        "Diagnosis": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C18020",
            output_type="http://purl.obolibrary.org/obo/NCIT_C154625",
            value_datatype="xsd:string"
        ),
        "Phenotype": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C18020",
            output_type="http://purl.obolibrary.org/obo/NCIT_C16977",
            value_datatype="xsd:string"
        ),
        "Genetic": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C15709",
            output_type="http://purl.obolibrary.org/obo/NCIT_C164607",
            specification_type="http://purl.obolibrary.org/obo/NCIT_C171178",
            value_datatype="xsd:string"
        ),
        "Examination": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/MAXO_0000487",
            output_type="http://purl.obolibrary.org/obo/NCIT_C70856",
            value_datatype="xsd:float"
        ),
        "Laboratory": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C25294",
            output_type="http://purl.obolibrary.org/obo/NCIT_C70856",
            protocol_type="http://purl.obolibrary.org/obo/OBI_0000272",
            value_datatype="xsd:float"
        ),
        "Surgery": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type = "http://purl.obolibrary.org/obo/NCIT_C15329",
            value_datatype = "xsd:string"
        ),
        "Hospitalization": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type = "http://purl.obolibrary.org/obo/NCIT_C25179",
            value_datatype = "xsd:string"
        ),
        "Prescription": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type = "http://purl.obolibrary.org/obo/NCIT_C70962",
            output_type = "http://purl.obolibrary.org/obo/NCIT_C198143",
            protocol_type = "http://purl.obolibrary.org/obo/IAO_0000104",
            specification_type = "http://purl.obolibrary.org/obo/PDRO_0000191",        
            notation_type = "http://purl.obolibrary.org/obo/NCIT_C177929",
            value_datatype = "xsd:float"
        ),
        "Medication": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type = "http://purl.obolibrary.org/obo/NCIT_C70962",
            output_type = "http://purl.obolibrary.org/obo/NCIT_C167190",
            protocol_type = "http://purl.obolibrary.org/obo/IAO_0000104",
            specification_type = "http://purl.obolibrary.org/obo/PDRO_0010022",        
            notation_type = "http://purl.obolibrary.org/obo/NCIT_C177929",
            value_datatype = "xsd:float"
        ),
        "Clinical_trial": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000097",
            process_type = "http://purl.obolibrary.org/obo/NCIT_C71104",
            organisation_type = "http://purl.obolibrary.org/obo/NCIT_C16696",
            output_type = "http://purl.obolibrary.org/obo/NCIT_C83082",
            specification_type = "http://purl.obolibrary.org/obo/NCIT_C142439",
            value_datatype = "xsd:string"
        ),
        "Biobank": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type = "http://purl.obolibrary.org/obo/OMIABIS_0000061",
            organisation_type = "http://purl.obolibrary.org/obo/OBIB_0000616",
            output_type = "http://purl.obolibrary.org/obo/NCIT_C115570", 
            value_datatype = "xsd:string"
        ),
        "Questionnaire": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C20993",
            output_type="http://purl.obolibrary.org/obo/NCIT_C91102",
            value_datatype="xsd:float"
        ),
        # "PRO": Template_OBO.build_entry(
        #     role_type="http://purl.obolibrary.org/obo/OBI_0000093",
        #     process_type="http://purl.obolibrary.org/obo/NCIT_C95401",
        #     output_type="http://purl.obolibrary.org/obo/NCIT_C91102",
        #     value_datatype="xsd:float"
        # ),
        "Disability": Template_OBO.build_entry(
            role_type="http://purl.obolibrary.org/obo/OBI_0000093",
            process_type="http://purl.obolibrary.org/obo/NCIT_C20993",
            attribute_type="http://purl.obolibrary.org/obo/NCIT_C21007",
            output_type="http://purl.obolibrary.org/obo/NCIT_C91102",
            value_datatype="xsd:float"
        ),
    }

class Template_SNOMED:

    base_template = dict(
        pid=None,
        role_type="http://snomed.info/id/116154003",
        process_type=None,
        attribute_type=None,
        organisation_id=None,
        organisation_type=None,
        input_type=None,
        target_type=None,
        output_type=None,
        unit_type=None,
        specific_method_type=None,
        specification_type=None,
        protocol_type=None,
        protocol_id=None,
        cause_type=None,
        functional_specification_type=None,
        frequency_type=None,
        frequency_value=None,
        notation_id=None,
        notation_type=None,
        value_date=None,
        value_integer=None,
        value_string=None,
        value_float=None,
        value_datatype=None,
        value_id=None,
        comments=None,
        startdate=None,
        enddate=None,
        age=None,
        uniqid=None,
        event_id=None,
        value=None,
        valueIRI=None,
        activity=None,
        target=None,
        agent=None,
        input=None,
        unit=None
    )

    @classmethod
    def build_entry(cls, **overrides):
        entry = deepcopy(cls.base_template)
        entry.update(overrides)
        return entry

TEMPLATE_MAP_SNOMED = {
        "Birthdate": Template_SNOMED.build_entry(
            process_type="http://snomed.info/id/312486000",
            attribute_type="http://snomed.info/id/3950001",
            output_type="http://snomed.info/id/184099003",
            value_datatype="xsd:date"
        ),
        "Birthyear": Template_SNOMED.build_entry(
            process_type="http://snomed.info/id/312486000",
            attribute_type="http://snomed.info/id/3950001",
            output_type="http://snomed.info/id/258707000",
            value_datatype="xsd:integer"
        ),
        "Country": Template_OBO.build_entry(
            process_type="http://snomed.info/id/312486000",
            output_type="http://snomed.info/id/169812000",
            value_datatype="xsd:integer"
        ),
        "Deathdate": Template_SNOMED.build_entry(
            process_type="http://snomed.info/id/363049002",
            attribute_type="http://snomed.info/id/419620001",
            output_type="http://snomed.info/id/399753006",
            specification_type="http://snomed.info/id/307930005",
            value_datatype="xsd:date"
        ),
        "First_visit": Template_SNOMED.build_entry(
            process_type="http://snomed.info/id/308335008",
            attribute_type="http://snomed.info/id/769681006",
            output_type="http://snomed.info/id/406543005",
            value_datatype="xsd:date"
        ),
        "Symptoms_onset": Template_SNOMED.build_entry(
            process_type="http://snomed.info/id/308335008",
            attribute_type="http://snomed.info/id/308918001",
            output_type="http://snomed.info/id/298059007",
            value_datatype="xsd:date"
        ),
        "Sex": Template_SNOMED.build_entry(
            process_type="http://snomed.info/id/312486000",
            output_type="http://snomed.info/id/734000001",
            value_datatype="xsd:string"
        ),
        "Status": Template_SNOMED.build_entry(
            process_type="http://snomed.info/id/386053000",
            output_type="http://snomed.info/id/420107008",
            value_datatype="xsd:string"
        ),
        "Diagnosis": Template_SNOMED.build_entry(
            process_type="http://snomed.info/id/103693007",
            output_type="http://snomed.info/id/439401001",
            value_datatype="xsd:string"
        ),
        "Phenotype": Template_SNOMED.build_entry(
            process_type="http://snomed.info/id/363778006",
            output_type="http://snomed.info/id/8116006",
            value_datatype="xsd:string"
        ),
        "Disability": Template_SNOMED.build_entry(
            process_type="http://snomed.info/id/81078003",
            attribute_type="http://snomed.info/id/21134002",
            output_type="http://snomed.info/id/273421001",
            value_datatype="xsd:float"
        ),
        "Examination": Template_SNOMED.build_entry(
            process_type="http://snomed.info/id/315306007",
            output_type="http://snomed.info/id/363789004",
            value_datatype="xsd:float"
        ),
        "Laboratory": Template_SNOMED.build_entry(
            process_type="http://snomed.info/id/108252007",
            output_type="http://snomed.info/id/4241000179101",
            specification_type="http://snomed.info/id/258049002",
            value_datatype="xsd:float"
        ),
        "Surgery": Template_SNOMED.build_entry(
            process_type = "http://snomed.info/id/387713003",
            value_datatype = "xsd:string"
        ),
        "Hospitalization": Template_SNOMED.build_entry(
            process_type = "https://loinc.org/LA15417-1",
            value_datatype = "xsd:string"
        ),
        "Prescription": Template_SNOMED.build_entry(
            process_type = "http://snomed.info/id/33633005",
            specification_type = "http://snomed.info/id/761938008",        
            notation_type = "http://snomed.info/id/246488008",      
            output_type = "http://snomed.info/id/3317411000001100",
            value_datatype = "xsd:float"
        ),
        "Medication": Template_SNOMED.build_entry(
            process_type = "http://snomed.info/id/18629005",
            specification_type = "http://snomed.info/id/761938008",        
            notation_type = "http://snomed.info/id/246488008",      
            output_type = "https://loinc.org/18615-5",
            value_datatype = "xsd:float"
        ),
        "Clinical_trial": Template_SNOMED.build_entry(
            process_type = "http://snomed.info/id/110465008",
            organization_type = "http://snomed.info/id/22232009",
            output_type = "http://snomed.info/id/229059009", 
            value_datatype = "xsd:string"
        ),
        "Biobank": Template_SNOMED.build_entry(
            process_type = "http://snomed.info/id/433465004",
            organisation_type = "http://snomed.info/id/246488008",      
            output_type = "http://snomed.info/id/364611000000101",
            value_datatype = "xsd:float"
        )
    }