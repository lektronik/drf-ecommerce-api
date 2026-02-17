from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from products.models import Product
from .models import Cart, CartItem
from orders.models import Order

class CartTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(name='Test Product', price=10.00, stock=10)
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_model(self):
        self.assertEqual(self.cart.user.username, 'testuser')

    def test_cart_item_model(self):
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)
        self.assertEqual(cart_item.product.name, 'Test Product')
        self.assertEqual(cart_item.quantity, 2)

    def test_add_item_to_cart(self):
        data = {
            'cart': self.cart.id,
            'product': self.product.id,
            'quantity': 1
        }
        response = self.client.post('/api/cart/cart-items/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(CartItem.objects.get().product.name, 'Test Product')

    def test_convert_cart_to_order(self):
        # Add item to cart
        CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)
        
        # Convert to order
        response = self.client.post('/api/cart/convert-cart-to-order/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verify order created
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().total_price, 20.00)
        
        # Verify cart emptied
        self.assertEqual(CartItem.objects.count(), 0)

    def test_convert_empty_cart_error(self):
        # Ensure cart is empty
        self.cart.items.all().delete()
        
        response = self.client.post('/api/cart/convert-cart-to-order/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
