from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Product

from unittest.mock import patch

class ProductTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.product_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 10.00,
            'stock': 100
        }
        self.product = Product.objects.create(**self.product_data)

    @patch('products.views.PrintifyService')
    def test_list_products(self, MockPrintifyService):
        # Mock the service instance and its method
        mock_service_instance = MockPrintifyService.return_value
        mock_service_instance.get_products.return_value = [{'id': '1', 'title': 'Mock Product'}]

        response = self.client.get('/api/printify/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'id': '1', 'title': 'Mock Product'}])

    def test_create_product(self):
        # Assuming there is a local product creation endpoint, otherwise testing the model
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Test Product')
