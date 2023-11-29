from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import map_view, get_countries

from . import views
urlpatterns = [
    path('', views.home, name='home')
]
