from django.contrib import admin

# Register your models here.
from .models import Blog
admin.site.register(Blog)




from .models import Comment
admin.site.register(Comment)
