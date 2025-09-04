from django.shortcuts import render

def products_list_view(request):
    return render(request, 'products/product-cart.html')

# Create your views here.
