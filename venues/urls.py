from artists.models import Category
from artists.views import LikeView
from django.urls import path
from .views import VenueListView,VenueDetailView,AddVenueView,LikeView,VenueUpdateView,VenueDeleteView,CategoryView,UserView

urlpatterns = [
    path('', VenueListView.as_view(), name='venues'),
    path('<slug>',VenueDetailView.as_view(),name="venue_details"),
    path('add_venues/',AddVenueView.as_view(),name='add_venues'),
    path('like/<slug>',LikeView,name="like_venue"),
    path('edit/<slug>',VenueUpdateView.as_view(),name="update_venue"),
    path('delete/<slug>',VenueDeleteView.as_view(),name="delete_venue"),
    path('category/<slug>/',CategoryView, name="category"),
    path('user/<str:username>/',UserView,name="venue_user")



]
