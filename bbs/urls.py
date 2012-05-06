# By Daoyu @2011-04-12

from django.conf.urls.defaults import *
from tennis import settings

urlpatterns = patterns('tennis.bbs',
    url(r'^$', 'views.home'),
    (r'^(\d+)/$','views.view'),
    (r'^(\d+)/(\d+)/reply/$','update.reply_to_thread'),
    (r'^(\d+)/(\d+)/edit/$','update.edit_thread'),
    (r'^(\d+)/(\d+)/close/$','update.close_thread'),
    (r'^(\d+)/(\d+)/open/$','update.open_thread'),
    (r'^(\d+)/(\d+)/top/$','update.top_thread'),
    (r'^(\d+)/(\d+)/untop/$','update.untop_thread'),
    (r'^(\d+)/(\d+)/delete/$','update.delete_thread'),
    (r'^reply/(\d+)/(\d+)/(\d+)/delete/$','update.delete_reply'),
    
    (r'^(\d+)/(\d+)/$','views.viewthread'),
    (r'^(\d+)/new/$','create.new'),
    
    (r'^user/(\d+)/$','views.viewuser'),
    (r'^log/$','views.log'),
)
