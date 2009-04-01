from django import template
from django.core.urlresolvers import reverse

from application_manager.models import Application



register = template.Library()


@register.inclusion_tag('application_manager/nav_links.html')
def nav_links(user):
    applications = Application.objects.filter(active=True)
    user_applications = Application.objects.filter(user=user)    
    display_applications = []
    
    for application in applications:
        if application in user_applications:
            application.master_url_name = reverse(application.master_url_name)
            application.css_slug = application.package_identifier
            display_applications.append(application)
            
    return {'applications':display_applications}



from application_manager.views import get_applications
@register.inclusion_tag('application_manager/applications.html')
def application_manager(request):
    """
        Must have the request
    """
    return {'applications':get_applications(request),'next':request.path}