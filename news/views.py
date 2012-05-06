# By daoyu 2011-4-12

from django.shortcuts import render_to_response as rr
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from models import *
from tennis.news.models import *
from tennis.bbs.models import *

def home(req):
#    _as = article.objects.order_by('-time')[:6]
    _cats = category.objects.all()
    _cats_dict = []
    for _cat in _cats:
        _threads = [x._t for x in category_thread.objects.order_by('-_t__time').filter(_c = _cat)[:6]]
        _cats_dict.append([_cat, _threads])
    
    return rr('home.html',
            {#'articles':_as, 
             'categories':_cats_dict,},
            context_instance = RequestContext(req))

def view(req, aid):
    _article = article.objects.get(id=aid)
    _cs = [x._c for x in article_comment.objects.filter(_a=_article)]
    return rr('news/detail.html',
            {'article':_article, 'comments':_cs,},
            context_instance = RequestContext(req))

def list(req):
    _articles = article.objects.all()
    return rr('news/list.html',
            {'articles':_articles, },
            context_instance = RequestContext(req))