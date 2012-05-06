from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

def get_upload_to(instance, filename):
    return 'upload/avatar/' + str(instance.user.id) + '/' + filename     

class avatar(models.Model):
    def __unicode__(self):
        return self.user.username
    
    user = models.ForeignKey(User, unique = True)
    desc = models.TextField(max_length=100)
    avatar = models.ImageField(upload_to=get_upload_to,blank=True)
    
class new_avatar_form(ModelForm):    
    class Meta:
        model = avatar   
        exclude = ('user')

