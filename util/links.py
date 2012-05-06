# By Daoyu @2010-07-07
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from uncle.users.models import *

def show_403(request):
    msg = ''
    if request.GET.has_key('msg'):
        msg = request.GET['msg']
    
    return render_to_response('403.html',
        {'msg':msg,},         
        context_instance=RequestContext(request))

#-------------------------------------------------------------------------------
# Display the http://.../other/ page.
#-------------------------------------------------------------------------------
@login_required
def other(request):
    return render_to_response('other.html',
        {},         
        context_instance=RequestContext(request)) 

#-------------------------------------------------------------------------------
# Display the about page.
#-------------------------------------------------------------------------------
def about(request):
    return render_to_response('about.html',
        {},         
        context_instance=RequestContext(request))


