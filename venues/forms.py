from django import forms
from .models import Venue,Commenting
# ,Comments
from ckeditor.widgets import CKEditorWidget

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('venue_name','venue_county','venue_location','event_name',
        'event_start_date','event_stop_date',
        'category','event_description','event_offer','speaker_artist','event_fee','event_group_charge','event_group_charge_number','photo',
        )

        labels={
            'venue_name':'Name :',
            'event_name':'Event :',
            'speaker_artist':'Speakers/Artists :',
            'event_fee':'Event Charges :',
            'event_group_charge':'Group Charges :',
            'event_group_charge_number':'Number Of Persons Per Group :',
            'category':'Event Type :',            
            'event_description':'About The Event :',
            'event_offer':'Venue Event Offers :',
            'event_start_date':'Event Start Date :',
            'event_stop_date':'Event Stop Date :',
            'photo':'Venue Poster Image :',           
            'venue_county':'Venue County :',
            'venue_location':'Venue Address :',
           


        }

        widgets = {
             'venue_name': forms.TextInput(attrs={'class':'form-control','label':'Artist Name',}),
             'category': forms.Select(attrs={'class':'form-select'}),
             'event_name': forms.TextInput(attrs={'class':'form-control'}),
             'speaker_artist': forms.TextInput(attrs={'class':'form-control'}),
             'event_fee': forms.TextInput(attrs={'class':'form-control'}),
             'event_group_charge': forms.TextInput(attrs={'class':'form-control'}),
             'event_group_charge_number': forms.TextInput(attrs={'class':'form-control'}),            
             'event_description': forms.CharField(widget=CKEditorWidget()),
             'event_offer': forms.CharField(widget=CKEditorWidget()),
             'event_start_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),
             'event_stop_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),
             'photo': forms.FileInput(attrs={'class':'form-control'}),            
             'venue_county': forms.Select(attrs={'class':'form-select'}),
             'venue_location': forms.TextInput(attrs={'class':'form-control'}),
          
        }

class VenueEditForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('venue_name','venue_county','venue_location','event_name',
        'event_start_date','event_stop_date',
        'category','event_description','event_offer','speaker_artist','event_fee','event_group_charge','event_group_charge_number','photo',
        )

        labels={
            'venue_name':'Name :',
            'event_name':'Event :',
            'speaker_artist':'Speakers/Artists :',
            'event_fee':'Event Charges :',
            'event_group_charge':'Group Charges :',
            'event_group_charge_number':'Number Of Persons Per Group :',
            'category':'Event Type :',            
            'event_description':'About The Event :',
            'event_offer':'Venue Event Offers :',
            'event_start_date':'Event Start Date :',
            'event_stop_date':'Event Stop Date :',
            'photo':'Venue Poster Image :',           
            'venue_county':'Venue County :',
            'venue_location':'Venue Address :',
           


        }

        widgets = {
             'venue_name': forms.TextInput(attrs={'class':'form-control','label':'Artist Name',}),
             'category': forms.Select(attrs={'class':'form-select'}),
             'event_name': forms.TextInput(attrs={'class':'form-control'}),
             'speaker_artist': forms.TextInput(attrs={'class':'form-control'}),
             'event_fee': forms.TextInput(attrs={'class':'form-control'}),
             'event_group_charge': forms.TextInput(attrs={'class':'form-control'}),
             'event_group_charge_number': forms.TextInput(attrs={'class':'form-control'}),            
             'event_description': forms.CharField(widget=CKEditorWidget()),
             'event_offer': forms.CharField(widget=CKEditorWidget()),
             'event_start_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),
             'event_stop_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),
             'photo': forms.FileInput(attrs={'class':'form-control'}),            
             'venue_county': forms.Select(attrs={'class':'form-select'}),
             'venue_location': forms.TextInput(attrs={'class':'form-control'}),
          
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model= Commenting
        fields =("body",)

        widgets={ 

            'body': forms.CharField(widget=CKEditorWidget()),
            
        }