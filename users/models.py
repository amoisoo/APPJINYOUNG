from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
# Create your models here.

# membership
#https://www.366service.com/jp/qa/92220345d1a23ad40554b9865bea69bf

"""

id
email
password

last_login

is_superuser
is_staff


username
name
first_name

"""
def upload_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['users/avatars', str(instance.profile.id)+ '_' +str(instance.nickname)+str(".")+str(ext)])
    #setPath = '/'.join( ['user'  , str(instance.user.id ) + str( instance.nickname ) + str(".") + extension  ])

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('email is must')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)

        return user


import uuid
class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=128, blank=True, null=True )
    username = models.CharField(max_length=128, blank=True, null=True )
    first_name = models.CharField(max_length=128, blank=True, null=True )
    last_name = models.CharField(max_length=128, blank=True, null=True )



    is_active = models.BooleanField(default=True) # No Change
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False, blank=True)



    created         = models.DateTimeField( auto_now_add = True , blank=True, null=True)
    modified        = models.DateTimeField(auto_now=True, blank=True, null=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email




class Profile(models.Model):
    profile = models.OneToOneField( settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE )

    nickname = models.CharField(max_length=128 ,  unique=True )

    #address        = models.CharField( max_length=1024 , blank=True , default= "")
    phone = models.CharField(max_length=32 , blank=True, null=True )
    about = models.TextField(default= "" , blank=True, null=True )


    image = models.ImageField(blank=True, null=True, upload_to=upload_avatar_path)

    created         = models.DateTimeField( auto_now_add = True , blank=True, null=True)
    modified        = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.nickname
















