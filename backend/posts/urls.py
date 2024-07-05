from django.urls import path
from posts.views import ListSearchPosts, RetrieveUpdateDestroyPost, ListPostsUser, ListLikes, ListPostsFollowees, \
    CreateLike, ListCreatePosts, ListFriendsPostsView

from posts.views import ListCreatePosts

urlpatterns = [
    path('social/posts/', ListCreatePosts.as_view(), name='post-list'),
    path('social/posts/?search=<str:search_string>', ListSearchPosts.as_view(), name='post-list-create-search'),
    path('social/posts/<int:post_id>/', RetrieveUpdateDestroyPost.as_view(), name='retrieve-update-destroy-post'),
    path('social/posts/<int:user_id>/', ListPostsUser.as_view(), name='list-posts-user'),
    path("social/posts/following/", ListPostsFollowees.as_view(), name="list-posts-followees"),
    path("social/posts/friends/", ListFriendsPostsView.as_view(), name="friends-posts"),
    path("social/posts/likes/", ListLikes.as_view(), name="list-liked-posts"),
    path("social/posts/toggle-like/<int:post_id>/", CreateLike.as_view(), name="toggle-like")

]