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
    package_identifier = models.CharField(_("package identifier"), help_text=_(package_identifier_doc) ,max_length=100, unique=True) 
    model_identifier = models.CharField(_("model identifier"), help_text=_(model_identifier_doc) ,max_length=100)     
    sample_limit = models.IntegerField(_("sample limit"), help_text=_(sample_limit_doc))     
    item_url = models.CharField(_("item url"), max_length=100, help_text=_(item_url_doc))
    item_title = models.CharField(_("item title"), max_length=100, help_text=_(item_title_doc))    
    item_description = models.CharField(_("item description"), max_length=100, help_text=_(item_description_doc))


    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = _('application')
        verbose_name_plural = _('applications')
        
class ApplicationLink(models.Model):
    
    application = models.ForeignKey(Application, help_text=_("Our sample cases are based off the ones in the Application model."), related_name="application_link", verbose_name=_('applications'))
    url_name = models.CharField(_("url name"), help_text=_(url_name_doc) ,max_length=100, unique=True) 
    title = models.CharField(_('title'), help_text=_(applink_title_doc), max_length=100)
    description = models.TextField(_("description"), help_text=_(applink_description_doc), null=True, blank=True)


    def __unicode__(self):
        return ' '.join((self.title,self.url_name))
        
    class Meta:
        verbose_name = _('application link')
        verbose_name_plural = _('applications links')
        