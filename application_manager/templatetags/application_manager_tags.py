from django import template
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

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
            application.css_slug = slugify(application.title)
            display_applications.append(application)
            
    return {'applications':display_applications}


"""
<li class="tab rtab_profile"><div><a href="{% url profiles.views.profile request.user.username %}">{% trans "My Profile" %}</a></div></li>
<li class="tab rtab_friends"><div><a href="{% url list_friends request.user.username %}">{% trans "Friends" %}</a></div></li>
<li class="tab rtab_all_profile"><div><a href="{% url profile_search %}">{% trans "All Profiles" %}</a></div></li>                
<li class="tab rtab_inbox"><div><a href="{% url messages_inbox %}">{% trans "Inbox" %} ({{ combined_inbox_count }})</a></div></li>                
<!-- 
<li class="tab rtab_photos"><div><a href="{% url photos.views.photos %}">{% trans "Photos" %}</a></div></li>
<li class="tab rtab_blogs"><div><a href="{% url blog.views.blogs %}">{% trans "Blogs" %}</a></div></li>
<li class="tab rtab_projects"><div><a href="{% url your_projects %}">{% trans "Projects" %}</a></div></li>
<li class="tab rtab_tribes"><div><a href="{% url your_tribes %}">{% trans "Groups" %}</a></div></li>
<li class="tab rtab_tweets"><div><a href="{% url tweets_you_follow %}">{% trans "Statuses" %}</a></div></li>
<li class="tab rtab_bookmarks"><div><a href="{% url bookmarks.views.bookmarks %}">{% trans "Bookmarks" %}</a></div></li>
<li class="tab rtab_inbox"><div><a href="{% url messages_inbox %}">{% trans "Inbox" %} ({{ combined_inbox_count }})</a></div></li>


"""