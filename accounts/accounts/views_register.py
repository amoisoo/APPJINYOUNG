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


    <a href="./accounts">Register</a><br/>
    """
    return HttpResponse(mark_safe(html))







class Singup_Closed(TemplateView):
    """ログインページ"""
    #form_class = LoginForm
    template_name = 'accounts/signup_done.html'


#---------------------------------------------------------
class USER_createView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:signin_done')


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
