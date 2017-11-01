from django.conf.urls import url

from . import views
from rest_framework.authtoken import views as tokenauth_views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^token-auth/$', tokenauth_views.obtain_auth_token),
  url(r'^allrecipes/(?P<slug>[\w-]+)/$', views.allrecipes),
]