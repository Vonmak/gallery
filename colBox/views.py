from django.shortcuts import render
from .models import Image, Category
import datetime as dt

# Create your views here.
def index(request):
    images =Image.get_latest()
    return render(request, 'index.html',{'images':images})

def show(request):
    images = Image.get_images()
    return render(request, 'show.html', {'images': images})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_images(search_term)
        message = f"{search_term}"
        # print(searched_images)
        return render(request, 'search.html',{"message":message,"searched_images": searched_images,})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    