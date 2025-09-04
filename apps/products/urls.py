from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_list_view, name='blog_list'),
]
