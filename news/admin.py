#By Daoyu @2010-07-06
from django.contrib import admin
from tennis.news.models import *

admin.site.register(article)
admin.site.register(comment)
admin.site.register(article_comment)