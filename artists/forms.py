from django import forms
from .models import Artist,Comment
from ckeditor.widgets import CKEditorWidget
from django.forms import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import NON_FIELD_ERRORS
import datetime
from django.core.validators import MinValueValidator


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields= ('artist_name','event_name','event_start_date','event_end_date','category',
        'event_charge','event_group_charge','event_group_charge_number','event_description',
        'event_offer','event_county','event_location',
        'photo')
        labels = {
                'artist_name': 'Artists Name',
                'event_name':'Event',
                'event_description':'About The Event',
                'event_charge':'Entry Fee',
                'event_group_charge':'Entry Fee For A Group',
                'event_group_charge_number':'Number Of People Per Group',
                'event_start_date':'Start Datetime',
                'event_county':'County',
                'event_location':'Address',
                'photo':'Event Poster',
                
                'category':'Event Catergory',
                'event_offer':'Offers For This Event',
                'event_end_date':'End Datetime'

        }
        
        widgets = {
           
             'artist_name': forms.TextInput(attrs={'class':'form-control' 'required'}),
             'event_name': forms.TextInput(attrs={'class':'form-control'}),
             'category': forms.Select(attrs={'class':'form-select'}),
             'event_type': forms.TextInput(attrs={'class':'form-control'}),
             'event_start_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),
            'event_end_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),

             'event_description': forms.CharField(widget=CKEditorWidget()),
             'event_offers': forms.CharField(widget=CKEditorWidget()),
             'event_charge': forms.TextInput(attrs={'class':'form-control'}),
             'event_group_charge': forms.TextInput(attrs={'class':'form-control'}),
             'event_group_charge_number': forms.NumberInput(attrs={'class':'form-control'}),
             'photo': forms.FileInput(attrs={'class':'form-control'}),
          
             'event_county': forms.Select(attrs={'class':'form-select'}),
             'event_location': forms.TextInput(attrs={'class':'form-control'}),
           
        }
        def clean_date(self):
            event_start_date = self.cleaned_data['event_start_date']
            if event_start_date < datetime.date.today():
                raise forms.ValidationError("The date cannot be in the past!")
            return event_start_date

        error_messages={
            'artist_name':{
                'required':('Field is needed')
            }
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'required': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        


class ArtistEditForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields= ('artist_name','event_name','event_start_date','event_end_date','category',
        'event_charge','event_group_charge','event_group_charge_number','event_description',
        'event_offer','event_county','event_location',
        'photo')
        labels = {
                'artist_name': 'Artists Name ',
                'event_name':'Event',
                'event_description':'About The Event',
                'event_charge':'Entry Fee',
                'event_group_charge':'Entry Fee For A Group',
                'event_group_charge_number':'Number Of People Per Group',
                'event_start_date':'Start Datetime',
                'event_county':'County',
                'event_location':'Address',
                'photo':'Event Poster',
             
                'category':'Event Catergory',
                'event_offer':'Offers For This Event',
                'event_end_date':'End Datetime'

        }
        widgets = {
             'artist_name': forms.TextInput(attrs={'class':'form-control'}),
             'event_name': forms.TextInput(attrs={'class':'form-control'}),
             'category': forms.Select(attrs={'class':'form-select'}),
             'event_type': forms.TextInput(attrs={'class':'form-control'}),
             'event_start_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),
            'event_end_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),

             'event_description': forms.CharField(widget=CKEditorWidget()),
             'event_offers': forms.CharField(widget=CKEditorWidget()),
             'event_charge': forms.TextInput(attrs={'class':'form-control'}),
             'event_group_charge': forms.TextInput(attrs={'class':'form-control'}),
             'event_group_charge_number': forms.NumberInput(attrs={'class':'form-control'}),
             'photo': forms.FileInput(attrs={'class':'form-control'}),
            #  'video': forms.FileInput(attrs={'class':'form-control'}),
             'event_county': forms.Select(attrs={'class':'form-select'}),
             'event_location': forms.TextInput(attrs={'class':'form-control'}),
            

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= (
            # 'artist',
            'body',)

        widgets = {
             'artist': forms.Select(attrs={'class':'form-select'}),
            #  'name': forms.TextInput(attrs={'class':'form-control'}),
            #  'email': forms.EmailInput(attrs={'class':'form-select'}),
             'body': forms.CharField(widget=CKEditorWidget()),
        }


class ArtistSearchForm(forms.Form):
    q = forms.CharField()