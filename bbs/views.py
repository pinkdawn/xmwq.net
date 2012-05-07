# coding=UTF-8
from django.shortcuts import render_to_response as rr
from django.template import RequestContext
from models import category, thread, category_thread, thread_reply
from django.contrib.auth.decorators import login_required
from tennis.util.page import split_into_pages as P
from django.contrib.auth.models import User
from models import bbs_log 
#from django.db.models import Q

def home(req):
    cats = category.objects.all().order_by('order')
    cats_dict = []
    for cat in cats:
        _threads = [x._t for x in category_thread.objects.filter(_c=cat)]
        if _threads:
            _threads.sort(key=lambda x : x.last_reply_time) # last replied thread

            _posts = (x.posts for x in _threads)
            _count = reduce(lambda x,y : x+y,_posts)
            cats_dict.append([cat, len(_threads),_count, _threads[-2:]]) 
        else:
            cats_dict.append([cat, 0, 0 ])
        
    return rr('bbs/index.htm',
            {'cats':cats_dict, },
            context_instance = RequestContext(req))

def view(req, cid):
    cat = category.objects.get(id=cid)
    _threads = [x._t for x in category_thread.objects.filter(_c=cat).filter(_t__is_top=False).order_by('-_t__last_reply_time')]
    _top_threads = [x._t for x in category_thread.objects.filter(_c=cat).filter(_t__is_top=True).order_by('-_t__last_reply_time')]
    _thread_page = P(req,_threads)
        
    _t_dict = []
    for _thread in _thread_page.object_list:
        _replys = [x._r for x in thread_reply.objects.filter(_t = _thread)]
        if _replys :
            _reply = max(_replys, key=lambda n: n.time)
            _t_dict.append([_thread, len(_replys),  _reply])
        else:
            _t_dict.append([_thread, 0])
    
    return rr('bbs/category.html',
            {'cat':cat, 'page':_thread_page, 'threads':_t_dict,'tops':_top_threads,},
            context_instance = RequestContext(req))
    
def viewthread(req, cid, tid):
    if req.user.username!='pinkdawn':
        try:
            if req.META.has_key('HTTP_X_FORWARDED_FOR'):
                log = bbs_log(ip =  req.META['HTTP_X_FORWARDED_FOR'],thread_id = tid)
            else:
                log = bbs_log(ip = req.META['REMOTE_ADDR'],thread_id = tid)
                    
            log.userid = req.user.id
            if not log.userid:
                log.userid = 0
            
            log.save()
        except:
            pass  
        
    cat = category.objects.get(id=cid)
    t = thread.objects.get(id=tid)
    _replys = [x._r for x in thread_reply.objects.filter(_t = t).order_by('_r__time')]
    _rp = P(req, _replys)
    return rr('bbs/viewthread.html',
            {'cat':cat, 'thread':t,'page':_rp, },
            context_instance = RequestContext(req))

@login_required
def viewuser(req, uid):
    _u = User.objects.get(id=uid)
    '''_trs = thread_reply.objects.filter(
        Q(_t__user=_u) | Q(_r__user=_u)
    )'''
    
    #_replys = P(req, [(x._t, x._r) for x in _trs], 8)    
    _threads = P(req, [(x._c, x._t) for x in category_thread.objects.filter(_t__user=_u).order_by('-_t__time')], 10)
    
    return rr('bbs/viewuser.html',
            {#'replys':_replys,
             'client':_u,'threads':_threads,},
            context_instance = RequestContext(req))

@login_required    
def log(req):
    logs = bbs_log.objects.order_by('-time')
    log_page = P(req,logs,28)
    _logs = []
    for l in log_page.object_list:
        _ct = category_thread.objects.filter(_t__id=l.thread_id)
        if _ct:
            if l.userid != 0:
                _user = User.objects.get(id=l.userid)
                _logs.append([l.ip, l.time, [_ct[0]._c, _ct[0]._t], _user])
            else:
                _logs.append([l.ip, l.time, [_ct[0]._c, _ct[0]._t]])
    return rr('bbs/log.html',
            {'page':log_page,'dict':_logs,},
            context_instance = RequestContext(req))

@login_required
def init(req):
    cats = [['网动鹭岛','最火热的鹭岛网球动态'], ['约球会友','喊上朋友，一起来运动吧！'], ['网坛新闻','网坛大事']]
    for c,d in cats:
        _temp = category(title = c, desc = d)        
        _temp.save()
        