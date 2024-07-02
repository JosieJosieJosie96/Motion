from django.contrib import admin


class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_friends', 'state']
    search_fields = ['user__username', 'user_friends__username']
    list_filter = ['state']
