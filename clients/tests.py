from django.test import TestCase
from django.urls import reverse

from .models import Client
from django.test import Client as TClient


# Create your tests here.


class TestEmails(TestCase):

    def setUp(self):
        client = Client()
        client.email = "juliocsreis@gmail.com"
        client.name = "Teste Usuário"
        client.phone = "+5515997592161"
        client.msg = "teste menssagem para ver orçamento e outras funcçoes de teste" \
                     " nananananna"
        self.client = client

    def test_form_contact_api(self):
        c = TClient()
        data = {"name": self.client.name, "email": self.client.email, "phone": self.client.phone,
                "msg": self.client.msg}
        response = c.post(reverse('clients_api:client_contact'), data=data)
        print("test_form_contact_api response: ", response)
        self.assertEqual(response.status_code, 201)
