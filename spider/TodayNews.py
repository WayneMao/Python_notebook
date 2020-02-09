import numpy as np
import json
import requests
import random

def write_browser_info_to_file():
    my_user_agent = requests.get()

    with open("browser_info.json","w") as f:
        json.dump(my_user_agent.text,f)

write_browser_info_to_file()

def 
