import requests

import time
import json

from utils import get_random_browser

"""
Request URL
https://www.toutiao.com/api/pc/feed/?
max_behot_time=1581261896&
category=__all__&
utm_source=toutiao&
widen=1&
tadrequire=true&
as=A1F5BEA431B0404&
cp=5E41E05470848E1&
_signature=S4u4tAAgEBq5pIrzX1qh60uLuKAABXM

https://www.toutiao.com/api/pc/feed/?
max_behot_time=1581257918&
category=__all__&
utm_source=toutiao&
widen=1&
tadrequire=true&
as=A1F5DEB41106502&
cp=5E41B6359082FE1&
_signature=S4u4tAAgEBq5pIrzX1qTX0uLuKAABXM
"""

def get_request_url_and_headers():
    user_agent = get_random_browser()

    current_time = int(time.time())

    headers = {
        "user-agent": user_agent
    }

    base_url =

    proxies = {}

    return base_url,headers, proxies

def get_response_html():
    request_url, headers, proxies = get_request_url_and_headers()
    response = requests.get(request_url, headers=headers, proxies=proxies)

    global response_json
    response_json = json.load(response.text)

    print(response_json)
    if response_json["message"] == "error"
        get_response_html()

    return response_json

def data_to_file():
    data = response_json["data"]

    for i in range(len(data)):
        data_dict = data[i]

        with open("toutiao.json","a+") as f:
            json.dump(data_dict,f,ensure_ascii=False)
            f.write("\n")

json_content = get_response_html()
print(json_content)

data_to_file()

import pandas as pd

df = pd.read_json("toutiao.json",lines=True)
print(df)

df.to_excel("toutiao.xlsx")