from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="my_home" ),
    url(r'^addtravel$', views.addtravel, name="add_travel" ),
    url(r'^addtravel/add$', views.add, name="add" ),
    url(r'^addtomytravel/(?P<id>\d+)$', views.myaddtravel, name="my_added_travel"),
    url(r'^travels/destination/(?P<id>\d+)$', views.destination, name="my_destination"),
    url(r'^logout$', views.logout, name="logout" ),
]
