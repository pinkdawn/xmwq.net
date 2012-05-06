from models import *
from django.shortcuts import render_to_response as rr
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect as rd

@login_required
def create(req):
    if req.method == 'GET':
        form = new_article_form()
    elif req.method == 'POST':
        form = new_article_form(req.POST)
        if form.is_valid():
            form.instance.author = req.user
            form.save()
            return rd("/news/")            
        
    return rr('news/create.html',
            {'form':form, },
            context_instance = RequestContext(req))