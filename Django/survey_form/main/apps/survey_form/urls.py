from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^result$', views.result),
    url(r'^survey_form/process$', views.process),
    # url(r'^process$', views.process),
    url(r'^reset$', views.reset)
]
