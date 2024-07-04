
from rest_framework_simplejwt import views as jwt_views
from user.views import RegistrationView, RegistrationValidationView, UserSearchView
from django.urls import path
from .views import UserListView, ListOfFollowers, ListOfFollowing, FollowUnfollowUser, UserProfileView, MeView


urlpatterns = [
    path('auth/registration/', RegistrationView.as_view()),
    path('auth/registration/validation/', RegistrationValidationView.as_view()),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/?search=<str:search_string>/', UserSearchView.as_view()),
    path('users/<int:user_id>/', UserProfileView.as_view(), name='user-profile'),
    path('social/followers/', ListOfFollowers.as_view(), name='list-followers'),
    path('social/following/', ListOfFollowing.as_view(), name='list-following'),
    path('social/toggle-follow/<int:user_id>/', FollowUnfollowUser.as_view(), name='follow-unfollow-user'),
    path('users/me/', MeView.as_view()),
]