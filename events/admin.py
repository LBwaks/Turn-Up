from django.contrib import admin
from .models import Comment, Event,Category
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name','event_county','event_location','event_start_date','created_date','is_featured')
    list_editable=('is_featured',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user= request.user
        obj.save()

admin.site.register(Event,EventAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','description')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user= request.user
        obj.save()
        
admin.site.register(Category,CategoryAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display =('event','user')

admin.site.register(Comment,CommentAdmin)