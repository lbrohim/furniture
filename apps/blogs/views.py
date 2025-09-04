from django.shortcuts import render

from django.http import HttpResponse

def blog_list(request):
    return render(request, 'blogs/blog_list.html')

# Create your views here.
