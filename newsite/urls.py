from django.conf.urls import patterns, include, url
from aperson import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.login),
    url(r'^errlogin/$', views.errlogin),
    url(r'^home/$', views.check),
    url(r'^register/$', views.register),
    url(r'^registerme/$', views.check2),
    url(r'^result/$',views.search),
    url(r'^newsearch/$',views.newsearch),
    url(r'^tweets/$',views.tweets),
)

