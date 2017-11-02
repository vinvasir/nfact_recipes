from django.conf.urls import url

from . import views
from rest_framework.authtoken import views as tokenauth_views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^allrecipes/(?P<slug>[\w-]+)/$', views.allrecipes),
  url(r'^bbcgoodfood/(?P<slug>[\w-]+)/$', views.bbcgoodfood),
  url(r'^twopeasandtheirpod/(?P<slug>[\w-]+)/$', views.twopeasandtheirpod)
]