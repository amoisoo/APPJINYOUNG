from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils.html import mark_safe
from django.utils.text import slugify
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

from django.shortcuts import render, redirect, get_object_or_404
def index(request):
    html = """

    <h2><a href="../">Application Forums</a><br/></h2>

    <a href="./time">time</a><br/>
    <a href="./jump">jump</a><br/>
    <a href="./temp">temp</a><br/><br/>

    <a href="./forum">Forum</a><br/>
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
    return render(request, 'Main/temp.html', object_list)


class INDEX_TEMPLATE(TemplateView):
    template_name = 'COLORADMIN_FRONT/FORUM/index.html'

class CATEGORY_TEMPLATE(TemplateView):
    template_name = 'COLORADMIN_FRONT/FORUM/category.html'

class DETAIL_TEMPLATE(TemplateView):
    template_name = 'COLORADMIN_FRONT/FORUM/detail.html'



class DATA(object):


    def __init__(self):



        self.THEME_NAME = r'COLORADMIN_FRONT/FORUM/'
        self.THEME_NAME = r'COLORADMIN_ADMIN/APP_FORUM/'

        self.data_init()



    def data_init(self):
        self.TEM_FORUM_LIST       =   self.THEME_NAME + "forum_list.html"
        self.TEM_FORUM_CREATE     =   self.THEME_NAME + "forum_create.html"
        self.TEM_FORUM_UPDATE     =   self.THEME_NAME + "forum_update.html"
        self.TEM_FORUM_DELETE     =   self.THEME_NAME + "forum_delete.html"

        self.TEM_CATEGORY_LIST       =   self.THEME_NAME + "category_list.html"
        self.TEM_CATEGORY_DETAIL       =   self.THEME_NAME + "category_detail.html"
        self.TEM_CATEGORY_CREATE     =   self.THEME_NAME + "category_create.html"
        self.TEM_CATEGORY_UPDATE     =   self.THEME_NAME + "category_update.html"
        self.TEM_CATEGORY_DELETE     =   self.THEME_NAME + "category_delete.html"



        self.TEM_PAGE_DETAIL       =   self.THEME_NAME + "page_detail.html"
        self.TEM_PAGE_CREATE     =   self.THEME_NAME + "page_create.html"
        self.TEM_PAGE_UPDATE     =   self.THEME_NAME + "page_update.html"
        self.TEM_PAGE_DELETE     =   self.THEME_NAME + "page_delete.html"

        self.TEM_COMMENT_DETAIL       =   self.THEME_NAME + "comment_detail.html"
        self.TEM_COMMENT_CREATE     =   self.THEME_NAME + "comment_create.html"
        self.TEM_COMMENT_UPDATE     =   self.THEME_NAME + "comment_update.html"
        self.TEM_COMMENT_DELETE     =   self.THEME_NAME + "comment_delete.html"
DATA = DATA()

#-------------------------------------------------------------------------------

from .models import Forum
from .models import Forumsub
from .models import Comment
from .models import Page
#-------------------------------------------------------------------------------
FORUM       = Forum
FORUMSUB    = Forumsub
COMMENT     = Comment
PAGE        = Page
from django import forms

MAIN_FIELDS = [ "id_sort" , "slug" ,  "title", 'subtitle', "note" , 'image', 'code','codelog', 'html', 'css', 'js']

class BASE_FORM_FORUM(forms.ModelForm):

    title = forms.CharField( widget=forms.TextInput(attrs={ "size":20 }) )
    #note = forms.CharField( widget=forms.TextInput )

    class Meta:
        model = Forum
        fields = MAIN_FIELDS




class BASE_FORM_FORUM_CATEGORY(forms.ModelForm):

    title = forms.CharField( widget=forms.TextInput(attrs={ "size":20 }) )
    #note = forms.CharField( widget=forms.TextInput )

    class Meta:
        model = Forumsub
        fields = MAIN_FIELDS + ['parent']
#from .forms import BlogFro




class BASE_FORM_COMMENT_COMMENT(forms.ModelForm):

    title = forms.CharField( widget=forms.TextInput(attrs={ "size":20 }) )
    #note = forms.CharField( widget=forms.TextInput )

    class Meta:
        model = Comment
        fields = MAIN_FIELDS + ['parent']




class BASE_FORM_COMMENT_PAGE(forms.ModelForm):

    title = forms.CharField( widget=forms.TextInput(attrs={ "size":20 }) )
    #note = forms.CharField( widget=forms.TextInput )

    class Meta:
        model = Page
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

#-------------------------------------------------------------------------------


class FORUM_LIstView( ListView):
    model = Forum
    paginate_by = 24
    context_object_name = "forums"
    #login_url = "/time"
    template_name = DATA.TEM_FORUM_LIST


class FORUM_DetailView(ListView):
    model = Forumsub
    paginate_by = 36

    context_object_name = "categories"
    template_name = DATA.TEM_CATEGORY_LIST

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        #context['id_forum'] = self.kwargs.get('pk')
        #context['slug'] = self.kwargs.get('slug')

        FORUM_LIST = Forum.objects.get( slug =self.kwargs.get('slug') )
        context['FORUM'] = FORUM_LIST




        return context

    def get_queryset(self):
        #board = get_object_or_404(Forum , pk=self.kwargs.get('board_id'))
        #self.kwargs['pk'] = board
        #board = Forum.objects.all()
        #board = Forumsub.objects.all()
        #board = Forumsub.objects.filter(id  =1 )



        slug = self.kwargs.get('slug')
        FORUM = Forum.objects.get(slug =slug)

        board = Forumsub.objects.filter(parent_id = FORUM.id  )


        #pk = self.kwargs.get('slug')
        #board = Forumsub.objects.filter(parent_id = pk )

        return board


#-------------------
# Edit / LoginRequiredMixin
#-------------------


class FORUM_UpdateView(LoginRequiredMixin , UpdateView):
    model = Forum

    #fields = ["title" , "note" ]
    form_class = BASE_FORM_FORUM
    template_name = DATA.TEM_FORUM_UPDATE

    login_url = "/login"

    #success_url = reverse_lazy("index")
    def get_success_url(self):


        Forum = self.model.objects.get(slug=self.kwargs.get('slug'))

        print(self.kwargs.get('slug'))
        print(Forum)

        #return reverse_lazy("forum:detail" , kwargs={"pk": blog_pk})
        return reverse_lazy("forum:detail" , kwargs={"slug": Forum.slug})


    def form_valid(self, form):
        #ok
        messages.success( self.request , "Edit OK" )
        form.instance.user = self.request.user

        form.instance.slug =  slugify(self.request.POST['slug'] , allow_unicode = True)


        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Edit NG" )
        return super().form_invalid( form )


class FORUM_DeleteView(LoginRequiredMixin , DeleteView):
    model = Forum
    #template_name = "forum/forum_delete.html"
    template_name = DATA.TEM_FORUM_DELETE

    success_url = reverse_lazy("forum:index")
    login_url = "/login"

    def delete(self, request, *args, **kwargs):
        messages.success( self.request , "Delete OK" )
        return super().delete( request, *args, **kwargs  )


class FORUM_CreateView(LoginRequiredMixin ,  CreateView):
    model = Forum
    form_class = BASE_FORM_FORUM

    login_url = "/login"

    #fields = ["title" , "note" ]
    #success_url = "http://google.com"
    success_url = reverse_lazy("forum:index")
    context_object_name = "object"

    template_name = DATA.TEM_FORUM_CREATE


    def form_valid(self, form):
        #ok

        messages.success( self.request , "Create OK" )
        getTitle = self.request.POST['title']
        form.instance.slug =  slugify(getTitle , allow_unicode = True)
        form.instance.user = self.request.user
        return super().form_valid( form )


    def form_invalid(self, form):
        #error
        messages.error( self.request , "Create NG" )
        return super().form_invalid( form )
#-------------------------------------------------------------------------------
class FORUMSUB_DetailView(DetailView):
    model = Forumsub
    template_name = DATA.TEM_CATEGORY_DETAIL


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(  self.kwargs.get('slug') )
        print(  self.kwargs.get('pk') )

        #pk = self.kwargs.get('pk')
        pk2 = self.kwargs.get('pk')
        #print(pk , pk2 )
        #board = Forumsub.objects.get( id = pk2 )
        print("CATEGORY DETAIL : " , pk2)
        #context['COMMENTS'] = COMMENT.objects.get( parent = 59 )
        context['COMMENTS'] = COMMENT.objects.filter( parent = pk2 )
        context['PAGES'] = PAGE.objects.filter( parent = pk2 )

        #context['object'] = board

        return context





class FORUMSUB_LIstView( ListView):
    model = Forumsub
    paginate_by = 5
    context_object_name = "categories"
    #login_url = "/time"
    template_name = DATA.TEM_CATEGORY_LIST



    def get_queryset(self):
        #board = get_object_or_404(Forum , pk=self.kwargs.get('board_id'))
        #self.kwargs['pk'] = board
        board = Forum.objects.all()
        board = Forumsub.objects.filter(id  =1 )
        board = Forumsub.objects.filter(parent_id = 3 )

        return board



#-------------------
# Edit / LoginRequiredMixin
#-------------------
class FORUMSUB_CreateView(LoginRequiredMixin ,  CreateView):
    model = Forumsub
    form_class = BASE_FORM_FORUM_CATEGORY

    login_url = "/login"

    #fields = ["title" , "note" ]
    #success_url = "http://google.com"
    success_url = reverse_lazy("forum:index")

    template_name = DATA.TEM_CATEGORY_CREATE


    def get_success_url(self):
        #return reverse_lazy("forum:index")

        #return reverse_lazy("forum:detail" , kwargs={"pk": getIDParent})

        FORUM = Forum.objects.get( id = self.kwargs.get('pk') )
        print( '-' * 50 )


        print( '-' * 50 )

        return reverse_lazy("forum:detail" , kwargs={"slug": FORUM.slug })
        #return reverse_lazy("forum:index")



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['id_forum'] = pk

        slug = self.kwargs.get('slug')
        context['slug'] = slug

        return context



    def form_valid(self, form):
        #ok
        messages.success( self.request , "Create OK" )
        getTitle = self.request.POST['title']
        form.instance.slug =  slugify(getTitle , allow_unicode = True)
        form.instance.user = self.request.user
        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Create NG" )
        return super().form_invalid( form )

class FORUMSUB_UpdateView(LoginRequiredMixin , UpdateView):
    model = Forumsub

    #fields = ["title" , "note" ]
    form_class = BASE_FORM_FORUM_CATEGORY
    template_name = DATA.TEM_CATEGORY_UPDATE

    login_url = "/login"

    #success_url = reverse_lazy("index")
    def get_success_url(self):
        print(self.kwargs.get('slug'))
        print(self.kwargs.get('pk'))
        pk = self.kwargs.get('pk')

        Forum = FORUM.objects.get(slug=self.kwargs.get('slug'))


        return reverse_lazy("forum:category_detail" , kwargs={"slug": Forum.slug , 'pk':  pk })



    def form_valid(self, form):
        #ok
        messages.success( self.request , "Edit OK" )
        form.instance.user = self.request.user

        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Edit NG" )
        return super().form_invalid( form )


class FORUMSUB_DeleteView(LoginRequiredMixin , DeleteView):
    model = Forumsub
    #template_name = "forum/forum_delete.html"
    template_name = DATA.TEM_CATEGORY_DELETE

    #success_url = reverse_lazy("forum:index")
    login_url = "/login"

    def get_success_url(self):

        print(self.kwargs.get('slug'))
        print(self.kwargs.get('pk'))


        Forum = FORUM.objects.get(slug=self.kwargs.get('slug'))
        print(Forum.slug)


        return reverse_lazy("forum:detail" , kwargs={"slug": Forum.slug})
        return reverse_lazy("forum:index" , kwargs={})



        print(Forum)
        Forum = FORUM.objects.get(slug=self.kwargs.get('slug'))

        #return reverse_lazy("forum:detail" , kwargs={"pk": blog_pk})
        return reverse_lazy("forum:detail" , kwargs={"slug": Forum.slug})

        pk2 = self.kwargs['pk']
        #pk  = self.request.POST['pk']
        #print('delete : ' , pk, pk2 )
        #book_id     = self.request.POST['parnet_id']

        return reverse_lazy("forum:detail"  , kwargs={"pk": pk2  })

    def delete(self, request, *args, **kwargs):
        messages.success( self.request , "Delete OK" )
        return super().delete( request, *args, **kwargs  )






#-------------------------------------------------------------------------------

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

#-------------------------------------------------------------------------------


class PAGE_LIstView( ListView):
    model = Page
    paginate_by = 5
    #context_object_name = "blogs"
    #login_url = "/time"
    template_name = "page/page_list.html"

class PAGE_DetailView(DetailView):
    model = Page
    template_name = DATA.TEM_PAGE_DETAIL

    context_object_name = "pages"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        self.kwargs['pk']


        context['URL_FORUM'] = self.kwargs['forum']
        context['URL_CATEGORY'] = self.kwargs['category']
        context['URL_PK'] = self.kwargs['category']

        context['PAGE'] = PAGE.objects.get( id = self.kwargs['pk'] )


        return context

#-------------------
# Edit / LoginRequiredMixin
#-------------------
class PAGE_CreateView(LoginRequiredMixin ,  CreateView):
    model = Page
    form_class = BASE_FORM_COMMENT_PAGE

    login_url = "/login"

    #fields = ["title" , "note" ]
    #success_url = "http://google.com"

    template_name = DATA.TEM_PAGE_CREATE

    def get_success_url(self):
        slug = self.request.POST['parent_slug']
        pk = self.request.POST['parent']

        #return reverse_lazy("forum:detail" , kwargs={"pk": blog_pk})
        return reverse_lazy("forum:category_detail" , kwargs={"slug": slug , 'pk': pk })
    def form_valid(self, form):
        #ok
        messages.success( self.request , "Create OK" )
        form.instance.user = self.request.user

        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Create NG" )
        return super().form_invalid( form )

class PAGE_UpdateView(LoginRequiredMixin , UpdateView):
    model = Page

    #fields = ["title" , "note" ]
    form_class = BASE_FORM_COMMENT_PAGE
    template_name = DATA.TEM_PAGE_UPDATE
    login_url = "/login"

    #success_url = reverse_lazy("index")
    def get_success_url(self):
        urlFORUM = self.kwargs['forum']
        urlCATEGORY = self.kwargs['category']
        pk = self.kwargs['pk']

        return reverse_lazy("forum:category_detail", kwargs={"slug": urlFORUM , 'pk' :  urlCATEGORY })


    def form_valid(self, form):
        #ok
        messages.success( self.request , "Edit OK" )
        form.instance.user = self.request.user

        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Edit NG" )
        return super().form_invalid( form )

class PAGE_DeleteView(LoginRequiredMixin , DeleteView):
    model = Page
    #template_name = "page/page_delete.html"
    template_name = DATA.TEM_PAGE_DELETE
    success_url = reverse_lazy("page_index")
    login_url = "/login"

    def get_success_url(self):
        urlFORUM = self.kwargs['forum']
        urlCATEGORY = self.kwargs['category']
        pk = self.kwargs['pk']

        return reverse_lazy("forum:category_detail", kwargs={"slug": urlFORUM , 'pk' :  urlCATEGORY })

    def delete(self, request, *args, **kwargs):
        messages.success( self.request , "Delete OK" )
        return super().delete( request, *args, **kwargs  )






#-------------------------------------------------------------------------------

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

#-------------------------------------------------------------------------------


class COMMENT_LIstView( ListView):
    model = Comment
    paginate_by = 20
    #context_object_name = "blogs"
    #login_url = "/time"
    template_name = "comment/comment_list.html"


class COMMENT_DetailView(DetailView):
    model = Comment
    template_name = DATA.TEM_COMMENT_DETAIL


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        self.kwargs['pk']


        context['URL_FORUM'] = self.kwargs['forum']
        context['URL_CATEGORY'] = self.kwargs['category']
        context['URL_PK'] = self.kwargs['category']

        context['PAGE'] = COMMENT.objects.get( id = self.kwargs['pk'] )


        return context
#-------------------
# Edit / LoginRequiredMixin
#-------------------

class COMMENT_CreateView(LoginRequiredMixin ,  CreateView):
    model = Comment
    form_class = BASE_FORM_COMMENT_COMMENT

    login_url = "/login"

    #fields = ["title" , "note" ]
    #success_url = "http://google.com"

    template_name = DATA.TEM_COMMENT_CREATE

    def get_success_url(self):
        slug = self.request.POST['parent_slug']
        pk = self.request.POST['parent']

        #return reverse_lazy("forum:detail" , kwargs={"pk": blog_pk})
        return reverse_lazy("forum:category_detail" , kwargs={"slug": slug , 'pk': pk })

    def form_valid(self, form):
        #ok
        messages.success( self.request , "Create OK" )
        #getSlugId = self.kwargs.get('parent') #  Not support
        getSlugId = self.request.POST['parent']

        print( "comment create : ", self.request.POST['parent'] )

        form.instance.parent_id =  getSlugId #getSlugId # getActID.id
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
        urlFORUM = self.kwargs['forum']
        urlCATEGORY = self.kwargs['category']
        pk = self.kwargs['pk']

        return reverse_lazy("forum:category_detail", kwargs={"slug": urlFORUM , 'pk' :  urlCATEGORY })


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

    def get_success_url(self):
        urlFORUM = self.kwargs['forum']
        urlCATEGORY = self.kwargs['category']
        pk = self.kwargs['pk']

        return reverse_lazy("forum:category_detail", kwargs={"slug": urlFORUM , 'pk' :  urlCATEGORY })

    def delete(self, request, *args, **kwargs):
        messages.success( self.request , "Delete OK" )
        return super().delete( request, *args, **kwargs  )













