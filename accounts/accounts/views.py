from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView , PasswordChangeDoneView , PasswordChangeForm
from django.views.generic import CreateView


from django.contrib.auth.forms import UserCreationForm

def index(request):
    html = """

    <h2><a href="../">Application Accountss</a><br/></h2>

    <a href="./time">time</a><br/>
    <a href="./jump">jump</a><br/>
    <a href="./temp">temp</a><br/><br/>

    <a href="./accounts">Accounts</a><br/>
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

class DATA(object):


    def __init__(self):



        self.THEME_NAME = r'accounts/'
        self.THEME_NAME = r'SKOTE/APP_ACCOUNTS/'
        self.THEME_NAME = r'COLORADMIN_ADMIN/APP_ACCOUNTS/'

        self.data_init()



    def data_init(self):
        self.TEM_INDEX       =   self.THEME_NAME + "index.html"
        self.TEM_LOGIN       =   self.THEME_NAME + "login.html"
        self.TEM_LOGOUT     =   self.THEME_NAME + "logout.html"

        self.TEM_PROFILE     =   self.THEME_NAME + "profile.html"


        self.TEM_SIGNIN     =   self.THEME_NAME + "signup.html"
        self.TEM_SIGNIN_DONE     =   self.THEME_NAME + "signup_done.html"


        self.TEM_PROFILE_SETTINGS     =   self.THEME_NAME + "profile_settings.html"
        self.TEM_PASSWORD_CHNAGE     =   self.THEME_NAME + "password_chnage.html"
        self.TEM_PASSWORD_CHNAGE_DONE    =   self.THEME_NAME + "password_chnage_done.html"

DATA = DATA()
#-------------------------------------------------------------------------------
class INDEX_TEMPLATE(TemplateView):
    template_name = DATA.TEM_INDEX



class Login(LoginView):
    """ログインページ"""
    #form_class = LoginForm
    template_name = DATA.TEM_LOGIN
    success_url = reverse_lazy('accounts:index')


class Logout(LogoutView):
    """ログアウトページ"""
    template_name = DATA.TEM_LOGOUT
    success_url = reverse_lazy('accounts:index')


class Account_Profile(TemplateView):
    template_name = DATA.TEM_PROFILE

class Account_Profile_Settins(TemplateView):
    template_name = DATA.TEM_PROFILE_SETTINGS
#---------------------------------------------------------

class Singup_Closed(TemplateView):
    """ログインページ"""
    #form_class = LoginForm
    template_name = DATA.TEM_SIGNIN_DONE



from users.models import User
##from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.conf import settings

class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model() # settings.AUTH_USER_MODEL
        fields = ('email', 'password1', 'password2')



#error
class USER_createView(CreateView):
    #model = Used Form Class

    form_class = SignUpForm  # UserCreationForm
    template_name = DATA.TEM_SIGNIN
    success_url = reverse_lazy('accounts:signin_done')




#---------------------------------------------------------------
# Dont Use.
#---------------------------------------------------------------
def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_passsword(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/signup_done.html', {'ui_form': user_form})

    else:

        user_form = UserCreationForm()
        return render( request ,'accounts/signup.html' , {'ui_form':user_form} )


#---------------------------------------------------------

class PASSWORD_changeView(PasswordChangeView):
    template_name = DATA.TEM_PASSWORD_CHNAGE
    form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:password-change-done')

class PASSWORD_chnageDone(PasswordChangeDoneView):
    template_name = DATA.TEM_PASSWORD_CHNAGE_DONE


#class Account_Reset_Password(TemplateView):
#    template_name = 'accounts/password_reset.html'


#class Account_Reset_Password(TemplateView):
#    template_name = 'accounts/password_reset.html'

