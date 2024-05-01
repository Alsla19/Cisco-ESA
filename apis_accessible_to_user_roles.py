import requests
import json
import pprint
url = "http://10.106.36.175:6080/esa/api/v2.0/login/privileges"

payload={}
headers = {
  'Authorization': 'Basic YWRtaW46Sxxxxxxxxxxxxxxxxxxx',
  'Cookie': 'thenetworkviking'
}

response = requests.request("GET", url, headers=headers, data=payload, verify="False")

json_string = json.loads(response.content)

pprint.pprint(json_string)
