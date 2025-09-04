from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.contact_page_view, name='contacts'),
]
