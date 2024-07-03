from django.urls import path, include
from .views import UserListView, ListOfFollowers, ListOfFollowing, FollowUnfollowUser, UserProfileView, MeView


urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/?search=<str:search_string>/', UserListView.as_view(), name='search_users'),
    path('users/<int:user_id>/', UserProfileView.as_view(), name='user-profile'),
    path('social/followers/', ListOfFollowers.as_view(), name='list-followers'),
    path('social/following/', ListOfFollowing.as_view(), name='list-following'),
    path('social/toggle-follow/<int:user_id>/', FollowUnfollowUser.as_view(), name='follow-unfollow-user'),
    path('users/me/', MeView.as_view()),
]
