import requests
import json

url = "http://10.106.74.234:6080/esa/api/v2.0/config/dictionaries/TheNetworkVikingAhsan?device_type=esa"

payload = json.dumps({
  "data": {
    "ignorecase": 0,
    "wholewords": 1,
    "words": [
      [
        "*credit",
        2,
        "prefix"
      ],
      [
        "*aba"
      ],
      [
        "YouTube Channel"
      ]
    ],
    "encoding": "utf-8"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46S2hXXXXXXXXXXXXXXX'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#Video Tutorial for this program: 
#https://www.youtube.com/watch?v=LHranoFP2AE&t=162s