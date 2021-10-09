from django.contrib import admin
from.models import  Category,Artist,Comment
from django.utils.html import format_html
from django.contrib.auth.models import User 
# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    def ImageThumbnail(self,object):
        return format_html('<img src="{}" width="60" class="img-thumbnail"/>'.format(object.photo.url))
    ImageThumbnail.short_description='Event Poster'


    list_display =  ('artist_name', 'ImageThumbnail','event_name',
    # 'category',
    'created_date','is_featured')
    list_editable=('is_featured',)
    search_fields=('artist_name','event_name','event_county','event_location')
    list_filter= ('event_start_date','created_date','event_charge')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user= request.user
        obj.save()
    
admin.site.register(Artist,ArtistAdmin)

class CategoryAdmin(admin.ModelAdmin):
    # def ImageThumbnail(self,object):
    #     return format_html('<img src="{}" width="60" class="img-thumbnail"/>'.format(object.photo.url))
    # ImageThumbnail.short_description='Event Poster'


    list_display =  ('name','description','created_date')
    
    search_fields=('name',)
    list_filter= ('name','created_date')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user= request.user
        obj.save()
    
admin.site.register(Category,CategoryAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('artist','user')

admin.site.register(Comment,CommentAdmin)
