from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

project_name = "book"
app_name = ""
class  Book(models.Model):
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


    depth           = models.ForeignKey('self', related_name='book_book_replies', on_delete=models.SET_NULL   , blank=True , null=True)
    setImagePath = (r'%s/' % (project_name) ) + "book/%Y_%m_%d"
    #image            = ThumbnailImageField(upload_to=(setImagePath ), blank=True, null=True)
    image           = models.ImageField(upload_to=setImagePath, blank=True, null=True)
    user            = models.ForeignKey(get_user_model(), on_delete=models.CASCADE  , blank=True , null=True)

    created         = models.DateTimeField( auto_now_add = True )
    modified        = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ( 'id_sort' , "-id", )
        #abstract = True
        #verboase_name = 'post'
        #verbose_name_plural = 'posts'
        #db_table = 'blog_blog'

    def get_absolute_url(self):
        return reverse(  'book:detail' , args=(self.id,)  )

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

class  Menu(models.Model):
    id_sort = models.IntegerField(blank=True, default=99999)

    parent           = models.ForeignKey(Book, on_delete=models.CASCADE ,blank=True , default= 1 )
    slug            = models.SlugField( unique=False , allow_unicode=True, help_text="one word for title alias" , blank=True, null=True)

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


    depth           = models.ForeignKey('self', related_name='book_menu_replies', on_delete=models.SET_NULL   , blank=True , null=True)
    setImagePath = (r'%s/' % (project_name) ) + "menu/%Y_%m_%d"
    #image            = ThumbnailImageField(upload_to=(setImagePath ), blank=True, null=True)
    image           = models.ImageField(upload_to=setImagePath, blank=True, null=True)
    user            = models.ForeignKey(get_user_model(), on_delete=models.CASCADE  , blank=True , null=True)

    created         = models.DateTimeField( auto_now_add = True )
    modified        = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ( 'id_sort' , "id", )
        #abstract = True
        #verboase_name = 'post'
        #verbose_name_plural = 'posts'
        #db_table = 'blog_blog'

    def get_absolute_url(self):
        return reverse(  'book:detail' , args=(self.id,)  )

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


class  Page(models.Model):
    id_sort = models.IntegerField(blank=True, default=99999)

    parent           = models.ForeignKey(Menu, on_delete=models.CASCADE ,blank=True , default= 1 )
    slug            = models.SlugField( unique=False , allow_unicode=True, help_text="one word for title alias" , blank=True, null=True)

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


    depth           = models.ForeignKey('self', related_name='book_page_replies', on_delete=models.SET_NULL   , blank=True , null=True)
    setImagePath = (r'%s/' % (project_name) ) + "menu/%Y_%m_%d"
    #image            = ThumbnailImageField(upload_to=(setImagePath ), blank=True, null=True)
    image           = models.ImageField(upload_to=setImagePath, blank=True, null=True)
    user            = models.ForeignKey(get_user_model(), related_name='book_page_user', on_delete=models.CASCADE  , blank=True , null=True)

    created         = models.DateTimeField( auto_now_add = True )
    modified        = models.DateTimeField( auto_now=True)


    class Meta:
        ordering = ( 'id_sort' , "id", )
        #abstract = True
        #verboase_name = 'post'
        #verbose_name_plural = 'posts'
        #db_table = 'blog_blog'

    def get_absolute_url(self):
        return reverse(  'book:detail' , args=(self.id,)  )

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