from sys import stderr

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from application_manager.models import Application

def get_applications(request):
    """ This is a handy function for getting all the data needed to display
        application manager views. 
    """
    applications = Application.objects.filter(active=True)
    user_applications = Application.objects.filter(user=request.user)
    for application in applications:
        # We construct the links here off the ApplicationLink
        # objects because I can't figure out how to turn url names
        # in Django into valid URLs via the template engine.
        # It would be nice to move this out at some point.

        link_list = []
        for app_link in application.application_link.all():
            link_dict = {'title':app_link.title,
                        'href':reverse(app_link.url_name),
                        'description':app_link.description}
            link_list.append(link_dict)
        application.link_list = link_list
        
        # flag the application as activated or not.
        if application in user_applications:
            application.activated = True
        else:
            application.activated = False
            
        # Fetch the url name of the application itself
        application.url_name = reverse(application.master_url_name)
        
        ####################################################
        # Get a set of items based on the application type
        ####################################################
        
        # Fetch the model
        module = __import__(application.package_identifier, globals(), locals())
        model = module.models.__dict__[application.model_identifier]
        user_lookup_name = '%s_id' % application.user_lookup_name
        print >> stderr, model
        items = model.objects.all()        
        print >> stderr, items.query        
        print >> stderr, items              
        where_stmt = '%s=%s' % (user_lookup_name, request.user.id)
        items = items.extra(where=[where_stmt]).reverse()[:application.sample_limit]        
        print >> stderr, items.query
        print >> stderr, items        
        
        # prepare the item_url
        item_url_list = application.item_url.split('.')
            
        
        for item in items:
            # TODO: WTF?!? For some obscure reason we need this print statement here
            # Or things don't work right in that it can't find the cached related object 
            print >> stderr, item

            # set the item URL
            if len(item_url_list) == 2:
                # We traverse to a cached object here                
                cached_object = item.__dict__['_%s_cache' % item_url_list[0]]
                # now we fetch the URL from the cached object
                item_url = cached_object.__dict__[item_url_list[1]]
            elif len(item_url_list) == 1:
                # fetch the url directly                
                item_url = item_url_list[0]
                if item_url == 'get_absolute_url':
                    item_url = item.get_absolute_url()
                else:
                    item_url = item.__dict__[item_url_list[0]]
            else:
                # TODO - handle longer traversals
                # TODO - likely merging with the first if in this block group
                pass
            item.url = item_url
            
            # now set the item title and description
            item.title = item.__dict__[application.item_title]
            item.description = item.__dict__[application.item_description]            
        
        application.items = items  
        
    return applications  

def application_manager(request,template_name='application_manager/applications.html'):
    """ This is a application_manager view """
    applications = get_applications(request)
        
    response_dictionary = {'applications':applications}    
    return render_to_response(template_name, response_dictionary, context_instance=RequestContext(request))
    
def application_activate(request,application_id):
    application = get_object_or_404(Application, id = application_id)
    application.user.add(request.user)
    msg = "You have activated %s" % application.title
    request.user.message_set.create(message=msg)
    next = request.GET.get("next",None)
    if next:
        return HttpResponseRedirect(next)
    return HttpResponseRedirect(reverse("application_manager"))

    
def application_deactivate(request,application_id):
    application = get_object_or_404(Application, id = application_id)
    application.user.remove(request.user)
    msg = "You have deactivated %s" % application.title
    request.user.message_set.create(message=msg)  
    next = request.GET.get("next",None)
    if next:
        return HttpResponseRedirect(next)
    return HttpResponseRedirect(reverse("application_manager"))
