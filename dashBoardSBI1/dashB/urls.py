from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^inwardcomp/$', views.compIn_view, name='compin'),
	url(r'^outwardcomp/$', views.compOut_view, name='compout'),
    url(r'^outward([a-zA-Z]*)/$', views.outward_view, name='outward'),
    url(r'^inward([a-zA-Z]*)/$', views.inward_view, name='inward'),
    url(r'^viewdata/$', views.view_data, name='viewData'),
    url(r'^$', views.index, name='index'),
]