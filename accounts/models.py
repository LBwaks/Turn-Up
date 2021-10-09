from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from  ckeditor.fields import RichTextField
from django.urls import reverse
from django.conf import settings
import uuid
# Create your models here.

user_type=[
('user','User'),
('artist','Artist'),
('venue_rep','Venue Representative'),
('event_rep','Event Representative')
]
gender = [
    ('male','Male'),
     ('female', 'Female'),
     ('intersex','Intersex')
     ]
class Profile(models.Model):
    profile_uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type_of_user=models.CharField(choices=user_type, blank=True,null=True,max_length=30)
    
    phone_number = PhoneNumberField(unique=True,blank=True,null=True)
    gender= models.CharField(choices=gender,blank=True,null=True, max_length=10)
    type_of_artists= models.CharField(blank=True,null=True,max_length=30)
    
    profile_pic = models.ImageField(upload_to='profile/',blank=True,null=True,default='profile/profile.png')
    bio = RichTextField(blank=True,null=True) 

    organisation_name= models.CharField(blank=True,null=True, max_length= 200)
    organisation_email=models.EmailField(blank=True,null=True,max_length= 200)

    venue_name=models.CharField(blank=True,null=True,max_length= 200)
    venue_email = models.EmailField(blank=True,null=True,max_length= 200)
    venue_no = PhoneNumberField(blank=True,null=True,unique=True)
    
    City = models.CharField(blank=True,null=True,max_length= 200)
    address =models.CharField(blank=True,null=True,max_length= 200)

    facebook_url = models.URLField(blank=True,null=True,max_length= 200)
    twitter_url = models.URLField(blank=True,null=True,max_length= 200)
    instagram_url = models.URLField(blank=True,null=True,max_length= 200)
    website_url = models.URLField(blank=True,null=True,max_length= 200)


    

    @property
    def profile_pic_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url

    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.profile_uuid})
    
