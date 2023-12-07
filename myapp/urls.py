from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    # path('myapp/', views.season, name='season'),
    path('myapp/season', views.season, name='season'), 
    path('myapp/world', views.world, name='world'),
    path('myapp/search', views.search_artist, name='search_artist'),
    path('myapp/timeline', views.timelineView, name ='timelineView')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)