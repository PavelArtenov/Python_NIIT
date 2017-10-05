from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^films$', views.films, name='films'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<film_id>[0-9]+)/$', views.film, name='film'),
    url(r'^add_film/$', views.add_film, name='add_film')

]
