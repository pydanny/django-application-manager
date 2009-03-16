from django.contrib import admin
from application_manager.models import Application, ApplicationLink

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'description')
    
class ApplicationLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_name', 'application', 'description')
    

admin.site.register(Application, ApplicationAdmin)
admin.site.register(ApplicationLink, ApplicationLinkAdmin)