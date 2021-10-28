import requests
import json

url = "https://api-qa.knightsbridge.live/api/users/signin"
payload = json.dumps({
    "email": "sompod123@gmail.com",
    "password": "@ndsfGjJdf4325sg"
})
headers = {'Content-Type': 'application/json'}
response = requests.request("POST", url, headers=headers, data=payload)
body = response.json()
print(body)
token = body['token']
