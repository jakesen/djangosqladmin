from django.test import TestCase, Client

class DatabaseTests(TestCase):

    def setUp(self):
        self.client = Client()
        
    def test_dashboard(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
