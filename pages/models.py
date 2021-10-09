from django.db import models
from autoslug import AutoSlugField
from django.conf import settings

# Create your models here.
class Team(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,editable=False,on_delete=models.CASCADE,null=False) 
    first_name= models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='first_name', unique=True)
    last_name =models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='team_photos/%Y/%m/%d/',default="team_photos/avatar.png")
    facebook_link=models.URLField(max_length=250)
    twitter_link=models.URLField(max_length=250)
    linkedin_link=models.URLField(max_length=250)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
