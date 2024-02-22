import pandas as pd
import yaml

from toolkit.main import Toolkit

with open("toolkit/exemplar_data/CAREconfig_testbed.yaml") as file:
    configuration = yaml.load(file, Loader=yaml.FullLoader)
    
test= Toolkit()

test_done = test.yaml_quality_control(input_data="toolkit/exemplar_data/yaml_preCARE_testbed.csv",configuration=configuration)
test_done.to_csv ("toolkit/exemplar_data/yaml_CARE_testbed.csv", index = False, header=True)


test_faib= Toolkit()

test_done_fiab = test_faib.whole_quality_control(input_data="toolkit/exemplar_data/preCARE.csv")
test_done_fiab.to_csv ("toolkit/exemplar_data/CARE.csv", index = False, header=True)