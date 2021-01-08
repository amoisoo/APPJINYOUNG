from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings

project_name = "blog"
app_name = "None"

from users.models import User
class  Blog(models.Model):
    id_sort = models.IntegerField(blank=True, default=99999)

    #parent           = models.ForeignKey(ABS_Shelf_Book, on_delete=models.CASCADE ,blank=True , default= 1 )
    slug            = models.SlugField( unique=True , allow_unicode=True, help_text="one word for title alias" , blank=True, null=True)

    title           = models.CharField( max_length=1024 , blank=True , default= "")
    subtitle        = models.CharField( max_length=1024 , blank=True , default= "")
    note            = models.TextField(                   blank=True , default= "")


    component       = models.CharField( max_length=1024 , blank=True , default= "")
    context         = models.CharField( max_length=1024 , blank=True , default= "")

    code             = models.TextField(default= "" , blank=True , null=True )
    codelog             = models.TextField(default= "" , blank=True , null=True )

    html             = models.TextField(default= "" , blank=True , null=True )
    js             = models.TextField(default= "" , blank=True , null=True )
    css             = models.TextField(default= "" , blank=True , null=True )
    style             = models.TextField(default= "" , blank=True , null=True )
    json             = models.TextField(default= "" , blank=True , null=True )
    #location         = models.CharField( max_length=1024 , blank=True , default= "")


    visible          = models.CharField( max_length=1024 , blank=True , default= "")
    layout           = models.CharField( max_length=1024 , blank=True , default= "")

    separator           = models.CharField( max_length=1024 , blank=True , default= "")
    tag           = models.CharField( max_length=1024 , blank=True , default= "")


    depth           = models.ForeignKey('self', related_name='blog_blog_replies', on_delete=models.SET_NULL   , blank=True , null=True)
    setImagePath = (r'%s/' % (project_name) ) + "common/%Y_%m_%d"
    #image            = ThumbnailImageField(upload_to=(setImagePath ), blank=True, null=True)
    image           = models.ImageField(upload_to=setImagePath, blank=True, null=True)

    views           = models.IntegerField(  default= 0 , blank=True , null=True )
    likes           = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True )

    #user            = models.ForeignKey(get_user_model(), on_delete=models.CASCADE  , blank=True , null=True) # base USER
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE  , blank=True , null=True)

    created         = models.DateTimeField( auto_now_add = True )
    modified        = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ( 'id_sort' , "-id", )
        #abstract = True
        #verboase_name = 'post'
        #verbose_name_plural = 'posts'
        db_table = 'blog_blog'

    def get_absolute_url(self):
        return reverse(  'blog:detail' , args=(self.id,)  )

    def get_url_slug(self):
        return reverse(  'blog:slug' , args=(self.slug ,)  )

    def get_previous(self):
        return self.get_previous_by_created()

    def get_next(self):
        return self.get_next_by_created()

    def summary(self):
        return self.note[:10] + "..."

    def myCustomString(self):

        return "<h2>CustomString</h2>ABCDEFG"

    def __str__(self):
        return self.title



class  Comment(models.Model):
    id_sort = models.IntegerField(blank=True, default=99999)

    parent           = models.ForeignKey(Blog, on_delete=models.CASCADE ,blank=True , null=True , default= 1 , related_name='blog_comment_list' )
    slug            = models.SlugField( unique=True , allow_unicode=True, help_text="one word for title alias" , blank=True, null=True)

    title           = models.CharField( max_length=1024 , blank=True , default= "")
    subtitle        = models.CharField( max_length=1024 , blank=True , default= "")
    note            = models.TextField(                   blank=True , default= "")


    component       = models.CharField( max_length=1024 , blank=True , default= "")
    context         = models.CharField( max_length=1024 , blank=True , default= "")
    code             = models.TextField(default= "" , blank=True , null=True )
    codelog             = models.TextField(default= "" , blank=True , null=True )

    html             = models.TextField(default= "" , blank=True , null=True )
    js             = models.TextField(default= "" , blank=True , null=True )
    css             = models.TextField(default= "" , blank=True , null=True )
    style             = models.TextField(default= "" , blank=True , null=True )
    json             = models.TextField(default= "" , blank=True , null=True )
    #location         = models.CharField( max_length=1024 , blank=True , default= "")


    visible          = models.CharField( max_length=1024 , blank=True , default= "")
    layout           = models.CharField( max_length=1024 , blank=True , default= "")

    separator           = models.CharField( max_length=1024 , blank=True , default= "")
    tag           = models.CharField( max_length=1024 , blank=True , default= "")


    depth           = models.ForeignKey('self', related_name='blog_comment_replies', on_delete=models.SET_NULL   , blank=True , null=True)
    setImagePath = (r'%s/' % (project_name) ) + "comment/%Y_%m_%d"
    #image            = ThumbnailImageField(upload_to=(setImagePath ), blank=True, null=True)
    image           = models.ImageField(upload_to=setImagePath, blank=True, null=True)
    user            = models.ForeignKey(get_user_model(), related_name='blog_comment_user', on_delete=models.CASCADE  , blank=True , null=True)

    created         = models.DateTimeField( auto_now_add = True )
    modified        = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ( 'id_sort' , "id", )
        #abstract = True
        #verboase_name = 'post'
        #verbose_name_plural = 'posts'
        #db_table = 'blog_blog'

    def get_absolute_url(self):
        return reverse(  'forum:detail' , args=(self.id,)  )

    def get_previous(self):
        return self.get_previous_by_created()

    def get_next(self):
        return self.get_next_by_created()

    def summary(self):
        return self.note[:10] + "..."

    def myCustomString(self):

        return "<h2>CustomString</h2>ABCDEFG"

    def __str__(self):
        return self.title


#https://www.366service.com/jp/qa/33ee1abe3eb330c3ae933d1f0ca18123