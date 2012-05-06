# By Daoyu @2011-04-12

from django.conf.urls.defaults import *
from tennis import settings

urlpatterns = patterns('tennis.users',
    url(r'^$', 'views.home'),
    url(r'^edit/$', 'update.change_avatar'),
    url(r'^register/', 'new.new'),
)
