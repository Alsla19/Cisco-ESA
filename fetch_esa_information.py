import requests
import json
import pprint
url = "http://10.106.36.175:6080/esa/api/v2.0/config/appliances?device_type=esa"

payload={}
headers = {
  'Authorization': 'Basic YWRtaW46S2xxxxxxxxxxxxxxxxxxxxxx',
  'Cookie': 'thenetworkviking'
}

response = requests.request("GET", url, headers=headers, data=payload, verify="False")

json_string = json.loads(response.content)

pprint.pprint(json_string)
