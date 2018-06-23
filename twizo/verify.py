import requests
import json
from requests.auth import HTTPBasicAuth

TWIZO_TEST_API_KEY = 'OVSXDvByaLF9GxXebEUHelIxY7IemJwRyn6iPzEqZA5SRZvI'
TWIZO_REAL_API_KEY = 'VkuCjRhaiZAoiDZ2yCJ6HGdS9o6dOkI9cbnArfV7jl6j2nQT'
URL = 'https://api-asia-01.twizo.com/v1/verification/submit'
phone_number = "6598553351"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=utf8"
}
auth = HTTPBasicAuth('twizo', TWIZO_TEST_API_KEY)
payload = {
    "recipient": phone_number,
    "type": "sms",
    "sender": "PearShape",
    "bodyTemplate": "Your verification code is %token%"
}

r = requests.post(URL, headers=headers, auth=auth, data=json.dumps(payload))
messageId = json.loads(r.text)["messageId"]
print(messageId)

URL2 = "https://api-asia-01.twizo.com/v1/verification/submit/"+messageId

r2 = requests.get(URL2, headers=headers, auth=auth)
print(r2.text)