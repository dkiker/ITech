from django.conf.urls import patterns, url
from tripPlanterApp import views

urlpatterns = patterns('',
                        url(r'^$', views.index, name='index'),
                        url(r'^trip/(?P<tripID>[\w\-]+)/$',views.summary, name='tripSummary'),
                        url(r'^plan/(?P<location>[\w\-]+)$',views.plan, name='plan'),
                        url(r'^explore/$',views.explore, name='explore'),
                        url(r'^about/$',views.about, name='about'),
                        url(r'^search_trips/', views.search_trips, name='search_trips'),


                       )