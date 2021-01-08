from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "shelf"

urlpatterns = [
    path('', views.index, name='index'),
#  path('', views.INDEX_TEMPLATE.as_view()  , name='index'),
    path(r"time", views.time),
    path(r"jump", views.jump),
    path(r"temp", views.temp),
#    re_path(r'^.*\.html', views.pages, name='pages'),

] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )