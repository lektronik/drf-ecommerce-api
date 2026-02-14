from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .services import PrintifyService

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


from django.conf import settings

class PrintifyProductListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        service = PrintifyService(api_key=settings.PRINTIFY_API_KEY, shop_id=settings.PRINTIFY_SHOP_ID)
        try:
            products = service.get_products()
            return Response(products, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PrintifyOrderListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        service = PrintifyService(api_key=settings.PRINTIFY_API_KEY, shop_id=settings.PRINTIFY_SHOP_ID)
        try:
            orders = service.get_orders()
            return Response(orders, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PrintifyOrderDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, order_id):
        service = PrintifyService(api_key=settings.PRINTIFY_API_KEY, shop_id=settings.PRINTIFY_SHOP_ID)
        try:
            order = service.get_order(order_id)
            return Response(order, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, order_id):
        service = PrintifyService(api_key=settings.PRINTIFY_API_KEY, shop_id=settings.PRINTIFY_SHOP_ID)
        try:
            updated_order = service.update_order(order_id, request.data)
            return Response(updated_order, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
