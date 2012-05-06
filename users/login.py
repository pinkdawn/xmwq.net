from django.shortcuts import render_to_response as rr
from django.template import RequestContext
from django.http import HttpResponseRedirect as rd

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


def log_in(req):
    if req.method == 'GET':
        af = AuthenticationForm()
    elif req.method == 'POST':
        #form = AuthenticationForm(data=req.POST, request = request) if cookie_test else AuthenticationForm(data=request.POST)
        af = AuthenticationForm(data=req.POST)        
        if af.is_valid():
            user = User.objects.get(username = req.POST['username'])
            user.backend = 'django.contrib.auth.backends.ModelBackend'        
            login(req, user)
            if req.POST.has_key('next'):
                return rd(req.POST['next'])
            return rd('/')                
        
    if req.GET.has_key('next'):
        return rr('login.html',
            {'next':req.GET['next'],
             'form':af, },
            context_instance = RequestContext(req))
    else:
        return rr('login.html',
            {'form':af, },
            context_instance = RequestContext(req))

@login_required
def log_out(req):
    logout(req)
    return rd('/')