import requests
import pandas as pd
import json
from pprint import pprint

response = requests.get(
    'http://biclinic.site/vk/statistics?user_id=8&type_info=campaign&demo_id=1010743906%2C1010950323%2C1012600663&period=month&date_from=0&date_to=0&status=period')
a = {"response":[]}

q = response.json()
for i in q['response']:
    for j in i['stats']:
        j['id'] = i['id']
        print(j)



for i in q["response"]:
    a["response"].extend(i["stats"])
result = pd.DataFrame.from_dict(a["response"])
print(result)