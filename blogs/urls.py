from django.urls import path
from .views import BlogListView,BlogDetailView,LikeView,TagView
urlpatterns = [
    path('', BlogListView.as_view(), name='blogs'),
    path('<slug>',BlogDetailView.as_view(),name='blog_detail'),
    path('like/<slug>',LikeView,name="like_blog"),
    path('tags/<slug>/',TagView,name='tags')
]
