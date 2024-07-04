from django.urls import path
from posts.views import ListSearchPosts, RetrieveUpdateDestroyPost, ListPostsUser, ListLikes, ListPostsFollowees, \
    CreateLike, ListCreatePosts, ListFriendsPostsView


urlpatterns = [
    path('', ListCreatePosts.as_view(), name='post-list'),
    path('?search=<str:search_string>', ListSearchPosts.as_view(), name='post-list-create-search'),
    path('<int:post_id>/', RetrieveUpdateDestroyPost.as_view(), name='retrieve-update-destroy-post'),
    path('<int:user_id>/', ListPostsUser.as_view(), name='list-posts-user'),
    path("following/", ListPostsFollowees.as_view(), name="list-posts-followees"),
    path("friends/", ListFriendsPostsView.as_view(), name="friends-posts"),
    path("likes/", ListLikes.as_view(), name="list-liked-posts"),
    path("toggle-like/<int:post_id>/", CreateLike.as_view(), name="toggle-like")

]
