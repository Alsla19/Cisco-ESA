import requests
import json
import pprint
url = "http://10.106.36.175:6080/esa/api/v2.0/message-tracking/connection-details?endDate=2021-11-16T11:25:00.000Z&icid=78&mid=47&serialNumber=420B2473585CCD1F6F6B-A135E077FA2A&startDate=2018-11-09T00:00:00.000Z"

print("*****You have to provide the MID, ICID and the serial number for this program as well! I have hard coded it******\n\n")

payload={}
headers = {
  'Authorization': 'Basic YWRtaW46xxxxxxxxxxxxxxxxxx',
  'Cookie': 'ahsanabbas'
}

response = requests.request("GET", url, headers=headers, data=payload, verify="False")

json_string = json.loads(response.content)

pprint.pprint(json_string['messages']['summary'][0])
print("\n\n")
pprint.pprint(json_string['messages']['summary'][1])




