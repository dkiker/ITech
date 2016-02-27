from django.conf.urls import patterns, url
from tripPlanterApp import views

urlpatterns = patterns('',
                        url(r'^/$', views.index, name='index'),
                        url(r'^trip/(?P<tripID>[\w\-]+)/$',views.summary, name='tripSummary'),
                        url(r'^add_trip/', views.add_trip, name='add_trip'),
                       )