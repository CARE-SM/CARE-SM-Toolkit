import pandas as pd
import yaml

from toolkit.main import Toolkit

with open("toolkit/exemplar_data/CAREconfig_testbed.yaml") as file:
    configuration = yaml.load(file, Loader=yaml.FullLoader)
    
# test= Toolkit()

# test_done = test.whole_quality_control(input_data="toolkit/exemplar_data/preCARE_NEW.csv",configuration=configuration)
# test_done.to_csv ("toolkit/exemplar_data/CARE_NEW.csv", index = False, header=True)


test= Toolkit()

test_done_fiab = test.whole_quality_control(input_data="toolkit/exemplar_data/preCARE_NEW.csv")
test_done_fiab.to_csv ("toolkit/exemplar_data/CARE_NEW.csv", index = False, header=True)