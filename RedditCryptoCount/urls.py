from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.latest_count, name='latest_count'),
    url(r'^update_coin_list/$', views.update_coin_list, name='update_coin_list'),
]