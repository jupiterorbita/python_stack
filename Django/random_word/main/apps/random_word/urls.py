from django.conf.urls import url
from . import views

print('=== inside urls.py APP ===')
urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_word/$', views.index),
    url(r'^random_word/reset$', views.reset),
    url(r'^reset$', views.reset)
]