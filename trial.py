from toolkit.main import Toolkit

toolkit_snomed = Toolkit()
toolkit_snomed.whole_method(folder_path="toolkit/data/snomed/", template_type="SNOMED") ## SNOMED or OBO

toolkit_obo = Toolkit()
toolkit_obo.whole_method(folder_path="toolkit/data/obo/", template_type="OBO") ## SNOMED or OBO