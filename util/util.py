# By daoyu @2010-07-10

from uncle.users.models import *

def update(user, content):    
    _update = update()
    _update.content = user.first_name + ', ' + user.last_name + ' with account (' + user.username + ') ' + content    
    _update.save()
    
#-------------------------------------------------------------------------------
# old [1,2,3] rest [2,3] new [3,5,7] ==>
# old [1,2,3,5,7] rest[2]
#-------------------------------------------------------------------------------
def append_non_repeat(old, rest, new):
    for value in new:
        if not value in old:
            old.append(value)
        if value in rest:
            rest.remove(value)

    return old, rest

#-------------------------------------------------------------------------------
# Using re to match whether a string is email address.
#-------------------------------------------------------------------------------
def match_email_address(text):
    import re            
    p = re.compile('\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*')
    if p.match(text):
        return True
    
    return False

#-------------------------------------------------------------------------------
# Remove the last blank and special characters from string.
#-------------------------------------------------------------------------------
def format_string(fn):
    fn = fn.lower()
    fn = fn.strip()
    for op in '+-*':
        fn = fn.replace(op,'')
        
    return fn;

#-------------------------------------------------------------------------------
# Test whether the name is a pitcure.
#-------------------------------------------------------------------------------
def is_picture(fn):
    _fn = fn.lower()
    _fn = _fn.split('.')[-1]
    if _fn in ['jpg','png','bmp','gif','tif','dpx']:
        return True
    else:
        return False

#-------------------------------------------------------------------------------
# Test whether the name is a video.
#-------------------------------------------------------------------------------
def is_video(fn):
    _fn = fn.lower()
    _fn = _fn.split('.')[-1]
    if _fn in ['mov','mp4','flv','3gp']:
        return True
    else:
        return False

import re

r = re.compile(r'\b([A-Z][a-z]+[A-Z][a-z]+)\b')
def process(content):
    return re.sub(r'[\n\r]+', '<br/><br/>', content)
