from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from django.utils.translation import  gettext as _
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth import get_user_model
User = get_user_model()

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ()}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(models.User, UserAdmin)

class ADMIN_PROFILE(admin.ModelAdmin):
    list_display = ( 'nickname' , 'id' , 'modified', 'created')
    #fields = (  'nickname' )
admin.site.register(models.Profile , ADMIN_PROFILE)

