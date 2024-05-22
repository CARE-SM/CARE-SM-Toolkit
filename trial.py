import pandas as pd
import yaml

from toolkit.main import Toolkit

with open("toolkit/exemplar_data/CAREconfig.yaml") as file:
    configuration = yaml.load(file, Loader=yaml.FullLoader)

# test= Toolkit()

# test_done = test.yaml_quality_control(input_data="toolkit/exemplar_data/yaml_preCARE.csv",configuration=configuration)
# test_done.to_csv ("toolkit/exemplar_data/yaml_CARE_TEST.csv", index = False, header=True)

test_fiab= Toolkit()

test_done_fiab = test_fiab.whole_quality_control(input_data="toolkit/exemplar_data/preCARE.csv")
test_done_fiab.to_csv ("toolkit/exemplar_data/CARE.csv", index = False, header=True)