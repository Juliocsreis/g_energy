from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import AllowAny
from clients.models import Client
from clients.emails import email_to_client_contact_form, email_to_admin_client_contact_form
import os
import requests
from ipware import get_client_ip
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import time
import hashlib

PIXEL_ID = "519816429359831"
TOKEN = os.environ.get("facebook_api_conversion")
fb_url = "https://graph.facebook.com/v10.0/" + PIXEL_ID + "/events?access_token=" + TOKEN


def send_facebook_conversion(event_name, event_source_url, **kwargs):
    myData = {"data": [
        {
            "event_name": event_name,
            "event_time": int(time.time()),
            "action_source": "website",
            "event_source_url": event_source_url,
            "user_data": {
                # "em": "7b17fb0bd173f625b58636fb796407c22b3d16fc78302d79f0fd30c2fc2fc068",
                # "client_user_agent": null
            },
            "custom_data": {
                "currency": "BRL",
                "value": "0.0"
            }
        }
    ],
        # "test_event_code": "TEST45270"
    }
    user_data = kwargs.get("user_data")
    if user_data:
        for key in user_data:
            myData["data"][0]["user_data"][key] = user_data[key]
    # if kwargs:
    #     for key in kwargs:
    #         if key != "user_data":
    #             myData["data"][0][key] = kwargs[key]

    post = requests.post(fb_url, json=myData)
    return post


def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

@api_view(['POST'])
@permission_classes([AllowAny])
def client_contact(request):
    if request.method == "POST":
        name = request.data.get('name', None)
        email = request.data.get('email', None)
        phone = request.data.get('phone', None)
        msg = request.data.get('msg', None)
        lead_origin = request.data.get('origin', None)
        client = Client()
        client.name = name.strip()
        client.email = email.strip()
        client.phone = phone
        client.msg = msg
        client.lead_origin = lead_origin
        client.created = timezone.now()
        if client.email and client.msg:
            client_ip, is_routable = get_client_ip(request)
            user_data = {"client_ip_address": client_ip, "client_user_agent": request.META['HTTP_USER_AGENT'],
                         "fn": encrypt_string(name.split(' ', 1)[0]), "ln": encrypt_string(name.split(' ', 1)[-1]),
                         "ph": encrypt_string(phone), "email": encrypt_string(email)}

            full_path = request.build_absolute_uri()
            send_facebook_conversion("Contact", full_path, user_data=user_data)
            client.save()
            email_to_client_contact_form(client)
            email_to_admin_client_contact_form(client)
        return Response({'response': 'ok'}, status=status.HTTP_201_CREATED)



