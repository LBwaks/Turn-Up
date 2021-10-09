# from category.models import Category
from django.db import models
from  ckeditor.fields import RichTextField
import datetime
from django.db.models import indexes
from django.utils import timezone
from autoslug import AutoSlugField
from django.conf import settings
from django.urls import reverse
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.contrib.postgres.indexes import GinIndex


# Create your models here.

class Category(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,editable=False,on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length = 255)
    slug = AutoSlugField(populate_from='name', unique=True)
    description =RichTextField()
    created_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("artist_category",kwargs={'slug':self.slug})

    #     # return reverse('hom')
        # def get_absolute_url(self):
        # return reverse("artist_detail", kwargs={"slug": self.slug})
    
    


class Artist(models.Model):
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
    artist_name=models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='artist_name', unique=True)
    category = models.ForeignKey(Category,verbose_name="Category",on_delete=models.CASCADE)
    # other_artist=models.CharField(blank=True,null=True,max_length=255)
    event_name=models.CharField(max_length=100)
    # event_type=models.CharField(max_length=100)
    event_description=RichTextField()
    event_offer=RichTextField(blank=True,null=True)
    event_charge=models.IntegerField(blank=True,null=True)
    event_group_charge=models.IntegerField(blank=True,null=True)
    event_group_charge_number=models.IntegerField(blank=True,null=True)
    event_start_date=models.DateTimeField(auto_now_add=False)
    event_end_date=models.DateTimeField(auto_now_add=False)
    photo = models.ImageField(upload_to='artists_events_photos/',default='artists_events_photos/artists.jpg')
    video=models.FileField(upload_to='artists_events_videos/',blank=True,null=True)
    is_featured = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    event_county=models.CharField( choices=county_choice, max_length=20,  default=Nairobi)
    event_location=models.CharField(max_length=100)
    likes =models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='Artist_likes',blank=True)
    artist_view=models.IntegerField(default=0,db_index=True)
    created_date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            GinIndex(name='NewGinIndex',fields=['artist_name','event_name'],opclasses=['gin_trgm_ops'])
            ]
    
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    # def video_url(self):
    #     if self.video and hasattr(self.video, 'url'):
    #         return self.video.url

    # def save(self, *args, **kwargs):
    #     new_image = self.reduce_image_size(self.photo)
    #     self.photo = new_image
    #     super().save(*args, **kwargs)

    # def reduce_image_size(self, photo):
    #     # print(photo)
    #     img = Image.open(photo)
    #     thumb_io = BytesIO()
    #     # img=img.resize( (500,300) ) 
    #     img.save(thumb_io, 'jpeg', quality=70)
    #     new_image = File(thumb_io, name=photo.name)
    #     return new_image
# imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.artist_name

    def get_absolute_url(self):
        return reverse("artist_detail", kwargs={"slug": self.slug})
    def get_related_artist_by_tags(self):
       return Artist.objects.filter(category_id=self.category_id).exclude(pk=self.pk)      
      
class Comment(models.Model):
    artist=models.ForeignKey(Artist, related_name="comments",on_delete=models.CASCADE,null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = RichTextField()
    parent = models.ForeignKey('self', null=True, related_name='artist_replies', blank=True, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.artist.artist_name)
    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created_date').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

