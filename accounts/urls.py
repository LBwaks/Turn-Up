from django.urls import path
from .views import UserRegisterView,CreateProfilePageView,MyProfileView,UserEditView,EditProfilePageView,PasswordsChangeView 
from django.contrib.auth import views as auth_views
urlpatterns = [
   
    path('register/', UserRegisterView.as_view(), name='register'),
    path('update_profile/', UserEditView.as_view(), name='update_profile'),
    # path('<slug:username>/profile/',ProfileView.as_view(), name='profile_page'),
    path('<slug:profile_uuid>/my-profile/',MyProfileView.as_view(), name='profile'),
    path('<slug:profile_uuid>/edit_profile_page', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page', CreateProfilePageView.as_view(), name='create_profile'),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change_password.html'))
    
]
