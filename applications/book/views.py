from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils.html import mark_safe
from django.utils.text import slugify
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView


def index(request):
    html = """

    <h2><a href="../">Application Books</a><br/></h2>

    <a href="./time">time</a><br/>
    <a href="./jump">jump</a><br/>
    <a href="./temp">temp</a><br/><br/>

    <a href="./book">Book</a><br/>
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
    return render(request, 'COLORADMIN_ADMIN/APP_BOOK/temp.html', object_list)


class INDEX_TEMPLATE(TemplateView):
    template_name = 'book/index.html'
    template_name = 'COLORADMIN_ADMIN/APP_BOOK/index.html'



#-------------------------------------------------------------------------------

from .models import Book
from .models import Menu
from .models import Page

#-------------------------------------------------------------------------------

from django import forms

MAIN_FIELDS = [ "id_sort" , "slug" ,  "title", 'subtitle', "note" , "component", "context" , 'code','codelog' , 'html', 'css', 'js' , 'style', 'json', "visible", "layout", "separator",'tag' , 'depth',  'image']


class BASE_FORM_BOOK(forms.ModelForm):

    title = forms.CharField( widget=forms.TextInput(attrs={ "size":20 }) )
    #note = forms.CharField( widget=forms.TextInput )

    class Meta:
        model = Book
        fields = MAIN_FIELDS

#from .forms import BlogFro




class BASE_FORM_MENU(forms.ModelForm):

    title = forms.CharField( widget=forms.TextInput(attrs={ "size":20 }) )
    #note = forms.CharField( widget=forms.TextInput )

    class Meta:
        model = Menu
        fields = MAIN_FIELDS + ['parent']

#from .forms import BlogFro


class BASE_FORM_PAGE(forms.ModelForm):

    title = forms.CharField( widget=forms.TextInput(attrs={ "size":20 }) )
    #note = forms.CharField( widget=forms.TextInput )

    class Meta:
        model = Page
        fields = MAIN_FIELDS + ['parent']



#-------------------------------------------------------------------------------
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

        self.THEME_NAME = r'COLORADMIN_ADMIN/APP_BOOK/'
        self.THEME_NAME = r'SKOTE/APP_BOOK/'


        self.data_init()


    def data_init(self):

        self.TEM_BOOK_LIST       =   self.THEME_NAME + "book_list.html"
        self.TEM_BOOK_DETAIL     =   self.THEME_NAME + "book_detail.html"
        self.TEM_BOOK_CREATE     =   self.THEME_NAME + "book_create.html"
        self.TEM_BOOK_UPDATE     =   self.THEME_NAME + "book_update.html"
        self.TEM_BOOK_DELETE     =   self.THEME_NAME + "book_delete.html"



        self.TEM_Menu_LIST       =   self.THEME_NAME + "menu_list.html"
        self.TEM_Menu_DETAIL     =   self.THEME_NAME + "menu_detail.html"
        self.TEM_Menu_CREATE     =   self.THEME_NAME + "menu_create.html"
        self.TEM_Menu_UPDATE     =   self.THEME_NAME + "menu_update.html"
        self.TEM_Menu_DELETE     =   self.THEME_NAME + "menu_delete.html"


        self.TEM_PAGE_LIST       =   self.THEME_NAME + "page_list.html"
        self.TEM_PAGE_DETAIL     =   self.THEME_NAME + "page_detail.html"
        self.TEM_PAGE_CREATE     =   self.THEME_NAME + "page_create.html"
        self.TEM_PAGE_UPDATE     =   self.THEME_NAME + "page_update.html"
        self.TEM_PAGE_DELETE     =   self.THEME_NAME + "page_delete.html"

DATA = DATA()
#-------------------------------------------------------------------------------


class BOOK_LIstView( ListView):
    model = Book
    paginate_by = 100
    context_object_name = "objects"
    #login_url = "/time"
    template_name =  DATA.TEM_BOOK_LIST

class BOOK_DetailView(DetailView):
    model = Book
    template_name =  DATA.TEM_BOOK_DETAIL
    success_url = reverse_lazy("book:book_index")

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        BOOK_ITEM   = self.model.objects.get( slug =self.kwargs.get('slug') )
        MENULIST    = Menu.objects.filter( parent_id = BOOK_ITEM.id  , depth_id=None )

        context['URL_BOOK'] = slug =self.kwargs.get('slug')

        CommentList = []
        MENU_MAIN_LIST = {}
        for  i in MENULIST:
            commentList = []
            commentList.append( i )
            getList = Menu.objects.filter(depth_id = i.id)
            MENU_MAIN_LIST[str(i.id)] = getList
            #print("MENUTOP : " , i )
            #print(getList)

        context['MENU_LIST'] = MENULIST
        context['MENU_LIST_SUB'] = MENU_MAIN_LIST

        return context

    def get_queryset(self):
        Forum = Book.objects.filter(slug  = self.kwargs.get('slug') )
        #print("detail : " , Forum)



        #board = get_object_or_404(Forum , pk=self.kwargs.get('board_id'))
        #self.kwargs['pk'] = board
        #board = Forum.objects.all()
        #board = Forumsub.objects.all()
        #board = Forumsub.objects.filter(id  =1 )

        #Forum = self.model.objects.get(slug=self.kwargs.get('slug'))
        #Forum = self.model.objects.get(pk=1)


        #Forum = Book.objects.get(slug  = "2020-11-15-140323" )



        #URL_book = self.kwargs.get('book')
        #FORUM = Book.objects.get(slug = '2020-11-15-140323' )

        #FORUM = Book.objects.get(id  = 1 )


        #pk = self.kwargs.get('slug')
        #board = Forumsub.objects.filter(parent_id = pk )

        return Forum

#-------------------
# Edit / LoginRequiredMixin
#-------------------
class BOOK_CreateView(LoginRequiredMixin ,  CreateView):
    model = Book
    form_class = BASE_FORM_BOOK

    login_url = "/login"

    #fields = ["title" , "note" ]
    #success_url = "http://google.com"
    success_url = reverse_lazy("book:index")

    template_name =  DATA.TEM_BOOK_CREATE


    def form_valid(self, form):
        #ok
        messages.success( self.request , "Create OK" )
        form.instance.user = self.request.user

        #getTitle = self.request.POST['title']
        #form.instance.slug = slugify(getTitle, allow_unicode=True)

        try:
            import time
            now = time.ctime()
            slugtime = time.strftime("%Y-%m-%d-%H%M%S", time.strptime(now))
            form.instance.slug = slugify(slugtime, allow_unicode=True)
        except:
            import uuid
            slugtime = uuid.uuid1()
            form.instance.slug = slugify(slugtime, allow_unicode=True)


        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Create NG" )
        return super().form_invalid( form )

class BOOK_UpdateView(LoginRequiredMixin , UpdateView):
    model = Book

    #fields = ["title" , "note" ]
    form_class = BASE_FORM_BOOK
    template_name =  DATA.TEM_BOOK_UPDATE
    login_url = "/login"

    #success_url = reverse_lazy("index")
    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy("book:book_detail" , kwargs={"slug": slug})


    def form_valid(self, form):
        #ok
        messages.success( self.request , "Edit OK" )
        form.instance.slug = slugify(self.request.POST['slug'], allow_unicode=True)

        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Edit NG" )
        return super().form_invalid( form )

class BOOK_DeleteView(LoginRequiredMixin , DeleteView):
    model = Book
    #template_name = "book/book_delete.html"
    template_name =  DATA.TEM_BOOK_DELETE
    success_url = reverse_lazy("book_index")
    login_url = "/login"

    def delete(self, request, *args, **kwargs):
        messages.success( self.request , "Delete OK" )
        return super().delete( request, *args, **kwargs  )












#-------------------------------------------------------------------------------


class MENU_LIstView( ListView):
    model = Menu
    paginate_by = 5
    context_object_name = "objects"
    #login_url = "/time"
    template_name = DATA.TEM_Menu_LIST




class MENU_DetailView(DetailView):
    model = Book
    template_name =  DATA.TEM_Menu_DETAIL
    success_url = reverse_lazy("book:book_index")



    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        BOOK_ITEM   = self.model.objects.get( slug =self.kwargs.get('book') )
        MENU_ITEM   = Menu.objects.get( slug =self.kwargs.get('slug') )

        MENULIST    = Menu.objects.filter( parent_id = BOOK_ITEM.id  , depth_id=None)



        context['URL_BOOK'] = slug =self.kwargs.get('book')
        context['URL_MENU'] = slug =self.kwargs.get('slug')

        CommentList = []
        MENU_MAIN_LIST = {}
        for  i in MENULIST:
            commentList = []
            commentList.append( i )
            getList = Menu.objects.filter(depth_id = i.id)
            MENU_MAIN_LIST[str(i.id)] = getList
            #print("MENUTOP : " , i )
            #print(getList)

        context['MENU_LIST'] = MENULIST
        context['MENU_LIST_SUB'] = MENU_MAIN_LIST
        #---------------------------------------------------------
        PAGELIST    = Page.objects.filter( parent_id = MENU_ITEM.id , depth_id=None )
        context['PAGE_LIST'] = PAGELIST
        PAGELIST    = Page.objects.filter( parent_id = MENU_ITEM.id  )

        PAGE_MAIN_LIST = {}
        for index, i in enumerate(PAGELIST):
            getChildList = Page.objects.filter(depth=str(i.id))

            if (len(getChildList) != 0):
                PAGE_MAIN_LIST[str(i.id)] = getChildList

        context['PAGE_CHILD_LIST'] = PAGE_MAIN_LIST



        return context

    def get_queryset(self):
        book = self.kwargs.get('book')
        slug = self.kwargs.get('slug')

        print('MENU DETAIL VIEW : ' , book , slug )

        Forum = Menu.objects.filter(slug  = self.kwargs.get('slug') )
        print('MENU DETAIL VIEW : ' , Forum )



        #board = get_object_or_404(Forum , pk=self.kwargs.get('board_id'))
        #self.kwargs['pk'] = board
        #board = Forum.objects.all()
        #board = Forumsub.objects.all()
        #board = Forumsub.objects.filter(id  =1 )

        #Forum = self.model.objects.get(slug=self.kwargs.get('slug'))
        #Forum = self.model.objects.get(pk=1)


        #Forum = Book.objects.get(slug  = "2020-11-15-140323" )



        #URL_book = self.kwargs.get('book')
        #FORUM = Book.objects.get(slug = '2020-11-15-140323' )

        #FORUM = Book.objects.get(id  = 1 )


        #pk = self.kwargs.get('slug')
        #board = Forumsub.objects.filter(parent_id = pk )

        return Forum


#-------------------
# Edit / LoginRequiredMixin
#-------------------
class MENU_CreateView(LoginRequiredMixin ,  CreateView):
    model = Menu
    form_class = BASE_FORM_MENU

    login_url = "/login"

    #fields = ["title" , "note" ]
    #success_url = "http://google.com"
    #success_url = reverse_lazy("book:book_index")

    template_name = DATA.TEM_Menu_CREATE

    def get_success_url(self):
        slug_book = self.request.POST['book_slug']

        try:
            slug_menu = self.request.POST['menu_slug']
            print('MENU CREATE get success:', slug_book, slug_menu)

            return reverse_lazy("book:menu_detail", kwargs={"book": slug_book, 'slug': slug_menu})

        except:

            return reverse_lazy("book:book_detail" , kwargs={ 'slug' : slug_book }  )


    def form_valid(self, form):
        #ok
        messages.success( self.request , "Create OK" )
        import time
        now = time.ctime()
        #slugtime = time.strftime("%Y-%m-%d-%H%M%S", time.strptime(now))
        try:
            slugtime = time.strftime("%Y-%m-%d-%H%M%S", time.strptime(now))
        except:
            import uuid
            slugtime = uuid.uuid1()

        form.instance.user = self.request.user

        getSlug = slugify(self.request.POST['title'], allow_unicode=True)
        print("SLUG get:", getSlug)
        try:
            #findSlug = self.model.objects.get(slug=getSlug)
            #findSlug = self.model.objects.all().get(id =146)
            #findSlug = Menu.objects.get(slug=self.kwargs.get('slug'))
            try: # slug : find -> set time
                #findSlug = Menu.objects.get(slug="linear-color-key888")
                findSlug = Menu.objects.get(slug=str(getSlug))

                print("SLUG find:", findSlug, getSlug , type(getSlug))
                print("SLUG find:", findSlug.id, findSlug.slug)
                form.instance.slug = slugify(slugtime, allow_unicode=True)
            except: # slug : no -> create title name
                form.instance.slug = getSlug
        except:
            print('SLUG ERROR')
            form.instance.slug = slugify(slugtime, allow_unicode=True)


        #BOOK_ITEM   = self.model.objects.get( slug =self.kwargs.get('slug') )

        #form.instance.parent_id = 3
        #form.instance.depth = 11


        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Create NG" )
        return super().form_invalid( form )


class MENU_UpdateView(LoginRequiredMixin , UpdateView):
    model = Menu

    #fields = ["title" , "note" ]
    form_class = BASE_FORM_MENU
    template_name = DATA.TEM_Menu_UPDATE
    login_url = "/login"

    #success_url = reverse_lazy("index")
    def get_success_url(self):
        book = self.kwargs.get('book')
        slug = self.kwargs.get('slug')
        print('MENU UPDATE get success:' , book , slug)

        return reverse_lazy("book:menu_detail" , kwargs={"book": book, 'slug' : slug }  )


    def form_valid(self, form):
        #ok
        messages.success( self.request , "Edit OK" )
        book = self.kwargs.get('book')
        slug = self.kwargs.get('slug')

        print('MENU UPDATE :' , book , slug)
        form.instance.slug = slugify(self.request.POST['slug'], allow_unicode=True)

        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Edit NG" )
        return super().form_invalid( form )




class MENU_DeleteView(LoginRequiredMixin , DeleteView):
    model = Menu
    #template_name = "menu/menu_delete.html"
    template_name = DATA.TEM_Menu_DELETE
    #success_url = reverse_lazy("book:book_index")
    login_url = "/login"

    def get_success_url(self):
        slug_book = self.request.POST['book_slug']
        return reverse_lazy("book:book_detail", kwargs={'slug': slug_book})

    def delete(self, request, *args, **kwargs):
        messages.success( self.request , "Delete OK" )
        return super().delete( request, *args, **kwargs  )






#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------


class PAGE_LIstView( ListView):
    model = Page
    paginate_by = 5
    context_object_name = "objects"
    #login_url = "/time"
    template_name = DATA.TEM_PAGE_LIST

class PAGE_DetailView(DetailView):
    model = Page
    template_name = DATA.TEM_PAGE_DETAIL
#-------------------
# Edit / LoginRequiredMixin
#-------------------
class PAGE_CreateView(LoginRequiredMixin ,  CreateView):
    model = Page
    form_class = BASE_FORM_PAGE

    login_url = "/login"

    #fields = ["title" , "note" ]
    #success_url = "http://google.com"

    template_name = DATA.TEM_PAGE_CREATE

    def get_success_url(self):
        URL_BOOK = self.kwargs.get('book')
        URL_SLUG = self.kwargs.get('slug')

        return reverse_lazy("book:menu_detail" , kwargs={"book": URL_BOOK , 'slug' : URL_SLUG })

    def form_valid(self, form):
        #ok
        messages.success( self.request , "Create OK" )
        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Create NG" )
        return super().form_invalid( form )

class PAGE_UpdateView(LoginRequiredMixin , UpdateView):
    model = Page

    #fields = ["title" , "note" ]
    form_class = BASE_FORM_PAGE
    template_name = DATA.TEM_PAGE_UPDATE
    login_url = "/login"

    #success_url = reverse_lazy("index")
    def get_success_url(self):
        URL_BOOK = self.kwargs.get('book')
        URL_SLUG = self.kwargs.get('slug')

        return reverse_lazy("book:menu_detail" , kwargs={"book": URL_BOOK , 'slug' : URL_SLUG })


    def form_valid(self, form):
        #ok
        messages.success( self.request , "Edit OK" )
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
        URL_BOOK = self.kwargs.get('book')
        URL_SLUG = self.kwargs.get('slug')

        return reverse_lazy("book:menu_detail" , kwargs={"book": URL_BOOK , 'slug' : URL_SLUG })

    def delete(self, request, *args, **kwargs):
        messages.success( self.request , "Delete OK" )
        return super().delete( request, *args, **kwargs  )





