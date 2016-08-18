from django.conf.urls import url
from . import views

app_name = 'billboard_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^billboard_app/new_msg', views.new_msg, name='new_msg'),
]