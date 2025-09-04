from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_page_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})


def home_page_view(request):
    return render(request, 'pages/home3.html')

# Create your views here.
