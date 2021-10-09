from django.forms import modelformset_factory
from django import forms
from django.forms import fields
from .models import Event ,Comment
from ckeditor.widgets import CKEditorWidget
from django.forms.fields import DateField

class EventForm(forms.ModelForm):
    class Meta:
        EventFormSet = modelformset_factory(Event, fields=('event_host','speaker_artist'))
        model = Event
        fields =('event_name','category','event_start_date','event_stop_date','event_county','event_location','event_description',
        'event_offer','event_charge','event_group_charge','event_group_charge_number','event_attendees','event_host','speaker_artist','photo')
        labels={
            'event_name': 'Event Name :',
            'category':'Event type :',
            'eventy_county':'County:',
            'event_location':'Event Address :',
            'event_charge':'Event Entry charge :',
            'event_group_charge':'Charge For A Group :',
            'event_group_charge_number':'Number Of Persons Per Group :',
            'event_description':'About Event :',
            'event_offer':'Offers For This Event :',
            'event_host': 'Event Is Hosted By :',
            'event_start_date': 'Start Date Time :',
            'event_stop_date':'Stop Date Time :',
            'photo':'Event Image :',            
            'speaker_artist':'Speaker/Artist For Event  :',
            'event_attendees': 'Number Of Persons To Attend :',

        }
        widgets = {        
             'event_name': forms.TextInput(attrs={'class':'form-control','label':'Artist Name',}),
             'category': forms.Select(attrs={'class':'form-select'}),
             'eventy_county': forms.Select(attrs={'class':'form-select'}),
             'event_location': forms.TextInput(attrs={'class':'form-control'}),
             'event_group_charge': forms.NumberInput(attrs={'class':'form-control'}),
             'event_group_charge_number': forms.NumberInput(attrs={'class':'form-control'}),             
             'event_charge': forms.TextInput(attrs={'class':'form-control'}),
             'event_description': forms.CharField(widget=CKEditorWidget()),
             'event_host': forms.TextInput(attrs={'class':'form-control'}),
             'event_start_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),
             'event_stop_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),            
             'photo': forms.FileInput(attrs={'class':'form-control'}),          
             'speaker_artist': forms.TextInput(attrs={'class':'form-control'}),
             'event_attendees': forms.TextInput(attrs={'class':'form-control'}),
           

        }

class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields =('event_name','event_start_date','event_stop_date','event_county','event_location','event_description',
        'category',
        'event_charge','event_attendees','event_host','speaker_artist','photo')
        labels={
            'event_name': 'Event Name :',
            'category':'Event type :',
            'eventy_county':'County:',
            'event_location':'Event Address :',
            'event_charge':'Event Entry charge :',
            'event_group_charge':'Charge For A Group :',
            'event_group_charge_number':'Number Of Persons Per Group :',
            'event_description':'About Event :',
            'event_offer':'Offers For This Event :',
            'event_host': 'Event Is Hosted By :',
            'event_start_date': 'Event Start Date Time :',
            'event_stop_date':'Event Stop Date Time :',
            'photo':'Event Image :',            
            'speaker_artist':'Speaker/Artist For Event  :',
            'event_attendees': 'Number Of Persons To Attend :',
        }

        widgets = {
             'event_name': forms.TextInput(attrs={'class':'form-control','label':'Artist Name',}),
             'category': forms.Select(attrs={'class':'form-select'}),
             'eventy_county': forms.Select(attrs={'class':'form-select'}),
             'event_location': forms.TextInput(attrs={'class':'form-control'}),
             'event_group_charge': forms.NumberInput(attrs={'class':'form-control'}),
             'event_group_charge_number': forms.NumberInput(attrs={'class':'form-control'}),             
             'event_charge': forms.TextInput(attrs={'class':'form-control'}),
             'event_description': forms.CharField(widget=CKEditorWidget()),
             'event_host': forms.TextInput(attrs={'class':'form-control'}),
             'event_start_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),
             'event_stop_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),            
             'photo': forms.FileInput(attrs={'class':'form-control'}),          
             'speaker_artist': forms.TextInput(attrs={'class':'form-control'}),
             'event_attendees': forms.TextInput(attrs={'class':'form-control'}),
           
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= (
            
            'body',)

        widgets = {
            'body': forms.CharField(widget=CKEditorWidget()),
        }