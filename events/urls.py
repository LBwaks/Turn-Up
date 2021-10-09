from django.urls import path
from .views import AddEventView, EventView,EventDetailView,LikeView,UpdateEventView,DeleteEventView,CategoryView,UserView


urlpatterns = [
    path('', EventView.as_view(), name='events'),
    path('<slug>',EventDetailView.as_view(),name='event_details'),
    path('add_events/',AddEventView.as_view(),name="add_events"),
    path('edit/<slug>',UpdateEventView.as_view(),name="edit_event"),
    path('like/<slug>',LikeView, name="like_event"),
    path('<slug>/delete',DeleteEventView.as_view(),name="delete_event"),
    path('category/<slug>',CategoryView,name="event_category"),
    path('user/<username>/',UserView,name="event_user")
]
