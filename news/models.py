from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class article(models.Model):
    def __unicode__(self):
        return self.title
    
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(User,related_name='author', unique = False)
    time = models.DateTimeField(auto_now_add = True)
    text = models.TextField(max_length=16384)

class new_article_form(ModelForm):    
    class Meta:
        model = article   
        exclude = ('time', 'author')


class comment(models.Model):
    nick =  models.CharField(max_length = 40)
    email = models.CharField(max_length = 40, blank = True)
    text = models.TextField(max_length=140)
    time = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.nick
    
class article_comment(models.Model):
    _a = models.ForeignKey(article,related_name='article', unique=False)
    _c = models.ForeignKey(comment,related_name='comment', unique=True)