from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="60" class="img-thumbnail"/>'.format(object.photo.url))
    thumbnail.short_description='Profile'
    list_display=('thumbnail','first_name','last_name','designation','created_date')
    list_display_links=('thumbnail','first_name','last_name','designation')
    search_fields=('first_name','last_name','designation')
    list_filter= ('designation','created_date',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user= request.user
        obj.save()
        
admin.site.register(Team,TeamAdmin)
