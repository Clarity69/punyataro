from django.shortcuts import render

# Create your views here.
from .models import Artikel

def blog_index(request):
    post = Artikel.objects.all()
    context = {
        'post' : post
    }
    return render(request, 'index.html', context)