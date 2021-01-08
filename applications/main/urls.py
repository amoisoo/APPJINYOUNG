"""APPWEB2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path , include
from . import views
#from accounts.accounts import views as accountsView


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('', views.index , name='index'),
    path('', views.INDEX_TEMPLATE.as_view(), name='index'),
    path('index/', views.INDEX2_TEMPLATE.as_view(), name='index2'),
    #path("login/",  accountsView.Login.as_view(), name="login"),

    path('time', views.time, name='time'),
    path('jump', views.jump, name='jump'),
    re_path(r'^.*\.html', views.pages, name='pages'),

    #path('blog/', include('blog.urls')),

    path("accounts/"    , include("accounts.accounts.urls"    )     , name='accounts' ),
    path("users/"       , include("users.urls"    )         , name='users' ),
    #path("accounts/", include("applications.accounts.urls"), name='accounts'),

    path("api/"       , include("applications.api.urls")        , name='api'),
    path("arbre/"       , include("applications.arbre.urls")        , name='arbre'),
    path("blog/"        , include("applications.blog.urls")         , name='blog'),
    path("book/"       , include("applications.book.urls")        , name='book'),
    path("doc/"         , include("applications.doc.urls")        , name='doc'),
    path("forum/"       , include("applications.forum.urls")        , name='forum'),
    path("play/"      , include("applications.play.urls")       , name='play'),
    path("sample/"      , include("applications.sample.urls")       , name='sample'),
    path("shelf/"       , include("applications.shelf.urls")        , name='shelf'),
    path("support/"     , include("applications.support.urls")     , name='support'),


]+ static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )



