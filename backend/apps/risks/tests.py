import json
from http import HTTPStatus

from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory

from apps.risks.views import RiskTypeViewSet


class RiskTypeViewSetTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = Client()

    def test_get_all_risk_types(self):
        request = self.factory.get('/api/risks/')
        response = RiskTypeViewSet.as_view({'get': 'list'})(request)

        self.assertEqual(json.loads(response.content)['1']['name'], 'general')
        self.assertGreater(len(json.loads(response.content)), 1)
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_get_risk_types_by_id(self):
        response = self.client.get('/api/risks/1/', kwargs={'pk': 1})

        self.assertEqual(json.loads(response.content)['1']['name'], 'general')
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_get_risk_types_should_not_found(self):
        response = self.client.get('/api/risks/99/', kwargs={'pk': 99})

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND._value_)

    def test_post_should_method_not_allowed(self):
        response = self.client.post('/api/risks/1/', kwargs={'pk': 1})

        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED._value_)
