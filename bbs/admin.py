#By Daoyu @2010-07-06
from django.contrib import admin
from tennis.bbs.models import *

admin.site.register(reply)
admin.site.register(thread)
admin.site.register(thread_reply)
admin.site.register(category)
admin.site.register(category_thread)
admin.site.register(bbs_log)