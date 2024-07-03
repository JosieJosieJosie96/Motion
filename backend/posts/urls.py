from django.urls import path
from posts.views import ListCreatePosts, RetrieveUpdateDestroyPost

urlpatterns = [
    path('social/posts/', ListCreatePosts.as_view(), name='post-list'),  # POST & GET: List all posts / create post
    path('social/posts/<int:post_id>/', RetrieveUpdateDestroyPost.as_view(), name='specific-post'),  # GET, PATCH, DELETE: Specific post

]