import json
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class ContactTestCase(TestCase):
    fixtures = [
        'user',
        'contact', 'label',
        'contactemail', 'contactphonenumber', 'contactaddress',
        'contactimportantdate', 'contactwebsite'
    ]

    def setUp(self):
        self.client = APIClient()

    def make_header(self):
        header = {}
        user_id = 1
        user = User.objects.get(id=user_id)
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        header['Authorization'] = f'Bearer {refresh.access_token}'
        header['accept'] = 'application/json'
        return header

    def test_login(self):
        response = self.client.post(
            '/rest-auth/login/',
            json.dumps({
                'username': 'normaluser', 'email': 'normal@example.com', 'password': 'votmdnjem'}),
            content_type='application/json')
        self.assertEquals(response.status_code, 200)
        result = response.json()
        for key in ['access', 'refresh', 'user']:
            self.assertIn(key, result)

    def test_contact_list(self):
        header = self.make_header()
        response = self.client.get('/v1/contact/contact/', **header)
        self.assertEquals(response.status_code, 200)
        result = response.json()
        for key in ['id', 'profile_photo', 'name', 'emails', 'phone_numbers',
                    'company_name', 'company_position']:
            self.assertIn(key, result['results'][0].keys())

    def test_contact_list_ordering_name(self):
        header = self.make_header()
        response = self.client.get('/v1/contact/contact/?ordering=name', **header)
        self.assertEquals(response.status_code, 200)
        result = response.json()
        ordered_name_list = [
            'Alex.Ferguson', 'Bentancur.Rodrigo', 'Cristiano.Ronaldo',
            'Didier.Drogba', 'Eden.Azar', 'Heungmin Son']
        name_list = [data['name'] for data in result['results']]
        self.assertEquals(name_list, ordered_name_list)

    def test_contact_list_ordering_name_desc(self):
        header = self.make_header()
        response = self.client.get('/v1/contact/contact/?ordering=-name', **header)
        self.assertEquals(response.status_code, 200)
        result = response.json()
        ordered_name_list = [
            'Heungmin Son', 'Eden.Azar', 'Didier.Drogba', 'Cristiano.Ronaldo',
            'Bentancur.Rodrigo', 'Alex.Ferguson']
        name_list = [data['name'] for data in result['results']]
        self.assertEquals(name_list, ordered_name_list)

    def test_contact_detail(self):
        header = self.make_header()
        response = self.client.get('/v1/contact/contact/1/', **header)
        self.assertEquals(response.status_code, 200)
        result = response.json()
        for key in ['id', 'profile_photo', 'name', 'emails', 'phone_numbers',
                    'company_name', 'company_position', 'memo', 'addresses',
                    'important_dates', 'websites']:
            self.assertIn(key, result.keys())

    def test_contact_create(self):
        header = self.make_header()
        response = self.client.post(
            '/v1/contact/contact/',
            json.dumps({
                "profile_photo": "https://avatars.githubusercontent.com/u/7259599?v=4",
                "name": "Iniesta andres",
                "emails": [{
                    "email": "iniesta@example.com",
                    "label": "Personal"
                }],
                "phone_numbers": [{
                    "phone_number": "010-3333-4444",
                    "label": "Personal"
                }],
                "company_name": "Barcelona",
                "company_position": "SoccerDoSah",
                "memo": "",
                "addresses": [{
                    "address": "spain",
                    "label": "Home"
                }],
                "important_dates": [{
                    "important_date": "2024-08-09",
                    "label": "Birthday"
                }],
                "websites": [{
                    "website": "https://avatars.githubusercontent.com/u/7259599?v=4",
                    "label": "Homepage"
                }]
            }),
            content_type='application/json',
            **header)
        self.assertEquals(response.status_code, 201)
