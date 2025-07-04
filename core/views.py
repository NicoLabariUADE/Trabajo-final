from django.shortcuts import render
from pages.models import Page

def home(request):
    latest_pages = Page.objects.order_by('-created_at')[:5]
    return render(request, 'core/home.html', {'latest_pages': latest_pages})

def about(request):
    return render(request, 'core/about.html')
