from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "book"

urlpatterns = [
    #path('', views.index, name='index'),
    path('book/', views.INDEX_TEMPLATE.as_view()  , name='book_index'),
    path(r"time", views.time , name = 'time'),
    path(r"jump", views.jump , name = 'jump' ),
    path(r"temp", views.temp , name = 'temp'),
#    re_path(r'^.*\.html', views.pages, name='pages'),

]





urlpatterns += [
    #path('', views.index, name='books'),


    path(""                 , views.BOOK_LIstView.as_view(),      name="index"),
    #path("book/<int:pk>/"        , views.BOOK_DetailView.as_view(),    name="book_detail"),

    path("book_create/"          , views.BOOK_CreateView.as_view(),    name="book_create"),
    path("book/<str:slug>/update/" , views.BOOK_UpdateView.as_view(),    name="book_update"),
    path("book/<str:slug>/delete/" , views.BOOK_DeleteView.as_view(),    name="book_delete"),

    path("book/<slug:slug>/", views.BOOK_DetailView.as_view(), name="book_detail"),

]






urlpatterns += [
    #path("book/(?P<book>[-\w]+)/(?P<slug>\d+)/", views.MENU_DetailView.as_view(), name="menu_detail"),

    #path('book/(?P<book>[-a-zA-Z0-9_]+)/(?P<slug>[-a-zA-Z0-9_]+)/$', views.MENU_DetailView.as_view(), name="menu_detail"),
    path("book/<slug:book>/<slug:slug>/"            , views.MENU_DetailView.as_view(), name="menu_detail"),
    path("book/<slug:book>/<slug:slug>/update/"     , views.MENU_UpdateView.as_view(), name="menu_update"),
    path("book/<slug:book>/<slug:slug>/delete/"     , views.MENU_DeleteView.as_view(), name="menu_delete"),

    path("menu/create/", views.MENU_CreateView.as_view(), name="menu_create"),

    path("menu/"                 , views.MENU_LIstView.as_view(),      name="menu_index"),


    path("menu/<int:pk>/", views.MENU_DetailView.as_view(), name="menu_detail2"),

]






urlpatterns += [

    path("page/<int:pk>/update/<slug:book>/<slug:slug>/", views.PAGE_UpdateView.as_view(), name="page_update"),
    path("page/<int:pk>/delete/<slug:book>/<slug:slug>/", views.PAGE_DeleteView.as_view(), name="page_delete"),
    path("page/create/<slug:book>/<slug:slug>/", views.PAGE_CreateView.as_view(), name="page_create"),

    path("page/<int:pk>/<slug:book>/<slug:slug>/", views.PAGE_DetailView.as_view(), name="page_detail"),


]




urlpatterns += [

] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )