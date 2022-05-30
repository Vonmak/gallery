from django.shortcuts import render
from .models import Image, Category, Location
import datetime as dt

# Create your views here.
def index(request):
    locations = Location.get_all()
    return render(request, 'index.html',{'locations':locations})

def home(request):
    images =Image.get_latest()
    locations = Location.get_all()
    return render(request, 'home.html',{'images':images, 'locations':locations})

def show(request):
    images = Image.get_images()
    return render(request, 'show.html', {'images': images})


def search_results(request):
    title=Category.name
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_images(search_term)
        message = f"{search_term}"
        # print(searched_images)
        return render(request, 'search.html',{"message":message,"searched_images": searched_images,'title':title})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def location(request,locale):
    images = Image.filter_by_location(locale)
    return render(request, 'location.html', {'images':images})