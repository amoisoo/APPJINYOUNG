from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "doc"


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.INDEX_TEMPLATE.as_view(), name='index'),
    path('temp', views.INDEX2_TEMPLATE.as_view(), name='index2'),
    path(r"time", views.time),
    path(r"jump", views.jump),
    #re_path(r'^.*\.html', views.pages, name='pages'),
    re_path(r'^.*\.*', views.pages, name='pages'),  # for  subdomain

]



urlpatterns += [

] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )