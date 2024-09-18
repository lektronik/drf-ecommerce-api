from django.urls import path
from .views import PrintifyProductListView, PrintifyOrderListView, PrintifyOrderDetailView

urlpatterns = [
    path('printify/products/', PrintifyProductListView.as_view(), name='printify-products'),
    path('printify/orders/', PrintifyOrderListView.as_view(), name='printify-orders'),
    path('printify/orders/<int:order_id>/', PrintifyOrderDetailView.as_view(), name='printify-order-detail'),
]
