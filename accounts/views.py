from django.views import generic 
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.urls import reverse_lazy
from accounts.models import Profile 
from django.views.generic import DetailView ,CreateView
from .forms import SignUpForm,EditProfileForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import get_object_or_404
from .forms import ProfilePageForm,EditProfilePageForm
from django.contrib.messages.views import SuccessMessageMixin 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CreateProfilePageView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = Profile
    template_name = 'registration/create_profile_page.html'
    # fields="__all__"
    form_class = ProfilePageForm
    def form_valid(self, form):      
       form.instance.user = self.request.user      
       return super().form_valid(form)
    success_url = reverse_lazy('profile_page')  
    success_message='Profile Created Successfully'

class EditProfilePageView(SuccessMessageMixin,LoginRequiredMixin,generic.UpdateView):
    model= Profile
    template_name = 'registration/edit_profile_page.html'
    slug_url_kwarg = "profile_uuid"
    slug_field = "profile_uuid"
    # fields = '__all__'
    form_class=EditProfilePageForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):      
       form.instance.user = self.request.user      
       return super().form_valid(form)
    success_url = reverse_lazy('profile_page') 

# class ProfileView(LoginRequiredMixin,DetailView):
#     # slug_url_kwarg = "username"
#     # slug_field = "username"

#     def get_slug_field(self):
#         self.user.profile.user.username

#     model = Profile 
#     template_name='registration/user_profile.html'
   
#     # success_url = reverse_lazy('home')   
    
    

    # def get_context_data(self,*args, **kwargs):        
    #     context= super(ProfileView,self).get_context_data(*args, **kwargs)
    #     page_user = get_object_or_404(Profile,slug=self.kwargs['username'])
    #     context['page_user'] = page_user 
    #     return context

class MyProfileView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name='registration/my_profile.html'   
    slug_url_kwarg = "profile_uuid"
    slug_field = "profile_uuid"
    # success_url = reverse_lazy('home')   

    def get_context_data(self, **kwargs):        
        context= super(MyProfileView,self).get_context_data( **kwargs)
        my_profile = get_object_or_404(Profile, profile_uuid =self.kwargs['profile_uuid'])
        context['my_profile'] = my_profile
        return context

class  PasswordsChangeView(SuccessMessageMixin,LoginRequiredMixin,PasswordChangeView):
    form_class = PasswordChangeForm
    # template_name = 'registration/password.html'
    success_url = reverse_lazy('update_profile')

class UserRegisterView(SuccessMessageMixin,LoginRequiredMixin,generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(SuccessMessageMixin,LoginRequiredMixin,generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

