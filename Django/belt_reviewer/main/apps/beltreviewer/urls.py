from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^books$', views.books),
    url(r'^add_book$', views.add_book),
    url(r'^add_book_review', views.add_book_review),
    url(r'^add_book_method$', views.add_book_method),
    url(r'^book_review/(?P<id>\d+)$', views.book_review),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^logout$', views.logout)
]