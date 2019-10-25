from django.urls import path
from django.conf.urls import url
from.import views


app_name = 'structured_learning'

urlpatterns = [
    path('', views.structured_learning,name="structured"),
   	url(r'^w0/$', views.w0, name = "w0"),
   	url(r'^w1/$', views.w1, name = "w1"),
   	url(r'^w2/$', views.w2, name = "w2"),
   	url(r'^w3/$', views.w3, name = "w3"),
   	url(r'^w4/$', views.w4, name = "w4"),
   	url(r'^w5/$', views.w5, name = "w5"),


]
