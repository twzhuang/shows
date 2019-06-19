from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.display_add_show),
    url(r'^addshow$', views.addshow),
    url(r'^shows/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^shows/edit/(?P<id>\d+)$', views.edit),
    url(r'^shows/update/(?P<id>\d+)$', views.update),
    url(r'^shows/(?P<id>\d+)$', views.show)
]
