import os, sys

#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace) 

from os.path import abspath, dirname, join
from site import addsitedir

sys.path.insert(0, abspath(join(dirname(__file__), "../")))
sys.path.insert(0, abspath(join(dirname(__file__), ". . /. . /"))) 

#Add the path to 3rd party django application and to django itself.
sys.path.append('/home/zdy/www/tennis')
#sys.path.append('C:\\yml\\_myScript_\\dj_things\\web_development\\svn_views\\django-registration')

os.environ['DJANGO_SETTINGS_MODULE'] = 'tennis.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()