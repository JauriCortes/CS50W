from django.contrib import admin

from .models import Follows, Posts, User, Likes

# Register your models here.
admin.site.register(Follows)
admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Likes)
