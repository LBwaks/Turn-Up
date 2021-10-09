from artists.models import Category
from django.contrib import admin
from .models import Venue,Commenting,Category
# Comments

class VenueAdmin(admin.ModelAdmin):
    list_display =  ('venue_name','event_name',
    'category',
    'event_start_date','event_stop_date','is_featured')
    list_editable=('is_featured',)
    search_fields=('venue_name','event_name',)
    list_filter= ('event_start_date','created_date',
    # 'category',
    'event_stop_date')
    # """docstring for ."""
    #
    # def __init__(self, arg):
    #     super(, self).__init__()
    #     self.arg = arg
    #

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user= request.user
        obj.save()

admin.site.register(Venue,VenueAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('venue','user')

admin.site.register(Commenting,CommentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display =('name','description','created_date')
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user= request.user
        obj.save()
admin.site.register(Category,CategoryAdmin)
