from django.urls import path
from  .views import HomeView
from . import views
urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('search/',views.search,name='search'),    
    path('about',views.about,name='about'),  
    path('contact',views.contact,name='contact')
]
