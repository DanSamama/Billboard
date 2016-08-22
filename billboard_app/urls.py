from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from . import views


app_name = 'billboard_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^billboard_app/new_msg', views.new_msg, name='new_msg'),
    url(r'^register/$', views.register, name='register'),
    # url(r'^home/$', views.index, {'next_page': '/billboard_app'}),

]
