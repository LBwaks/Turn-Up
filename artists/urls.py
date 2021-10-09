from django.urls import path
from . import views
from .views import ArtistDetailView, ArtistView,LikeView,AddArtistView, UpdateArtistView,DeleteArtistView,CategoryView,UserView
# ,artist_search

urlpatterns = [
    path('', ArtistView.as_view(),name='artists'),
    path('<slug>',ArtistDetailView.as_view(),name='artist_detail'),
    path('add_artists/',AddArtistView.as_view(), name="add_artists"),
    path('edit/<slug>',UpdateArtistView.as_view(),name="update_artist"),
    path('<slug>/delete',DeleteArtistView.as_view(),name="delete_artist"),
    path('like/',LikeView, name="like_artist"),
    # path('search/',artist_search,name='search'), 
    path('category/<slug>/',CategoryView,name="artist_category"),
    path('user/<str:username>/',UserView,name="artist_user")
    # path('category/<str:slug>/',CategoryListView.as_view(),name="category")


]
 
