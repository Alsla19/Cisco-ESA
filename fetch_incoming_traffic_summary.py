import requests
import json
import pprint
url = "http://10.106.36.175:6080/esa/api/v2.0/reporting/mail_incoming_traffic_summary?startDate=2021-08-10T19:00:00.000Z&endDate=2021-09-24T23:00:00.000Z&device_type=esa"

payload={}
headers = {
  'Authorization': 'Basic YWRtaW46Sxxxxxxxxxxxxxxxxxxxxxx',
  'Cookie': 'ahsanabbas'
}

response = requests.request("GET", url, headers=headers, data=payload, verify="False")

json_string = json.loads(response.content)

pprint.pprint(json_string)

