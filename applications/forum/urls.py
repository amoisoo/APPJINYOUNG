from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "forum"

urlpatterns = [
    #path('', views.index, name='index'),
    path('forum', views.INDEX_TEMPLATE.as_view()  , name='index2'),
    path('sub/', views.CATEGORY_TEMPLATE.as_view()  , name='category'),
    path('detail/', views.DETAIL_TEMPLATE.as_view()  , name='detail'),
    path(r"time", views.time),
    path(r"jump", views.jump),
    path(r"temp", views.temp),
#    re_path(r'^.*\.html', views.pages, name='pages'),

]

from django.urls.converters import StringConverter

class HangulSlugConverter(StringConverter):
    regex = '[-\w]+'

from django.urls import register_converter
register_converter(HangulSlugConverter, 'myslug')



urlpatterns += [

    path(""                                   , views.FORUM_LIstView.as_view()      , name="index"),
    re_path(r"^category/(?P<slug>[-\w]+)/$"           , views.FORUM_DetailView.as_view()    , name="detail"),
    re_path(r"^category/(?P<slug>[-\w]+)/update/$", views.FORUM_UpdateView.as_view(), name="update"),
    re_path(r"^category/(?P<slug>[-\w]+)/delete/$", views.FORUM_DeleteView.as_view(), name="delete"),

    #path("<slug:slug>/<int:pk>/", views.FORUM_DetailView.as_view()    , name="detail"),
    #path("<slug:slug>/update/", views.FORUM_UpdateView.as_view(), name="update"),
    #path("<slug:slug>/delete/", views.FORUM_DeleteView.as_view(), name="delete"),

    # re_path(r"^(?P<slug>[-\w]+)/update/$"   , views.FORUM_UpdateView.as_view()    , name="update"),
    # re_path(r"^(?P<slug>[-\w]+)/delete/$"   , views.FORUM_DeleteView.as_view()    , name="delete"),


    # path("<int:pk>/", views.FORUM_DetailView.as_view(), name="detail"),
    #path("<int:pk>/update/", views.FORUM_UpdateView.as_view(), name="update"),
    #path("<int:pk>/delete/", views.FORUM_DeleteView.as_view(), name="delete"),

    path("forum/create/"          , views.FORUM_CreateView.as_view(),    name="create"),

]


urlpatterns += [
    path("forum/category/create/<int:pk>/", views.FORUMSUB_CreateView.as_view(), name="create_sub"),

    re_path(r"^category/(?P<slug>[-\w]+)/(?P<pk>\d+)/$" , views.FORUMSUB_DetailView.as_view(), name="category_detail"),
    re_path(r"^category/(?P<slug>[-\w]+)/(?P<pk>\d+)/update/$", views.FORUMSUB_UpdateView.as_view(), name="category_update"),
    re_path(r"^category/(?P<slug>[-\w]+)/(?P<pk>\d+)/delete/$", views.FORUMSUB_DeleteView.as_view(), name="category_delete"),

    path("category/<int:pk>/delete/<int:pk2>", views.FORUMSUB_DeleteView.as_view(), name="delete_sub"),

    #re_path(r"^category/(?P<slug>[-\w]+)/(?P<slug2>[-\w]+)/$", views.FORUMSUB_DetailView.as_view(), name="category_detail"),

    #re_path(r"^category/(?P<slug>[-\w]+)/delete/$", views.FORUMSUB_DetailView.as_view(), name="category_detail"),

    #path("<slug:slug>/<int:pk>/", views.FORUMSUB_DetailView.as_view(), name="category_detail"),

    path("forum/<int:pk>/update/<int:pk2>/", views.FORUMSUB_UpdateView.as_view(), name="update_sub"),
    path("<str:slug>/<str:slug2>//update/<int:pk2>/", views.FORUMSUB_UpdateView.as_view(), name="update_sub"),

    #path("category/<int:pk>/update/<int:pk2>/", views.FORUMSUB_UpdateView.as_view(), name="update_sub"),

    #path("<int:pk>/<int:pk2>/", views.FORUMSUB_DetailView.as_view(), name="category_detail"),

    #path("<int:pk>/<int:pk2>/", views.FORUMSUB_DetailView.as_view(), name="detail_sub"),

    path("category/"                 , views.FORUMSUB_LIstView.as_view(),      name="index_sub"),

]

urlpatterns += [
    path("forum/page_create/", views.PAGE_CreateView.as_view(), name="page_create"),


    path("page/<str:forum>/<str:category>/<int:pk>/", views.PAGE_DetailView.as_view(), name="page_detail"),
    path("page/<str:forum>/<str:category>/<int:pk>/update/", views.PAGE_UpdateView.as_view(), name="page_update"),
    path("page/<str:forum>/<str:category>/<int:pk>/delete/", views.PAGE_DeleteView.as_view(), name="page_delete"),


]


urlpatterns += [

    path("forum/comment_create/", views.COMMENT_CreateView.as_view(), name="comment_create"),

    path("comment/<str:forum>/<str:category>/<int:pk>/", views.COMMENT_DetailView.as_view(), name="comment_detail"),
    path("comment/<str:forum>/<str:category>/<int:pk>/update/", views.COMMENT_UpdateView.as_view(), name="comment_update"),
    path("comment/<str:forum>/<str:category>/<int:pk>/delete/", views.COMMENT_DeleteView.as_view(), name="comment_delete"),

]



urlpatterns += [


]+ static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )













