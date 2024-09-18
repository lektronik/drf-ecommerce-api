from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect

def redirect_to_api(request):
    return redirect('/api/')

def api_root(request):
    return JsonResponse({
        'message': 'Welcome to the API',
        'endpoints': {
            'products': request.build_absolute_uri(reverse('printify-products')),
            'orders': request.build_absolute_uri(reverse('printify-orders')),
            'order_detail': request.build_absolute_uri(reverse('printify-order-detail', kwargs={'order_id': 1})),  # Example order_id
            'auth': request.build_absolute_uri(reverse('rest_framework:login')),
            'auth_registration': request.build_absolute_uri(reverse('rest_register')),
            'cart': request.build_absolute_uri(reverse('cart-list')),
        }
    })
