from django.contrib import admin

# Register your models here.
from .models import Forum
admin.site.register(Forum)

from .models import Forumsub
admin.site.register(Forumsub)

from .models import Page
admin.site.register(Page)

from .models import Comment
admin.site.register(Comment)