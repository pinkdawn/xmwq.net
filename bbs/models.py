from django.db import models
from django.contrib.auth.models import User

class thread(models.Model):
    def __unicode__(self):
        return self.title
    
    title = models.CharField(max_length = 100)
    user = models.ForeignKey(User, unique = False)
    time = models.DateTimeField(auto_now_add = True)
    text = models.TextField(max_length=2500)
    last_reply_time = models.DateTimeField(auto_now_add = True)
    posts = models.IntegerField()
    is_commentable = models.BooleanField(default=True)
    is_top = models.BooleanField(default=False)

class category(models.Model):
    def __unicode__(self):
        return self.title
    
    title = models.CharField(max_length = 40)
    desc = models.CharField(max_length = 50) #description
    order = models.IntegerField(blank=True)
    
class category_thread(models.Model):
    _c = models.ForeignKey(category, unique = False)
    _t = models.ForeignKey(thread, unique = True)
    
class reply(models.Model):
    def __unicode__(self):
        return self.text
    
    time = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, unique = False)
    text = models.TextField(max_length=200)
    floor = models.IntegerField()
    
class thread_reply(models.Model):
    _t = models.ForeignKey(thread, unique = False)
    _r = models.ForeignKey(reply, unique = True)
    
class bbs_log(models.Model):
    ip = models.CharField(max_length = 40)
    time = models.DateTimeField(auto_now_add = True)
    userid = models.IntegerField(blank=True)
    thread_id = models.IntegerField() 
    def __unicode__(self):
        return self.ip + ' U:' + str(self.userid) + ' T:' + str(self.thread_id)