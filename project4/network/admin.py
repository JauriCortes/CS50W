from django.contrib import admin

from .models import Follows, Posts, User

# Register your models here.
admin.site.register(Follows)
admin.site.register(User)
admin.site.register(Posts)
