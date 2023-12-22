import pandas as pd
from perseo.main import milisec

class Toolkit:

    def import_your_data_from_csv(self, input_data):
      try:
          data = pd.read_csv(input_data)
          return data
      except FileNotFoundError:
          print(f"File not found: {input_data}")
          return None
      except pd.errors.EmptyDataError:
          print(f"The CSV file is empty: {input_data}")
          return None
      except pd.errors.ParserError:
          print(f"Error parsing the CSV file: {input_data}")
          return None
      
    ## Check the status of the columns
    def check_status_column_names(self, data):
        column_names = ["model", "pid", "event_id", "value", "age", "value_datatype", "valueIRI", "process_type", "unit_type", "input_type", "target_type", "frequency_type", "frequency_value", "agent_id", "route_type", "startdate", "enddate", "comments"]

        for name in column_names:
            if name not in data.columns:
                return False
        return data

    def check_for_duplicated_titles_among_row(self, data):
        count = 0
        for value in data["model"]:
            if value == "model":
                count += 1
        return count > 0
        
    ## Add ontological columns
    def add_columns_from_template(self,data):
        
        data = data.where(pd.notnull(data), None)

        temp = Template.template_model
        final_df = pd.DataFrame()
        row_df = dict()

        for row in data.iterrows():
            milisec_point = milisec()

            # Tag each row with the new of the model 
            new_row = {milisec_point : {"model": row[1]["model"]}}
            row_df.update(new_row)

            # Include columns related to ontological terms:
            for cde in temp.items():
                if cde[0] == row_df[milisec_point]["model"]:
                    row_df[milisec_point].update(cde[1])

            # Include columns from input CSV table:
            for title, val in row[1].items():
                if not val == None:
                    row_df[milisec_point].update({title:val})

            # Concate rows:
            final_row_df = pd.DataFrame(row_df[milisec_point], index=[1])
            final_df = pd.concat([final_df, final_row_df])

        final_df = final_df.reset_index(drop=True)

        final_df = final_df.where(pd.notnull(final_df), None)
        return final_df
      
      
      
    def transform_shape_based_on_config(self, configuration, data):
        
        # Import static template for all CDE terms:
        temp = Template.template_model
        
        # Empty objects:
        final_df = pd.DataFrame()
        row_df = {}

        # Iterate each row from data input
        # check each YAML object from configuration file to set the parameters
        for row in data.iterrows():

            for config in configuration.items():

                # Create a unique stamp per new row to about them to colapse:
                milisec_point = milisec()

                row_df.update({milisec_point: {'model':config[1]["cde"]}})
                
                # Add YAML template static information
                for cde in temp.items():
                    if cde[0] == row_df[milisec_point]["model"]:
                        row_df[milisec_point].update(cde[1])

                # Relate each YAML parameter with original data input
                for element in config[1]["columns"].items():
                    for r in row[1].index:
                        if r == element[1]:
                            dict_element = {element[0]:row[1][r]}
                            row_df[milisec_point].update(dict_element)
                            

                # Store formed element into the final table:
                final_row_df = pd.DataFrame(row_df[milisec_point], index=[1])
                final_df = pd.concat([final_df, final_row_df])

        final_df = final_df.reset_index(drop=True)

        final_df = final_df.where(pd.notnull(final_df), None)
        return final_df

    ## Value edition
    def value_edition(self, data):
        
        for index, row in data.iterrows():

            # Based on the value_datatype, add value
            if row["value_datatype"] == "xsd:string":
                data.at[index, "value_string"] = data["value"][index]

            if row["value_datatype"] == "xsd:float":
                data.at[index, "value_float"] = data["value"][index]

            if row["value_datatype"] == "xsd:integer":
                data.at[index, "value_integer"] = data["value"][index] #.astype('int64')

            if row["value_datatype"] == "xsd:date":
                data.at[index, "value_date"] = data["value"][index]

            ## Depends of model, valueIRI or value goes to attribute, output or concentration
            if row["model"] in ["Sex","Status","Diagnosis","Symptom","Clinical_trial"]:
                data.at[index, "attribute_type"] = data["valueIRI"][index]

            if row["model"] in ["Genetic","Imaging"]:
                data.at[index, "output_id"] = data["valueIRI"][index]
                
            if row["model"] in ["Medication"]:
                data.at[index, "concentration_value"] = data["value"][index]

            data = data.where(pd.notnull(data), None)

        return data     

    # Time edition
    def time_edition(self, data):

        for index, row in data.iterrows():
            data = data.where(pd.notnull(data), None)

            ## From value_date to stardate
            data = data.where(pd.notnull(data), None)
            if row["value_date"] != None and row["startdate"] == None:
                data.at[index,"date"] = data["value_date"][index]

        for index, row in data.iterrows():
            data = data.where(pd.notnull(data), None)
            
            ## From age to value when date is None #TODO improve this part
            data = data.where(pd.notnull(data), None)
            if row["age"] == None and row["value_integer"] != None and row["model"] in ["Deathdate","First_visit","Symptoms_onset"]:
                data.at[index, "value_integer"] = data["age"][index]
                
        for index, row in data.iterrows():
            data = data.where(pd.notnull(data), None)
            ## From startdate to enddate
            data = data.where(pd.notnull(data), None)
            if row["startdate"] != None and row["enddate"] == None:
                data.at[index,"enddate"] = data["startdate"][index]
            # print(row["enddate"])

            
        data = data.where(pd.notnull(data), None)
        return data

    ## Clean rows with no value
    def clean_empty_rows(self, data): # TODO solve the attribute_type value problem

        for row_final in data.iterrows():
            if row_final[1]["value"] == None and row_final[1]["valueIRI"] == None and row_final[1]["activity_type"] == None and row_final[1]["target_type"] == None and row_final[1]["model"] not in ["Biobank", "Consent_used", "Consent_contacted"]:
                data = data.drop(row_final[0])
        return data
    
    def delete_extra_columns(self, data):

        del data["value"]
        del data["valueIRI"]

        return data
    
    def unique_id_generation(self,data):
        data['uniqid'] = ""

        for i in data.index:
            data.at[i, "uniqid"] = milisec()
        
        return data

    def whole_quality_control(self,input_data):

        imported_file = self.import_your_data_from_csv(input_data)
        if imported_file is not None:
            print("CSV file imported successfully.")
        else:
            print("CSV file import failed. Please check the file path and format.")

        columns_names_conformation = self.check_status_column_names(imported_file)
        if columns_names_conformation is not None:
            print("Every CSV columns present.")
        else:
            print("CSV file quiality control failed. Please check the columns names, every required column is not present")

        table_without_extra_head= self.check_for_duplicated_titles_among_row(columns_names_conformation)
        if table_without_extra_head is not None:
            print("CSV without title duplcations done.")
        else:
            print("CSV file quiality control failed. Please check the data content, looks like their multiple head rows with title in you CSV.")

        table_with_template_addition = self.add_columns_from_template(columns_names_conformation)

        table_with_value_edited = self.value_edition(table_with_template_addition)

        table_with_time_corrected = self.time_edition(table_with_value_edited)

        table_with_blanks_cleaned = self.clean_empty_rows(table_with_time_corrected)

        table_extra_column_deleted = self.delete_extra_columns(table_with_blanks_cleaned)

        table_with_uniqid = self.unique_id_generation(table_extra_column_deleted)

        if table_with_uniqid is not None:
            print("CSV data transformation done.")
        else:
            print("CSV data transformation failed. Something went wrong during transformation.")

        return table_with_uniqid
      
      
    def yaml_quality_control(self,input_data,configuration):

        imported_file = self.import_your_data_from_csv(input_data)
        if imported_file is not None:
            print("CSV file imported successfully.")
        else:
            print("CSV file import failed. Please check the file path and format.")

        # columns_names_conformation = self.check_status_column_names(imported_file)
        # if columns_names_conformation is not None:
        #     print("Every CSV columns present.")
        # else:
        #     print("CSV file quiality control failed. Please check the columns names, every required column is not present")

        # table_without_extra_head= self.check_for_duplicated_titles_among_row(columns_names_conformation)
        # if table_without_extra_head is not None:
        #     print("CSV without title duplcations done.")
        # else:
        #     print("CSV file quiality control failed. Please check the data content, looks like their multiple head rows with title in you CSV.")

        table_with_template_addition = self.transform_shape_based_on_config(configuration=configuration, data=imported_file)

        table_with_value_edited = self.value_edition(table_with_template_addition)

        table_with_time_corrected = self.time_edition(table_with_value_edited)

        table_with_blanks_cleaned = self.clean_empty_rows(table_with_time_corrected)

        table_extra_column_deleted = self.delete_extra_columns(table_with_blanks_cleaned)

        table_with_uniqid = self.unique_id_generation(table_extra_column_deleted)

        if table_with_uniqid is not None:
            print("CSV data transformation done.")
        else:
            print("CSV data transformation failed. Something went wrong during transformation.")

        return table_with_uniqid
    
   
