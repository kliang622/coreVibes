from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf import settings
from django.conf.urls.static import static
# from myapp.views import MarkersMapView

# from .views import local_geojson

from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    # path('myapp/', views.season, name='season'),
    path('myapp/season', views.season, name='season'), 
    path('myapp/world', views.world, name='world'),
    # path('myapp/search_region', search_region, name='search_region'),
    # path('map/', views.map_view, name='map_view'), 
    path('myapp/search', views.search_artist, name='search_artist'),
    path('myapp/timeline', views.timelineView, name ='timelineView'), 
    # path("map/", MarkersMapView.as_view())
    # path('local_geojson/', views.local_geojson, name='local_geojson'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)