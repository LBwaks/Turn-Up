from django.db import models
from  ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.conf import settings
from django.urls import reverse 
# import datetime
from django.utils import timezone


class Category(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,editable=False,on_delete=models.CASCADE,null=False,related_name='venue_category_user')
    name = models.CharField(max_length = 255)
    slug = AutoSlugField(populate_from='name', unique=True)
    description =RichTextField()
    created_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("category",kwargs={'slug':self.slug}) 

# Create your models here.
class Venue(models.Model):    
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
    venue_name = models.CharField(max_length = 255)
    slug = AutoSlugField(populate_from='venue_name', unique=True)
    category = models.ForeignKey(Category,default="None",on_delete=models.CASCADE,related_name='venue_category')
    event_name = models.CharField(max_length = 255)
    event_start_date=models.DateTimeField(auto_now_add=False)
    event_stop_date=models.DateTimeField(auto_now_add=False)    
    event_attendees =models.IntegerField(blank=True,null=True)
    event_description =RichTextField()
    event_offer=RichTextField(blank=True,null=True)
    speaker_artist = models.CharField(max_length = 255,blank=True,null=True)
    event_fee = models.CharField(max_length = 255, null=True, blank=True)
    event_group_charge=models.IntegerField(blank=True,null=True)
    event_group_charge_number=models.IntegerField(blank=True,null=True)
    photo = models.ImageField(upload_to='venue_event_photo/',default="venue_event_photo/venues.jpg")
    video=models.FileField(upload_to='venue_events_videos/',blank=True,null=True)
    is_featured = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    venue_county=models.CharField( choices=county_choice,max_length=20,  default=Nairobi)
    venue_location=models.CharField(max_length=100)
    likes =models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='Venue_likes',blank=True)    
    venue_view=models.IntegerField(default=0,db_index=True)
    created_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
         return self.venue_name

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("venue_details", kwargs={"slug": self.slug})
    
    def get_related_venue_by_tags(self):
        return Venue.objects.filter(category_id=self.category_id).exclude(id=self.id)      
        


class Commenting(models.Model):
    venue=models.ForeignKey(Venue, related_name="commenting",on_delete=models.CASCADE,null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reply = models.ForeignKey('Commenting', null=True, related_name='venue_replies', blank=True, on_delete=models.CASCADE)

    body = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return (self.venue.venue_name)
