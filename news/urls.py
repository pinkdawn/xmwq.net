# By Daoyu @2011-04-12

from django.conf.urls.defaults import *
from tennis import settings

urlpatterns = patterns('tennis.news',
    url(r'^1/$', 'views.home'),
    url(r'^$', 'views.list'),
    url(r'^create/', 'new.create'),
    (r'^(\d+)/$','views.view'),
    (r'^edit/(\d+)/$','modify.edit'),
    (r'^del/(\d+)/$','modify.delete'),
    (r'^comment/(\d+)/$','comment.articlecomment'),
)
