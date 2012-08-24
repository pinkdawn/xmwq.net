# Daoyu @2010-07-07

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from settings import MEDIA_ROOT
import os

#-------------------------------------------------------------------------------
#  Give a user request, download the file for user.
#-------------------------------------------------------------------------------
@login_required
def download(request):
    root = MEDIA_ROOT
    path = request.GET['path'].encode('utf-8')
    if not path.startswith(root):        
        path = root + path
    
    filename = path.split('/')[-1]
    
    try:
        f = open(path, 'rb') # read as binary data.  
        data = f.read()
        f.close()
    except:
        return HttpResponseRedirect('/403/?msg=The file does not exist!')

    response = HttpResponse(data, mimetype = 'application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

#-------------------------------------------------------------------------------
# Upload a file object to given path on server.
#-------------------------------------------------------------------------------
def upload(path, file_obj, pre = '', type=''):
    if type:
        pre_name = file_obj.name.encode('utf-8').split('.')[0] + type
    else:
        pre_name = file_obj.name.encode('utf-8')
    name = file_obj.name.encode('utf-8')
    
    if os.path.exists(pre + path):
        while os.path.isfile('%s/%s' % (pre + path, pre_name)):
            name = '_' + name # in same file exists
            pre_name = '_' + pre_name # in same file exists
    else:
        os.makedirs(pre + path) # makedirs make all the dir        

    destination = open('%s/%s' % (pre + path, name), 'wb')

    for chunk in file_obj.chunks():
        destination.write(chunk)
    destination.close()

    return path + '/' + name

#-------------------------------------------------------------------------------
# Upload a file object to given path on server and replace exist one. 
# The original file name is xyz.xxx; If specify a target name, like abc,
# then the new file name is abc.xxx.
#-------------------------------------------------------------------------------
def upload_and_replace(path, file_obj, target_name=''):
    root = MEDIA_ROOT
    if target_name:
        name = target_name + '.' + file_obj.name.encode('utf-8').split('.')[-1]
    else:
        name = file_obj.name.encode('utf-8')

    if not os.path.exists(root + path):        
        os.makedirs(root + path)

    destination = open('%s/%s' % (root + path, name), 'wb')

    for chunk in file_obj.chunks():
        destination.write(chunk)
    destination.close()

    return path + '/' + name
