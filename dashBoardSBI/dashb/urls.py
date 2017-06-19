from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chart/([0-9]*)/$', views.chart, name='charts'),
]