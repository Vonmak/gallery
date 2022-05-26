from django.shortcuts import render
from .models import Image, Location, Category
import datetime as dt

# Create your views here.
def index(request):
    # images=Image.today_images()
    images =Image.get_latest()
    return render(request, 'index.html',{'images':images})

def show(request):
    images = Image.get_images()
    return render(request, 'show.html', {'images': images})
