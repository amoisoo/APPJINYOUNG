from django.urls import path

from . import views
from accounts.accounts import views_register

app_name = "accounts"


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.INDEX_TEMPLATE.as_view(), name='index'),

    path(r"time", views.time),
    path(r"jump", views.jump),
    path(r"temp", views.temp),
]


urlpatterns += [
    path("login/",  views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),

]

urlpatterns += [

    path("profile/", views.Account_Profile.as_view(), name="profile"),
]


urlpatterns += [
    path("password-change/", views.PASSWORD_changeView.as_view(), name="password-change"),
    path("password-change-done/", views.PASSWORD_chnageDone.as_view(), name="password-change-done"),
]


urlpatterns += [

    path("signin/", views.USER_createView.as_view(), name="signin"),
    #path("signin/", views.register, name="signin"),
    path("signin-done/", views.Singup_Closed.as_view(), name="signin_done"),

]

