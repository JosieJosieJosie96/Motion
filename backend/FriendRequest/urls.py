from django.urls import path

from FriendRequest.views import SendFriendRequestView, UpdateGetDeleteFriendRequestView, ListAllFriendsView

urlpatterns = [
    path('social/friends/<int:user_id>/', SendFriendRequestView.as_view()),
    path('social/friends/requests/<int:pk>/', UpdateGetDeleteFriendRequestView.as_view()),
    path('social/friends/', ListAllFriendsView.as_view()),
]
