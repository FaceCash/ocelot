#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('ocelot.app.facebook',
    url(r'^$', 'views.home', name='home'),
)

