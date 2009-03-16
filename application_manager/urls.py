from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^$', 'application_manager.views.application_manager', name='application_manager'),
    
    url(r'^activate/(?P<application_id>[\d]+)$', 
        'application_manager.views.application_activate', 
        name='application_activate'),
        
    #url(r'^deactivate/$',         
    url(r'^deactivate/(?P<application_id>[\d]+)$', 
        'application_manager.views.application_deactivate', 
        name='application_deactivate'),    
     
)

#url(r'^(?P<username>[\w]+)/$', 'profiles.views.profile', name='profile_detail'),