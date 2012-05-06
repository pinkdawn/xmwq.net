from django.conf.urls.defaults import patterns, include, url
from tennis import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^s/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    (r'^u/(?P<path>.*)$','django.views.static.serve',{'document_root':'D:\\home\\pinkdawn\\webapps\\u'}),
    
    url(r'^$', 'tennis.bbs.views.home'),
    url(r'^bbs/', include('tennis.bbs.urls')),
    url(r'^gallery/', include('tennis.gallery.urls')),
    url(r'^news/', include('tennis.news.urls')),
    url(r'^user/', include('tennis.users.urls')),
    
    (r'^accounts/login/$', 'tennis.users.login.log_in'),
    (r'^accounts/logout/$', 'tennis.users.login.log_out'),
    (r'logout/$','tennis.users.login.log_out'),
    (r'search/$','tennis.users.views.search'),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^init/', 'tennis.bbs.views.init'),
)
