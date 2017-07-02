# URLConf for the paperplaces.tms application.
from django.conf.urls import url
from paperplaces.tms import views

urlpatterns = [
	url(r'^$',views.root), # "/tms" calls root()
	url(r'^(?P<version>[0-9.]+)$',views.service), # eg, "/tms/1.0" calls service(version="1.0")
	url(r'^(?P<version>[0-9.]+)/' +r'(?P<shapefile_id>\d+)$',views.tileMap), # eg, "/tms/1.0/2" calls# tileMap(version="1.0", shapefile_id=2)
	url(r'^(?P<version>[0-9.]+)/' +r'(?P<shapefile_id>\d+)/(?P<zoom>\d+)/' +r'(?P<x>\d+)/(?P<y>\d+)\.png$',views.tile), # eg, "/tms/1.0/2/3/4/5" calls tile(version="1.0", shapefile_id=2, zoom=3, x=4,y=5)
]