class Template:

  template_model = dict(

    # Birthyear = dict(
    #   pid = None,
    #   event_id = None,
    #   comments = None,
    #   process_type = "http://purl.obolibrary.org/obo/NCIT_C142470",
    #   output_type = "http://purl.obolibrary.org/obo/NCIT_C70856",
    #   attribute_type = "http://purl.obolibrary.org/obo/NCIT_C83164",
    #   attribute_type2 = None,
    #   agent_id = None,
    #   input_type = None,
    #   target_type = None,
    #   activity_type = None,
    #   intensity_type = None,
    #   unit_type = None,
    #   agent_type = None,
    #   frequency_type = None,
    #   frequency_value = None,
    #   route_type = None,
    #   output_id = None,
    #   value_date = None,
    #   value_integer = None,
    #   value_string = None,
    #   value_float = None,
    #   value_datatype = "xsd:integer",
    #   age = None,
    #   startdate = None,
    #   enddate = None,
    #   uniqid = None,

    # ),

    Birthdate = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C142470",
      output_type = "http://purl.obolibrary.org/obo/NCIT_C70856",
      attribute_type = "http://purl.obolibrary.org/obo/NCIT_C68615",
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:date",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),

    Deathdate = dict( 
      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C142470",
      output_type = "http://purl.obolibrary.org/obo/NCIT_C70856",
      attribute_type = "http://purl.obolibrary.org/obo/NCIT_C70810",
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:date",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),

    First_visit = dict(

      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C142470",
      output_type = "http://purl.obolibrary.org/obo/NCIT_C70856",
      attribute_type = "http://purl.obolibrary.org/obo/NCIT_C164021",
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:date",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),

    Sex = dict( 

      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C142470",
      output_type = "http://purl.obolibrary.org/obo/NCIT_C70856",
      attribute_type = None,
      attribute_type2 = "http://purl.obolibrary.org/obo/NCIT_C28421",
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:string",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),


    Status = dict(

      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C142470",
      output_type = "http://purl.obolibrary.org/obo/NCIT_C70856",
      attribute_type = None,
      attribute_type2 = "http://purl.obolibrary.org/obo/NCIT_C166244",
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:string",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),

    Diagnosis = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C18020",
      output_type = "http://purl.obolibrary.org/obo/NCIT_C70856",
      attribute_type = None,
      attribute_type2 = "http://purl.obolibrary.org/obo/NCIT_C2991",
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:string",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),

    Symptom = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C18020",
      output_type = "http://purl.obolibrary.org/obo/NCIT_C70856",
      attribute_type = None,
      attribute_type2 = "http://purl.obolibrary.org/obo/NCIT_C100104",
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:string",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),

    Symptoms_onset = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type= "http://purl.obolibrary.org/obo/NCIT_C142470",
      output_type = "http://purl.obolibrary.org/obo/NCIT_C70856",
      attribute_type2= "http://purl.obolibrary.org/obo/NCIT_C100104",
      attribute_type= "http://purl.obolibrary.org/obo/NCIT_C124353",
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:date",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),

    Genetic = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type= "http://purl.obolibrary.org/obo/NCIT_C15709",
      output_type= "http://purl.obolibrary.org/obo/NCIT_C45766",
      attribute_type= "http://purl.obolibrary.org/obo/NCIT_C103223",
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = "http://purl.obolibrary.org/obo/NCIT_C16612",
      target_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:string",  
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),

    Consent_contacted = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type= "http://purl.obolibrary.org/obo/OBI_0000810",
      output_type = "http://purl.obolibrary.org/obo/OBIB_0000488",
      attribute_type= "http://purl.obolibrary.org/obo/NCIT_C25460",
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:string",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,



    ),

    Consent_used = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type= "http://purl.obolibrary.org/obo/OBI_0000810",
      output_type = "http://purl.obolibrary.org/obo/DUO_0000001",
      attribute_type= "http://purl.obolibrary.org/obo/NCIT_C25460",
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:string",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),

    Biobank = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type= "http://purl.obolibrary.org/obo/OMIABIS_0000061",
      output_type= "http://purl.obolibrary.org/obo/NCIT_C115570",
      attribute_type= None,
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = "http://purl.obolibrary.org/obo/OBIB_0000616",
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:string",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),

    Questionnaire = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C91102",
      output_type = "http://purl.obolibrary.org/obo/NCIT_C70856",
      attribute_type = "http://purl.obolibrary.org/obo/NCIT_C21007",
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:float",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),

    Body_measurement = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C142470" ,
      output_type = "http://purl.obolibrary.org/obo/NCIT_C70856" ,
      attribute_type = None,
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:float" ,
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),


    Lab_measurement = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C25294" ,
      output_type = "http://purl.obolibrary.org/obo/NCIT_C70856" ,
      attribute_type = None,
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype= "xsd:float" ,
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),


    Imaging = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C17369",
      output_type =  "http://purl.obolibrary.org/obo/NCIT_C81289",
      attribute_type = "http://purl.obolibrary.org/obo/NCIT_C176708",
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:string" ,
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    ),


    Surgery = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C15329",
      output_type = None,
      attribute_type = None,
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:string" ,
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,


    ),


    Clinical_trial = dict(

      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C71104" ,
      output_type=  "http://purl.obolibrary.org/obo/NCIT_C115575" ,
      attribute_type = None,
      attribute_type2 = "http://purl.obolibrary.org/obo/NCIT_C2991",
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = "http://purl.obolibrary.org/obo/NCIT_C16696" ,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:string",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,


    ),

    Medication = dict(
      pid = None,
      event_id = None,
      comments = None,
      process_type = "http://purl.obolibrary.org/obo/NCIT_C70962",
      output_type = None ,
      attribute_type = None,
      attribute_type2 = None,
      agent_id = None,
      substance_id = None,
      input_type = None,
      target_type = None,
      target_id = None,
      output_id = None,
      activity_type = None,
      intensity_type = None,
      unit_type = None,
      agent_type = None,
      frequency_type = None,
      frequency_value = None,
      route_type = None,
      concentration_value = None,
      value_date = None,
      value_integer = None,
      value_string = None,
      value_float = None,
      value_datatype = "xsd:float",
      age = None,
      protocol_id = None,
      startdate = None,
      enddate = None,
      uniqid = None,

    )


  )