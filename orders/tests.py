from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Order, OrderItem
from products.models import Product

class OrderTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(name='Test Product', price=10.00, stock=10)
        self.order_data = {
            'user': self.user.id,
            'total_price': 20.00,
            'status': 'Pending'
        }

    def test_create_order(self):
        response = self.client.post('/api/orders/', self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().status, 'Pending')

    def test_unauthenticated_order(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/orders/', self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_orders(self):
        Order.objects.create(user=self.user, total_price=10.00, status='Pending')
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_order_status(self):
        order = Order.objects.create(user=self.user, total_price=10.00, status='Pending')
        response = self.client.patch(f'/api/orders/{order.id}/', {'status': 'Completed'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.get(id=order.id).status, 'Completed')

    def test_delete_order(self):
        order = Order.objects.create(user=self.user, total_price=10.00, status='Pending')
        response = self.client.delete(f'/api/orders/{order.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)
