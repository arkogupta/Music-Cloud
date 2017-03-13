from django.conf.urls import url
from . import views



app_name = 'music'

urlpatterns =[
   #r'^$' is default when only /music/ is entered
   url(r'^$', views.IndexView.as_view() , name = 'index'), #go to views and find class IndexView and treat it as a view



   #/music/album_id/
   url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view() , name = 'detail'),
   #go to views and find class DetailView and treat it as a view


]
