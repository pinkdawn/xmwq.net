# coding=UTF-8
# By daoyu 2011-4-12

from django.shortcuts import render_to_response as rr
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect as rd
from models import *

def update(req): #update user
    pass

def change_avatar(req):
    msg = ''
    if req.method == 'GET':
        avatar_form = new_avatar_form()
        try:
            avatar_form.instance = req.user.get_profile()
        except:
            pass
    elif req.method == 'POST':
        avatar_form = new_avatar_form(req.POST)
        if avatar.objects.filter(user=req.user):
            _a = avatar.objects.filter(user=req.user)[0]
        else :
            _a = avatar()
            _a.user = req.user
        if req.FILES.has_key('avatar'):
            _img = req.FILES['avatar']
                
            if _img.size < 50*1024:
                from tennis.util.file import upload_and_replace
                _a.avatar = upload_and_replace('avatar',_img,str(_a.user.id))
            else:
                msg = "图片大小要小于50kb!"
                return rr('user/change_avatar.htm',
                    {'avatar_form':avatar_form,'msg':msg, },
                    context_instance = RequestContext(req))
            
        _a.desc = req.POST['desc']
        _a.save()
        return rd('/')
    return rr('user/change_avatar.htm',
            {'avatar_form':avatar_form,'msg':msg, },
            context_instance = RequestContext(req)) 