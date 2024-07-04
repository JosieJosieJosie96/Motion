from django.urls import path

from Comment.views import GetComments

urlpatterns = [
    path('social/comments/<int:post_id>/', GetComments.as_view()),
]