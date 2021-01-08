from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "arbre"

urlpatterns = [
    path(r"arbre/", views.temp , name = 'arbre'),
    path('', views.ARBRE_TEMPLATE.as_view()  , name='index'),

    path('index2', views.index, name='index2'),

    path('temp', views.INDEX_TEMPLATE.as_view()  , name='temp'),
    path(r"time", views.time , name = 'time'),
    path(r"jump", views.jump , name = 'jump'),
#    re_path(r'^.*\.html', views.pages, name='pages'),

] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )