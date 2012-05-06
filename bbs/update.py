# coding=UTF-8
from django.shortcuts import render_to_response as rr
from django.http import HttpResponseRedirect as rd
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import thread, reply,thread_reply
from django.contrib.auth.decorators import login_required
from tennis.util.page import split_into_pages as P

@login_required
def reply_to_thread(req, cid, tid):
    if req.method == 'POST':
        _t = thread.objects.get(id=tid)
        
        _r = reply()
        _r.text = req.POST['replytext']
        _r.user = req.user
        _r.floor = _t.posts + 1 
        _r.save()
        
        _t.posts = _t.posts + 1
        _t.last_reply_time = _r.time
        _t.save()
        
        _tr = thread_reply()
        _tr._t = _t;
        _tr._r = _r;
        _tr.save()
        
        return rd('/bbs/'+str(cid)+'/'+str(tid)+'/')

@login_required
def edit_thread(req, cid, tid):
    _t = thread.objects.get(id=tid)
    if _t.user.id == req.user.id or req.user.groups.all()[0].name == "admin":
        if req.method=='GET':
            return rr('bbs/edit_thread.html',
                {'thread':_t,'catid':cid,},
                context_instance = RequestContext(req))
        elif req.method =='POST':           
            _t.title = req.POST['threadname']
            _t.text = req.POST['threadtext']
            _t.save()
    else:
        pass
    return rd('/bbs/'+str(cid)+'/'+str(tid)+'/')

@login_required
def close_thread(req, cid, tid):
    if req.user.groups.all()[0].name == "admin":
        _thread = thread.objects.get(id=tid)
        _thread.is_commentable = False;
        _thread.save()        
    else:
        pass
    return rd('/bbs/'+str(cid)+'/'+str(tid)+'/')

@login_required
def open_thread(req, cid, tid):
    if req.user.groups.all()[0].name == "admin":
        _thread = thread.objects.get(id=tid)
        _thread.is_commentable = True;
        _thread.save()        
    else:
        pass
    return rd('/bbs/'+str(cid)+'/'+str(tid)+'/')

@login_required
def delete_thread(req, cid, tid):
    if req.user.groups.all()[0].name == "admin":
        thread.objects.filter(id=tid).delete()
    else:
        pass
    return rd('/bbs/'+str(cid)+'/')

@login_required
def delete_reply(req,cid, tid, rid):
    if req.user.groups.all()[0].name == "admin":
        reply.objects.filter(id=rid).delete()
    else:
        pass
    
    return rd('/bbs/'+str(cid)+'/'+str(tid)+'/')

@login_required
def top_thread(req, cid, tid):
    if req.user.groups.all()[0].name == "admin":
        _thread = thread.objects.get(id=tid)
        _thread.is_top = True;
        _thread.save()        
    else:
        pass
    return rd('/bbs/'+str(cid)+'/'+str(tid)+'/')

@login_required
def untop_thread(req, cid, tid):
    if req.user.groups.all()[0].name == "admin":
        _thread = thread.objects.get(id=tid)
        _thread.is_top = False;
        _thread.save()        
    else:
        pass
    return rd('/bbs/'+str(cid)+'/'+str(tid)+'/')