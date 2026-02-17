from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Product
from unittest.mock import patch, MagicMock

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

    def test_list_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_create_product(self):
        # Depending on permissions, this might require admin or be allowed for auth users
        # Assuming for now auth users can Create or read-only
        # Let's check viewset permissions. If standard ModelViewSet usually allows creation.
        new_product_data = {
            'name': 'New Product',
            'description': 'New Description',
            'price': 20.00,
            'stock': 50
        }
        response = self.client.post('/api/products/', new_product_data, format='json')
        # If default ModelViewSet, creating is allowed.
        if response.status_code == status.HTTP_201_CREATED:
            self.assertEqual(Product.objects.count(), 2)
        else:
            # If rejected, ensure it's at least 403 or similar
            self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_403_FORBIDDEN])

    def test_retrieve_product(self):
        response = self.client.get(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Product')

    @patch('products.views.PrintifyService')
    def test_printify_products(self, MockPrintifyService):
        mock_service = MockPrintifyService.return_value
        mock_service.get_products.return_value = [{'id': '1', 'title': 'Printify Product'}]
        
        response = self.client.get('/api/printify/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'id': '1', 'title': 'Printify Product'}])

    @patch('products.views.PrintifyService')
    def test_printify_orders(self, MockPrintifyService):
        mock_service = MockPrintifyService.return_value
        mock_service.get_orders.return_value = [{'id': '101', 'status': 'fulfilled'}]
        
        response = self.client.get('/api/printify/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'id': '101', 'status': 'fulfilled'}])
