from django.contrib import admin

# Register your models here.
from .models import Book
admin.site.register(Book)

from .models import Menu
admin.site.register(Menu)

from .models import Page
admin.site.register(Page)

