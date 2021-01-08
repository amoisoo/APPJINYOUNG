from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views





urlpatterns = [

    path("", include("applications.sample.urls"  ) , name = 'indexs'),
    path("accounts/", include("accounts.accounts.urls"), ),
    path("support/", include("applications.support.urls"), ),



]+ static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
