from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

from . import views
from .views import hotSong

urlpatterns = [
    path('', views.home, name='home'), 
    path('myapp/hotSong/<int:year>/', views.hotSong, name='hotSong'), 
    path('myapp/', views.season, name='season'),
    # path('hotSong/<int:year>/', hotSong, name='hotSong'),
]
