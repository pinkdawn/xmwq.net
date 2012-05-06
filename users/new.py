# coding=UTF-8
# By daoyu 2011-4-12

from django.shortcuts import render_to_response as rr
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect as rd
from models import *

def new(req): #new user
    msg = ''
    if req.method == 'GET':
        avatar_form = new_avatar_form()
        userAddForm = UserCreationForm()        
    elif req.method == 'POST':
        userAddForm = UserCreationForm(req.POST)
        avatar_form = new_avatar_form(req.POST)
        if userAddForm.is_valid():
            _a = avatar()
            _a.desc = req.POST['desc']            
            
            if req.FILES.has_key('avatar'): # 如果有上传图像
                _img = req.FILES['avatar']
                if _img.size < 50*1024: # 图片大小合适
                    userAddForm.save()
                    from tennis.util.file import upload_and_replace
                    _a.avatar = upload_and_replace('avatar',_img,str(userAddForm.instance.id))
                else: # 图片过大
                    msg = "图片大小要小于50kb!"
                    return rr('user/new.htm',
                        {'userAddForm':userAddForm, 'avatar_form':avatar_form,'msg':msg, },
                        context_instance = RequestContext(req))
            else: #没有上传图像，保存新建用户的请求，保存avatar。
                userAddForm.save()
            
            _a.user = userAddForm.instance
            _a.save()
            return rd('/')
    return rr('user/new.htm',
            {'userAddForm':userAddForm, 'avatar_form':avatar_form,'msg':msg, },
            context_instance = RequestContext(req))
        