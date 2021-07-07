from django.test import TestCase
from rest_framework.test import APIClient

client = APIClient()

# Create your tests here.
class YourTestClass(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_get_invoice(self):
        response = client.get('/invoices/')
        print(response)
