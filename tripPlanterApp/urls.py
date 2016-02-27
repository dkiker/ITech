from django.conf.urls import patterns, url
from tripPlanterApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))