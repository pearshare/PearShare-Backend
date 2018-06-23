from django.http import JsonResponse
import requests
import json
from requests.auth import HTTPBasicAuth
from django.contrib.auth.models import User
from .models import Message

# Create your views here.
TWIZO_TEST_API_KEY = 'ZxPqBHSjoJiqkBHnJng7v0A6NPR0z6Uh-HlryfH_uD93S2Id'
TWIZO_REAL_API_KEY = 'FWPBuRPbcZ0HhOqT0OauK-KNfb1x4IRw8SaprZLsyUzL-qpP'

def get_message_id(request, user_id):
    return JsonResponse({"messageId": User.objects.get(id=user_id).message_set.latest().messageID })

def request_payment_and_send_conf(request, user_id):
    phone_num = "6598553351"
    api_url= "https://api-asia-01.twizo.com/verification/submit"
    headers= {"Accept" : "application/json", "Content-Type": "application/json; charset=utf8"}
    auth = HTTPBasicAuth('twizo', TWIZO_TEST_API_KEY)
    
    payload = {
        "recipient": phone_num,
        "type": "sms",
        "sender": "PearShape",
        "bodyTemplate": "Please enter this verification code %token% to verify successfully delivery"
    }
    r = requests.post(api_url, auth=auth, headers=headers, data=json.dumps(payload))

    messageID = json.loads(r.text)["messageId"]
    queryset = Message.objects.create(messageID=messageID, user=User.objects.get(id=user_id))

    return JsonResponse({"messageID": messageID})

def confirm_token(request, messageID, token):
    api_url= "https://api-asia-01.twizo.com/verification/submit/"+ messageID + "?token="+token

    headers= {"Accept" : "application/json", "Content-Type": "application/json; charset=utf8"}
    auth = HTTPBasicAuth('twizo', TWIZO_TEST_API_KEY)
    
    payload = {
        "messageId": messageId, 
        "token": token
    }
    r = requests.get(api_url, auth= auth, headers=headers, data=payload)
    output = json.loads(r.text)["status"]
    #use user token entered and messageId to request on twizo api
    if output == "success":
        return JsonResponse({"message": "success"})
    else:
        return JsonResponse({"message": "failure"})