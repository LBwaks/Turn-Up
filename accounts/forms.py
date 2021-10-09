from django.contrib.auth.forms import PasswordChangeForm,  UserCreationForm ,UserChangeForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import fields
from accounts.models import Profile
# from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.formfields import PhoneNumberField




     
class ProfilePageForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ('type_of_user','phone_number','gender','profile_pic','bio','City','address',
         'facebook_url', 'twitter_url','instagram_url','website_url',
         'type_of_artists','organisation_name','organisation_email',
          'venue_name',
         'venue_email','venue_no')
        
        phone_number:PhoneNumberField(widget=forms.TextInput(attrs={}),required=False)        # type_of_user =forms.CharField(widget=forms.RadioSelect(choices=user_type))
        # type_of_user =forms.ChoiceField(widget=forms.RadioSelect)
      
        gender:forms.ChoiceField(widget = forms.RadioSelect)
        bio: forms.CharField(widget=CKEditorWidget(), required=False)     
        labels ={'bio':'Bio',
        'phone_number':'Phone Number',
       
        'gender':'Gender',
        'type_of_artists':'Type Of Artists',
        'organisation_name':'Event Organization/Company Name',
       
        'profile_pic':'Profile Image',
        'venue_email':'Venue Management Email',
        'venue_name':'Venue Name',
       
        'organisation_email':'Organisation Email',
        'venue_no':'Venue Management Phone Numder',
       
        'City':'Town/City',
        'address':'Your Address',
        'facebook_url':'Facebook Url Link',
        'twitter_url':'Twiter Url Link',
        'instagram_url':'Instagram Url Link',
        'website_url': 'Website Link'



        
        }
        widgets = {
           'type_of_user':forms.Select(),
      
             'type_of_artists': forms.TextInput(attrs={'placeholder':'eg Musician Actor'}),
             'organisation_name': forms.TextInput(attrs={}),
             'organisation_email': forms.EmailInput(attrs={}),             
            #  'organisation_no': forms.TextInput(attrs={}),
            #  'organisation_rep_role':forms.TextInput(attrs={}),
             'profile_pic': forms.FileInput(attrs={}),             
             'venue_email':  forms.EmailInput(attrs={}),
             'venue_name': forms.TextInput(attrs={}),
             'venue_no': forms.TextInput(attrs={}),
            
             'City': forms.TextInput(attrs={}),
             'address': forms.TextInput(attrs={}),
             'facebook_url': forms.URLInput(attrs={}),
             'twitter_url': forms.URLInput(attrs={}),
             'instagram_url': forms.URLInput(attrs={}),
             'website_url': forms.URLInput(attrs={}),
             
            

        }
class EditProfilePageForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ('type_of_user','phone_number','gender','profile_pic','bio','City','address',
         'facebook_url', 'twitter_url','instagram_url','website_url',
         'type_of_artists','organisation_name','organisation_email',
          'venue_name',
         'venue_email')
        
        phone_number:PhoneNumberField(widget=forms.TextInput(attrs={}), 
                       label=("Phone numberff"), required=False)
        type_of_user:forms.ChoiceField(choices=(('artist','Artist'),('venue_rep','Venue Representative'),('event_rep','Event Representative')),widget = forms.RadioSelect,)
      
        gender:forms.ChoiceField(choices = (('male','Male'), ('female', 'Female'),('intersex','Intersex')),widget = forms.RadioSelect,)
        bio: forms.CharField(widget=CKEditorWidget(),label=("Biodd"), required=False)     
        labels ={'bio':'Bio',
        'phone_number':'Phone Number',
        'type_of_user':'User Type',
        'gender':'Gender',
        'type_of_artists':'Type Of Artists',
        'organisation_name':'Event Organization/Company Name',
        # 'organisation_rep_role':'Company/Organization Represantive Role',
        'profile_pic':'Profile Image',
        'venue_email':'Venue Management Email',
        'venue_name':'Venue Name',
       
        'City':'Town/City',
        'address':'Your Address',
        'facebook_url':'Facebook Url Link',
        'twitter_url':'Twiter Url Link',
        'instagram_url':'Instagram Url Link',
        'website_url': 'Website Link'



        
        }
        widgets = {
           
             'type_of_artists': forms.TextInput(attrs={'placeholder':'eg Musician Actor'}),
             'organisation_name': forms.TextInput(attrs={}),
             'organisation_email': forms.EmailInput(attrs={}),
             
            #  'organisation_no': forms.TextInput(attrs={}),
            #  'organisation_rep_role':forms.TextInput(attrs={}),
             'profile_pic': forms.FileInput(attrs={}),             
             'venue_email':  forms.EmailInput(attrs={}),
             'venue_name': forms.TextInput(attrs={}),
             'venue_no': forms.TextInput(attrs={}),
             'venue_rep_role': forms.TextInput(attrs={}),
             'City': forms.TextInput(attrs={}),
             'address': forms.TextInput(attrs={}),
             'facebook_url': forms.URLInput(attrs={}),
             'twitter_url': forms.URLInput(attrs={}),
             'instagram_url': forms.URLInput(attrs={}),
             'website_url': forms.URLInput(attrs={}),
             
            

        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length= 100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length= 100 , widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields =( 'username','first_name','last_name','email','password1','password2')
    def __init__(self,*args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length= 100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length= 100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length= 100 , widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields =( 'username','first_name','last_name','email','password')
        help_texts = {
            'password': None,
            
        }
        
class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields =( 'old_password','new_password1','new_password2')
        labels= {'new_password1':'New Password',
                   'new_password2':'Confirm Password' }
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(max_length= 100,label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','New Password':'New Password'}))
    new_password2= forms.CharField(max_length= 100 ,label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','label':'Confirm Password'}))

    