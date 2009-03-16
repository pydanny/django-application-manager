from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from application_manager.docs import *


class Application(models.Model):
    
    user = models.ManyToManyField(User, blank=True, null=True, verbose_name=_('user'))
    title = models.CharField(_('title'), help_text=_(app_title_doc), max_length=100, unique=True)    
    description = models.TextField(_("description"), help_text=_(app_description_doc), null=True, blank=True)
    master_url_name = models.CharField(_("master url name"), help_text=_(master_url_name_doc),max_length=100, unique=True)             
    active = models.BooleanField(_('active'), help_text=_(active_doc), default=False)    
    
    # This section handles sample items displayed in Application manager's interface
    # These sample items are called 'items' for the sake of clarity and simplicity
    user_lookup_name = models.CharField(_("user lookup name"), help_text=_(user_lookup_name_doc) ,max_length=20, unique=False) 
    package_identifier = models.CharField(_("package identifier"), help_text=_("This is the application module name. So the Pinax bookmarks app would be simply <strong>bookmarks</strong>.") ,max_length=100, unique=True) 
    model_identifier = models.CharField(_("model identifier"), help_text=_("This is the application model name. So the Pinax bookmarks BookmarkInstance model would be simply <strong>BookmarkInstance</strong>.") ,max_length=100)     
    sample_limit = models.IntegerField(_("sample limit"), help_text=_("This is how many sample items should be displayed"))     
    item_url = models.CharField(_("item url"), max_length=100, help_text=_("This describes where the link is stored. So for bookmarks, it would be <strong>bookmark.url</strong>."))
    item_title = models.CharField(_("item title"), max_length=100, help_text=_("This describes where the title is displayed. The bookmark example oddly enough is <strong>description</strong>."))    
    item_description = models.CharField(_("item description"), max_length=100, help_text=_("This describes where the description is displayed. The bookmark example oddly enough is <strong>note</strong>."))


    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = _('application')
        verbose_name_plural = _('applications')
        
class ApplicationLink(models.Model):
    
    application = models.ForeignKey(Application, related_name="application_link", verbose_name=_('applications'))
    url_name = models.CharField(_("url name"), help_text=_("Enter url names.<br />Example: Bookmarks might include <strong>all_bookmarks</strong> and <strong>your_bookmarks</strong>.") ,max_length=100, unique=True) 
    title = models.CharField(_('title'), help_text=_("Your application link's name.<br />Example: Bookmakrs might include <strong>all bookmarks</strong> and <strong>your bookmarks</strong>"), max_length=100)
    description = models.TextField(_("description"), null=True, blank=True)


    def __unicode__(self):
        return ' '.join((self.title,self.url_name))
        
    class Meta:
        verbose_name = _('application link')
        verbose_name_plural = _('applications links')
        