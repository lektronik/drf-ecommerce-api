# cart/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet, ConvertCartToOrderView

router = DefaultRouter()
router.register(r'cart', CartViewSet)
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('convert-cart-to-order/', ConvertCartToOrderView.as_view(), name='convert-cart-to-order'),
]
