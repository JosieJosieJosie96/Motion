from django.urls import path

from posts.views import ListCreatePosts

urlpatterns = [
    path('social/posts/', ListCreatePosts.as_view()),  # POST: The user can create a new post by sending post data.
    # path('social/posts/'),  # GET: List all the posts of all users in chronological order
    # path('social/posts/?search=<str:search_string>'),  # GET: Search posts of all users and list result
    # path('social/posts/<int:post_id>/'),  # GET: Get a specific post by ID and display all the information
    # path('social/posts/<int:post_id>/'),  # PATCH: Update a specific post (allowed for owner of the post or an admin)
    # path('social/posts/<int:psocialost_id>/'),  # DELETE: Delete a post by ID (allowed for owner of the post or an admin)
    # path('social/posts/user/<int:user_id>/'),  # GET: List all the posts of a specific user in chronological order
    # path('social/posts/following/'),  # GET: List all the posts of followed users in chronological order
    # path('social/posts/friends/'),  # GET: List all the posts of the logged-in user’s friends in chronological order
    # path('social/posts/toggle-like/<int:post_id>/'),  # POST: Like/Unlike a post(should work like a toggle)
    # path('social/posts/likes/')
]
