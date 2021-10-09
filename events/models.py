from django.db import models
# from  artists.models import Category
from ckeditor.fields import RichTextField
import datetime
from django.utils import timezone
from autoslug import AutoSlugField
from django.urls import reverse
from django.conf import settings


class Category(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,editable=False,null=False,related_name='event_category_user')
    name = models.CharField(max_length = 255)
    slug = AutoSlugField(populate_from='name', unique=True)
    description =RichTextField()
    created_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("event_category",kwargs={'slug':self.slug})

# Create your models here.
class Event(models.Model):
    Mombasa = 'Mombasa'
    Kwale= 'Kwale'
    Kilifi= 'Kilifi'
    TanaRiver= 'Tana River'
    Lamu= 'Lamu'
    TaitaTaveta= 'Taita-Taveta'
    Garissa ='Garissa'
    Wajir= 'Wajir'
    Mandera= 'Mandera'
    Marsabit= 'Marsabit'
    Isiolo= 'Isiolo'
    MERU= 'MERU'
    TharakaNithi= 'Tharaka-Nithi'
    Embu= 'Embu'
    Kitui ='Kitui'
    Machakos= 'Machakos'
    Makueni= 'Makueni'
    Nyandarua= 'Nyandarua'
    Nyeri= 'Nyeri'
    Kirinyaga='Kirinyaga'
    Muranga="Muranga"
    Kiambu= 'Kiambu'
    Turkana ='Turkana'
    WestPokot='West Pokot'
    Samburu= 'Samburu'
    TransNzoia ='Trans Nzoia'
    UasinGishu= 'Uasin Gishu'
    ElgeyoMarakwet= 'Elgeyo-Marakwet'
    Nandi ='Nandi'
    Baringo= 'Baringo'
    Laikipia ='Laikipia'
    Nakuru= 'Nakuru'
    Narok= 'Narok'
    Kajiado= 'Kajiado'
    Kericho= 'Kericho'
    Bomet= 'Bomet'
    Kakamega ='Kakamega'
    Vihiga= 'Vihiga'
    Bungoma= 'Bungoma'
    Busia= 'Busia'
    Siaya= 'Siaya'
    Kisumu ='Kisumu'
    HomaBay= 'Homa Bay'
    Migori= 'Migori'
    Kisii= 'Kisii'
    Nyamira= 'Nyamira'
    Nairobi= 'Nairobi'

    county_choice= [
        (Mombasa, 'Mombasa'),
        (Kwale, 'Kwale'),
        (Kilifi, 'Kilifi'),
        (TanaRiver, 'Tana River'),
        (Lamu, 'Lamu'),
        (TaitaTaveta, 'Taita-Taveta'),
        (Garissa ,'Garissa'),
        (Wajir, 'Wajir'),
        (Mandera, 'Mandera'),
        (Marsabit, 'Marsabit'),
        (Isiolo, 'Isiolo'),
        (MERU, 'Meru'),
        (TharakaNithi, 'Tharaka-Nithi'),
        (Embu, 'Embu'),
        (Kitui ,'Kitui'),
        (Machakos, 'Machakos'),
        (Makueni, 'Makueni'),
        (Nyandarua, 'Nyandarua'),
        (Nyeri, 'Nyeri'),
        (Kirinyaga,'Kirinyaga'),
        (Muranga,"Murang'a"),
        (Kiambu, 'Kiambu'),
        (Turkana ,'Turkana'),
        (WestPokot,' West Pokot'),
        (Samburu, 'Samburu'),
        (TransNzoia ,'Trans Nzoia'),
        (UasinGishu, 'Uasin Gishu'),
        (ElgeyoMarakwet, 'Elgeyo-Marakwet'),
        (Nandi ,'Nandi'),
        (Baringo, 'Baringo'),
        (Laikipia ,'Laikipia'),
        (Nakuru, 'Nakuru'),
        (Narok, 'Narok'),
        (Kajiado, 'Kajiado'),
        (Kericho, 'Kericho'),
        (Bomet, 'Bomet'),
        (Kakamega ,'Kakamega'),
        (Vihiga, 'Vihiga'),
        (Bungoma, 'Bungoma'),
        (Busia, 'Busia'),
        (Siaya, 'Siaya'),
        (Kisumu ,'Kisumu'),
        (HomaBay, 'Homa Bay'),
        (Migori, 'Migori'),
        (Kisii, 'Kisii'),
        (Nyamira, 'Nyamira'),
        (Nairobi, 'Nairobi'),
    ]

    user=models.ForeignKey(settings.AUTH_USER_MODEL,editable=False,on_delete=models.CASCADE,null=False)
    event_name = models.CharField(max_length = 255)
    slug = AutoSlugField(populate_from='event_name', unique=True)
    event_county = models.CharField( choices=county_choice, max_length=20,  default=Nairobi)
    event_location = models.CharField(max_length = 255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default="None",related_name='event_category')
    event_description =RichTextField()
    event_offer=RichTextField(blank=True,null=True)
    event_charge = models.IntegerField(blank=True,null=True)
    event_group_charge=models.IntegerField(blank=True,null=True)
    event_group_charge_number=models.IntegerField(blank=True,null=True)
    event_host = models.CharField(max_length = 255,blank=True,null=True)
    event_start_date=models.DateTimeField(auto_now_add=False)
    event_stop_date=models.DateTimeField(auto_now_add=False) 
    speaker_artist =models.CharField(max_length = 255,blank=True,null=True)
    photo = models.ImageField(upload_to='event_photos/',default="event_photos/events.jpg")
    # video=models.FileField(upload_to='event_events_videos/',blank=True,null=True)
    event_attendees = models.IntegerField(blank=True,null=True)
    event_view=models.IntegerField(default=0,db_index=True)
    likes =models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='Event_likes',blank=True)
    is_featured =models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.event_name

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("event_details", kwargs={"slug": self.slug})

    def get_related_event_by_tags(self):
        return Event.objects.filter(category_id=self.category_id).exclude(id=self.id) 

class Comment(models.Model):
    event=models.ForeignKey(Event, related_name="comments",on_delete=models.CASCADE,null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_events_comments', on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', null=True, related_name='event_replies', blank=True, on_delete=models.CASCADE)
    body = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.event.event_name)

