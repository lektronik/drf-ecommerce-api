# cart/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer
from django.contrib.auth.models import User

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

class ConvertCartToOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        cart = Cart.objects.get(user=user)
        if not cart.items.exists():
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

        order_data = {
            'user': user.id,
            'total_price': sum(item.product.price * item.quantity for item in cart.items.all()),
            'status': 'Pending'
        }
        order_serializer = OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            order = order_serializer.save()
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    total_price=item.product.price * item.quantity
                )
            cart.items.all().delete()
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
