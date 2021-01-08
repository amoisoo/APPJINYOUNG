from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    html = """

    <h2><a href="../">Application Userss</a><br/></h2>

    <a href="./time">time</a><br/>
    <a href="./jump">jump</a><br/>
    <a href="./temp">temp</a><br/><br/>

    <a href="./users">Users</a><br/>
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



#-------------------------------------------------------------------------------

from .models import Profile
#-------------------------------------------------------------------------------

from django import forms

class BASE_FORM_PROFILE(forms.ModelForm):

    nickname = forms.CharField( widget=forms.TextInput(attrs={ "size":20 }) )
    #note = forms.CharField( widget=forms.TextInput )

    class Meta:
        model = Profile
        fields = ["nickname", 'phone', 'about' ,  "image"]

#from .forms import BlogFro


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
from django.views.generic import TemplateView, View


class PROFILE_LIstView( ListView):
    model = Profile
    paginate_by = 5
    context_object_name = "objects"
    #login_url = "/time"
    template_name = "SKOTE/APP_USERS/profile_list.html"


class PROFILE(TemplateView):
    template_name = "SKOTE/APP_USERS/profile_detail.html"




#-------------------
# Edit / LoginRequiredMixin
#-------------------

class PROFILE_CreateView(LoginRequiredMixin ,  CreateView):
    model = Profile
    form_class = BASE_FORM_PROFILE

    login_url = "/login"

    #fields = ["title" , "note" ]
    #success_url = "http://google.com"
    success_url = reverse_lazy("users:profile_index")

    template_name = "SKOTE/APP_USERS/profile_create.html"


    def form_valid(self, form):
        #ok
        messages.success( self.request , "Create OK" )

        form.instance.profile = self.request.user

        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Create NG" )
        return super().form_invalid( form )



class PROFILE_UpdateView(LoginRequiredMixin , UpdateView):
    model = Profile

    #fields = ["title" , "note" ]
    form_class = BASE_FORM_PROFILE
    template_name = "SKOTE/APP_USERS/profile_update.html"

    login_url = "/login"

    #success_url = reverse_lazy("index")
    def get_success_url(self):
        #blog_pk = self.kwargs['pk']
        success_url = reverse_lazy("users:profile_index")

        return success_url
    def form_valid(self, form):
        #ok
        messages.success( self.request , "Edit OK" )
        return super().form_valid( form )

    def form_invalid(self, form):
        #error
        messages.error( self.request , "Edit NG" )
        return super().form_invalid( form )

class PROFILE_DeleteView(LoginRequiredMixin , DeleteView):
    model = Profile
    #template_name = "profile/profile_delete.html"
    template_name = "SKOTE/APP_USERS/profile_delete.html"

    login_url = "/login"

    def get_success_url(self):
        #blog_pk = self.kwargs['pk']
        success_url = reverse_lazy("users:profile_index")

        return success_url

    def delete(self, request, *args, **kwargs):
        messages.success( self.request , "Delete OK" )
        return super().delete( request, *args, **kwargs  )

