from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^inward/compin[.a-zA-Z]*/$', views.compIn_view, name='compin'),
	url(r'^outward/compout[.a-zA-Z]*/$', views.compOut_view, name='compout'),
    url(r'^outward/[a-zA-Z]*/([0-9]*)[.a-z]*/$', views.outward_view, name='outward'),
    url(r'^inward/[a-zA-Z]*/([0-9]*)[.a-z]*/$', views.inward_view, name='inward'),
    url(r'^viewdata$', views.view_data, name='viewData'),
    url(r'^$', views.index, name='index'),
]