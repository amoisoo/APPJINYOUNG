from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.
from django.utils.text import slugify
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView


def index(request):
    html = """

    <h2><a href="../">Application Blogs</a><br/></h2>

    <a href="./time">time</a><br/>
    <a href="./jump">jump</a><br/>
    <a href="./temp">temp</a><br/><br/>

    <a href="./blog">Blog</a><br/>
    """
    return HttpResponse(mark_safe(html))


def time(request):
    import datetime
    now = datetime.datetime.now()
    html = "<html><body>지금 POST 시간은 <br>%s.</body></html>" % now
    return HttpResponse(html)


def jump(request):
    return HttpResponseRedirect("http://google.com/")


def temp(request):
    object_list = {"title": "title", "note": "note", "detail": mark_safe("datail<b>detail</b>detail")}
    # object_list = PostModel.objects.all()
    return render(request, 'COLORADMIN_FRONT/index.html', object_list)



class INDEX_TEMPLATE(TemplateView):
    template_name = 'blog/index.html'



#-------------------------------------------------------------------------------

from .models import Blog
from .models import Comment
#-------------------------------------------------------------------------------

from django import forms
MAIN_FIELDS = [ "id_sort" , "slug" ,  "title", 'subtitle', "note" , "component", "context" , 'code','codelog' , 'html', 'css', 'js' , 'style', 'json', "visible", "layout", "separator",'tag' , 'depth',  'image']

class BASE_FORM_BLOG(forms.ModelForm):

    title = forms.CharField( widget=forms.TextInput(attrs={ "size":20 }) )
    #note = forms.CharField( widget=forms.TextInput )

    class Meta:
        model = Blog
        fields = MAIN_FIELDS

#from .forms import BlogFro

class BASE_FORM_COMMENT_COMMENT(forms.ModelForm):

    title = forms.CharField( widget=forms.TextInput(attrs={ "size":20 }) )
    #note = forms.CharField( widget=forms.TextInput )

    class Meta:
        model = Comment
        fields = MAIN_FIELDS + ['parent']


#-------------------------------------------------------------------------------

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView




class DATA(object):


    def __init__(self):



        self.THEME_NAME = r'blog/'
        self.THEME_NAME = r'COLORADMIN_FRONT/BLOG/'
        self.THEME_NAME = r'COLORADMIN_ADMIN/APP_BLOG/'
        self.THEME_NAME = r'SKOTE/APP_BLOG/'

        self.data_init()



    def data_init(self):
        self.TEM_BLOG_LIST       =   self.THEME_NAME + "blog_list.html"
        self.TEM_BLOG_DETAIL     =   self.THEME_NAME + "blog_detail.html"
        self.TEM_BLOG_CREATE     =   self.THEME_NAME + "blog_create.html"
        self.TEM_BLOG_UPDATE     =   self.THEME_NAME + "blog_update.html"
        self.TEM_BLOG_DELETE     =   self.THEME_NAME + "blog_delete.html"
        self.TEM_BLOG_CONTACT    =   self.THEME_NAME + "contact.html"
        self.TEM_BLOG_SEARCH     =   self.THEME_NAME + "blog_search.html"

        self.TEM_BLOG_ARCHIVE     =   self.THEME_NAME + "blog_archive.html"
        self.TEM_BLOG_ARCHIVE_Y     =   self.THEME_NAME + "blog_archive_year.html"
        self.TEM_BLOG_ARCHIVE_M     =   self.THEME_NAME + "blog_archive_month.html"
        self.TEM_BLOG_ARCHIVE_D     =   self.THEME_NAME + "blog_archive_day.html"

        self.TEM_COMMENT_DETAIL       =   self.THEME_NAME + "comment_detail.html"
        self.TEM_COMMENT_CREATE     =   self.THEME_NAME + "comment_create.html"
        self.TEM_COMMENT_UPDATE     =   self.THEME_NAME + "comment_update.html"
        self.TEM_COMMENT_DELETE     =   self.THEME_NAME + "comment_delete.html"

DATA = DATA()


