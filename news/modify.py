from django.shortcuts import render_to_response as rr
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect as rd
from models import *

@login_required
def edit(req, aid):
    if req.method == 'GET':
        _article = article.objects.get(id=aid)
        form = new_article_form(instance = _article)        
    elif req.method == 'POST':
        form = new_article_form(req.POST)
        if form.is_valid():
            _article = article.objects.get(id=aid)            
            _article.title = req.POST['title']
            _article.text = req.POST['text']
            _article.save()
            return rd('/news/' + str(_article.id) + '/')
    
    return rr('news/edit.html',
            {'form':form, },
            context_instance = RequestContext(req))

@login_required
def delete(req, aid):
    article.objects.get(id=aid).delete()
    return rd("/news/")