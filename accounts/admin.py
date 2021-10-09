from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
   
    list_display =  ('user', 'phone_number','gender')
    
    search_fields=('user','gender')
    list_filter= ('user','gender',)
    
admin.site.register(Profile,ProfileAdmin)