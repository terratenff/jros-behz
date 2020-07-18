from django.contrib import admin
from .models import Profile, FriendRequest, Comment, Discussion, DiscussionGroup, Event

admin.site.register(Profile)
admin.site.register(FriendRequest)
admin.site.register(Comment)
admin.site.register(Discussion)
admin.site.register(DiscussionGroup)
admin.site.register(Event)
