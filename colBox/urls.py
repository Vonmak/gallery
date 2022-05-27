from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name='index'),
    path('show', views.show, name='show'),
    path('search/', views.search_results, name='searchResults'),
    re_path('^location/(?P<locale>\w+)/', views.location, name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)