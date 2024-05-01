import requests
import json
import pprint
url = "http://10.106.36.175:6080/esa/api/v2.0/health"

payload={}
headers = {
  'Authorization': 'Basic YWRtaW46xxxxxxxxxxxxxxxxxxxxxxx',
  'Cookie': 'ahsanabbas'
}

response = requests.request("GET", url, headers=headers, data=payload, verify="False")

json_string = json.loads(response.content)

pprint.pprint(json_string)
