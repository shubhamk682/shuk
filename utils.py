#helper functions

#modules will be writing over here

from xml.etree import ElementTree as ET
import re
import random
import yaml

def process_data(f_in,target_tag,f_out_train,f_out_test,split=0.2):
    try:
        root=ET.fromstring(f_in)
        for child in root:
            pid=child.get("ID","")
            label=1 if target_tag in child.get("Tags","") else 0
            title=re.sub(r"\s"," ",child.get("Title","")).strip()
            body=re.sub(r"\s"," ",child.get("Body","")).strip()
            combined_text=title+" "+body
            f_out=f_out_train if random.random() > split else f_out_test
            f_out.write(f"{pid}\t{label}\t{combined_text}\n")
    except Exception as e:
        raise e
    
def read_yaml(config_path):
    try:
        with open(config_path,"r") as data:
            config_data=yaml.safe_load(data)
        return config_data
    except Exception as e:
        raise e