class BLOG_LIstView( ListView):
    model = Blog
    paginate_by = 10
    context_object_name = "blogs"
    #login_url = "/time"
    template_name = DATA.TEM_BLOG_LIST

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        BLOG_LIST = Blog.objects.all()

        blogViews = 0
        allCommentCount = 1

        for i in BLOG_LIST:
            blogViews += i.views
            allCommentCount += len(i.blog_comment_list.all())



        context['BLOG_LIST'] = BLOG_LIST
        context['BLOG_LIST_VIEWS'] = blogViews
        context['BLOG_COMMENT_COUNT'] = allCommentCount
        return context




class BLOG_DetailView(DetailView):
    model = Blog
    template_name = DATA.TEM_BLOG_DETAIL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        BLOG_LIST = self.model.objects.all()

        #BOOK_ITEM   = self.model.objects.get( slug =self.kwargs.get('slug') )
        if (self.kwargs.get('pk') ):
            blogItem =  self.model.objects.get( id =self.kwargs.get('pk') )
            #context['comments'] = Comment.objects.filter( parent  = 3  )
            context['comments'] = Comment.objects.filter( parent  = self.kwargs.get('pk')  )

        else:
            blogItem =  self.model.objects.get( slug =self.kwargs.get('slug') )
            context['comments'] = Comment.objects.filter(   parent = blogItem.id  )

        context['likes_list'] = blogItem.likes.all()



        blogItem.views = blogItem.views + 1
        blogItem.save()

        #context['comments'] = context['post'].comment_set.filter(comment_id__isnull=True)

        Comment

        return context

#-------------------
# Edit / LoginRequiredMixin
#-------------------
class BLOG_CreateView(LoginRequiredMixin ,  CreateView):
    model = Blog
    form_class = BASE_FORM_BLOG

    login_url = "/login"

    #fields = ["title" , "note" ]
    #success_url = "http://google.com"
    success_url = reverse_lazy("blog:index")

    template_name = DATA.TEM_BLOG_CREATE


    def form_valid(self, form):
        #ok
        messages.success( self.request , "Create OK" )
        getTitle = self.request.POST['title']
        #form.instance.slug =  slugify(getTitle , allow_unicode = True)

        #form.instance.slug =  slugify(str(getTitle) , allow_unicode = True)
        try:
            import time
            now = time.ctime()
            slugtime = time.strftime("%Y-%m-%d-%H%M%S", time.strptime(now))
            form.instance.slug = slugify(slugtime, allow_unicode=True)
            form.instance.user = self.request.user
        except:
            import uuid
            slugtime = uuid.uuid1()
            form.instance.slug = slugify(slugtime, allow_unicode=True)

        form.instance.user = self.request.user
        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Create NG" )
        return super().form_invalid( form )



class BLOG_UpdateView(LoginRequiredMixin , UpdateView):
    model = Blog

    #fields = ["title" , "note" ]
    form_class = BASE_FORM_BLOG
    template_name = DATA.TEM_BLOG_UPDATE
    login_url = "/login"

    #success_url = reverse_lazy("index")
    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        return reverse_lazy("blog:detail" , kwargs={"pk": blog_pk})


    def form_valid(self, form):
        #ok
        messages.success( self.request , "Edit OK" )
        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Edit NG" )
        return super().form_invalid( form )

class BLOG_DeleteView(LoginRequiredMixin , DeleteView):
    model = Blog
    #template_name = "blog/blog_delete.html"
    template_name = DATA.TEM_BLOG_DELETE
    success_url = reverse_lazy("blog:index")
    login_url = "/login"

    def delete(self, request, *args, **kwargs):
        messages.success( self.request , "Delete OK" )
        return super().delete( request, *args, **kwargs  )



#-------------------------------------------------------------------------------
from django.views.generic.dates import ArchiveIndexView, YearArchiveView , MonthArchiveView, DayArchiveView




class BLOG_AV( ArchiveIndexView):
    model = Blog
    date_field = "modified"
    #context_object_name = "blogs"
    #login_url = "/time"
    template_name = DATA.TEM_BLOG_ARCHIVE



