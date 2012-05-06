from models import *
from django.shortcuts import render_to_response as rr
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect as rd

def articlecomment(req , aid):
    if req.method=='POST':
        _a = article.objects.get(id=aid) 
        _c = comment()
        _c.text = req.POST['comment_text']
        _c.nick = req.POST['nick_name']
        _c.email = req.POST['email']
        _c.save()
        
        _ac = article_comment()
        _ac._a = _a;
        _ac._c = _c;
        _ac.save()
        
        return rd('/news/' + str(aid) + '/')
        
        