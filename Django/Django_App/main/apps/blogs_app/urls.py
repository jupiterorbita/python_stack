from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<number>[0-9]{2})$', views.show),
    url(r'^(?P<number2>[0-9]{2})/edit$', views.edit),
    url(r'^(?P<number>[0-9]{2})/delete$', views.destroy)
]