class BLOG_AV_YEAR( YearArchiveView):
    model = Blog
    date_field = "modified"
    template_name = DATA.TEM_BLOG_ARCHIVE_Y


class BLOG_AV_MONTH( MonthArchiveView):
    model = Blog
    date_field = "modified"
    template_name = DATA.TEM_BLOG_ARCHIVE_M


class BLOG_AV_DAY( DayArchiveView):
    model = Blog
    date_field = "modified"
    template_name = DATA.TEM_BLOG_ARCHIVE_D


#-------------------------------------------------------------------------------

class Blog_contact(TemplateView):
    template_name = DATA.TEM_BLOG_CONTACT

#-------------------------------------------------------------------------------

from django import forms
from django.views.generic import FormView
from django.db.models import Q



class BASE_FORM_BLOG_search(forms.Form):
    search_word = forms.CharField(label="Search...")



class Blog_search(FormView):
    form_class = BASE_FORM_BLOG_search
    template_name = DATA.TEM_BLOG_SEARCH

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']

        getList = Blog.objects.filter(
              Q(title__icontains    =searchWord)
            | Q(subtitle__icontains =searchWord)
            | Q(note__icontains     =searchWord)
            | Q(slug__icontains     =searchWord)
        ).distinct()

        context = {}
        context['ui_form'] = form
        context['search_term'] = searchWord
        context['object_list'] = getList
        return render( self.request , self.template_name , context )


#-------------------------------------------------------------------------------


class COMMENT_CreateView(LoginRequiredMixin ,  CreateView):
    model = Comment
    form_class = BASE_FORM_COMMENT_COMMENT

    login_url = "/login"

    #fields = ["title" , "note" ]
    #success_url = "http://google.com"

    template_name = DATA.TEM_COMMENT_CREATE

    def get_success_url(self):
        pk = self.request.POST['parent']
        #pk = self.request.POST['parent']
        #pk = self.kwargs['pk']

        #return reverse_lazy("forum:detail" , kwargs={"pk": blog_pk})
        return reverse_lazy("blog:detail" , kwargs={ 'pk': pk })

    def form_valid(self, form):
        #ok
        messages.success( self.request , "Create OK" )
        #getSlugId = self.kwargs.get('parent') #  Not support

        #getSlugId = self.request.POST['parent']
        #print( "comment create : ", self.request.POST['parent'] )
        #form.instance.parent_id =  getSlugId #getSlugId # getActID.id

        form.instance.user = self.request.user

        #form.instance.depth_id = self.request.POST.get('depth_id')

        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Create NG" )
        return super().form_invalid( form )



class COMMENT_UpdateView(LoginRequiredMixin , UpdateView):
    model = Comment

    #fields = ["title" , "note" ]
    form_class = BASE_FORM_COMMENT_COMMENT
    template_name = DATA.TEM_COMMENT_UPDATE
    login_url = "/login"

    #success_url = reverse_lazy("index")
    def get_success_url(self):
        #urlFORUM = self.kwargs['forum']
        #urlCATEGORY = self.kwargs['category']
        getParent = self.request.POST['parent']

        pk = self.kwargs['pk']

        return reverse_lazy("blog:detail", kwargs={'pk' :  getParent })


    def form_valid(self, form):
        #ok
        messages.success( self.request , "Edit OK" )
        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Edit NG" )
        return super().form_invalid( form )


class COMMENT_DeleteView(LoginRequiredMixin , DeleteView):
    model = Comment
    #template_name = "comment/comment_delete.html"
    template_name = DATA.TEM_COMMENT_DELETE
    login_url = "/login"
    success_url = reverse_lazy("index")

    def get_success_url(self):
        getParent = self.request.POST['parent']

        #urlCATEGORY = self.kwargs['category']
        pk = self.kwargs['pk']

        print("DIRECT", getParent , pk)
        return reverse_lazy("blog:detail", kwargs={ 'pk' :  getParent })

    def delete(self, request, *args, **kwargs):
        messages.success( self.request , "Delete OK" )
        return super().delete( request, *args, **kwargs  )











































