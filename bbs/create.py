# coding=UTF-8
from django.shortcuts import render_to_response as rr
from django.http import HttpResponseRedirect as rd
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import category, thread, category_thread
from django.contrib.auth.decorators import login_required

@login_required
def new(req, cid):
    cat = category.objects.get(id=cid)
    if req.method == 'GET':
        return rr('bbs/newthread.html',
                {'cat':cat,},
                context_instance = RequestContext(req))        
    elif req.method == 'POST':
        _t = thread()
        _t.title = req.POST['threadname']
        _t.text = req.POST['threadtext']
        _t.user = req.user
        _t.posts = 0
        _t.save()
        
        _ct = category_thread()
        _ct._t = _t
        _ct._c = cat
        _ct.save()
        
        return rd('/bbs/' + str(cid) + '/')
    