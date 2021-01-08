from django.urls import path , re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "api"


urlpatterns = [
    path('', views.index, name='blogs'),
    #path('blog/', views.INDEX_TEMPLATE.as_view(), name='index2'),
    path(r"time", views.time),
    path(r"jump", views.jump),
    path(r"temp", views.temp),
]




urlpatterns += [

] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )