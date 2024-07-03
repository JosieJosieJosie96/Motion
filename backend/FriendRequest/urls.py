from django.urls import path
from .views import FriendRequestListView
from .views import FriendListView

urlpatterns = [
    path('social/friends/request/<int:user_id>/', FriendRequestListView.as_view(), name='friend-request-send'),
    path('social/friends/request/<int:pk>/', FriendRequestListView.as_view(), name='friend-request-details'),
    path('social/friends/', FriendListView.as_view(), name='friend-list-accepted'),
 ]
