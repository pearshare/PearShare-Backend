from django.shortcuts import render

# Create your views here.
TWIZO_TEST_API_KEY = 'OVSXDvByaLF9GxXebEUHelIxY7IemJwRyn6iPzEqZA5SRZvI'

def request_payment_and_send_conf():
    find user's phone number # this is just hardcoded 98553351
    make req to twizo api
    wait for it to send
    store messageId into db and attach to users. find user by username given in the request

def confirm_token
    use user token entered and messageId to request on twizo api
    if it is right
        return success!
    else
        return wrong token 