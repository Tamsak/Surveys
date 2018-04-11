from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^process$',views.submit),
    url(r'^process/result/$', views.result)
]