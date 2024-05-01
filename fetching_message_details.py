import requests
import json
import pprint

print("Fetch message details by providing following 3 parameters:\n")

mid = input("MID: ")
icid = input("ICID: ")
serial = input("Serail Number of the ESA: ")

url = "http://10.106.36.175:6080/esa/api/v2.0/message-tracking/details?endDate=2021-11-16T12:09:00.000Z&icid="+icid+"&mid="+mid+"&serialNumber="+serial+"&startDate=2018-11-16T00:00:00.000Z"

payload={}
headers = {
  'Authorization': 'Basic YWRtaW4xxxxxxxxxxxxxxxxxxxxxxxxxxx',
  'Cookie': 'ahsanabbas'
}

response = requests.request("GET", url, headers=headers, data=payload, verify="False")

json_string = json.loads(response.content)

#pprint.pprint(response.text)

pprint.pprint("Message Status: " + json_string['data']['messages']['messageStatus'])
pprint.pprint("Sender Group:  "  + json_string['data']['messages']['senderGroup'])
pprint.pprint("Sender: "         + json_string['data']['messages']['sender'])
pprint.pprint("Hostname: "       + json_string['data']['messages']['hostName'])
pprint.pprint("Subject: "        + json_string['data']['messages']['subject'])



