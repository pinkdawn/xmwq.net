# By daoyu 2011-4-12

from django.shortcuts import render_to_response as rr
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

def home(req):
    return rr('user/index.html',
            { },
            context_instance = RequestContext(req))

def view(req): 
    pass

def list(req): 
    pass

def listName(req): 
    pass

def search(req):
    return rr('search.html', context_instance = RequestContext(req))