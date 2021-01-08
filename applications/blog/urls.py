from django.urls import path , re_path

from . import views

app_name = "blog"


urlpatterns = [
    #path('', views.index, name='blogs'),
    path('blog/', views.INDEX_TEMPLATE.as_view(), name='index2'),
    path(r"time", views.time),
    path(r"jump", views.jump),
    path(r"temp", views.temp),
]



urlpatterns += [

    path(""                 , views.BLOG_LIstView.as_view(),      name="index"),
    path("post/<int:pk>/"        , views.BLOG_DetailView.as_view(),    name="detail"),
    path("post/create/"          , views.BLOG_CreateView.as_view(),    name="create"),
    path("post/<int:pk>/update/" , views.BLOG_UpdateView.as_view(),    name="update"),
    path("post/<int:pk>/delete/" , views.BLOG_DeleteView.as_view(),    name="delete"),

]

urlpatterns += [

    path("archive/"                 , views.BLOG_AV.as_view(),      name="archive"),
    path("archive/<int:year>/"                 , views.BLOG_AV_YEAR.as_view(), name="archive_year"),
    path("archive/<int:year>/<str:month>/", views.BLOG_AV_MONTH.as_view(), name="archive_month"),
    path("archive/<int:year>/<str:month>/<int:day>/", views.BLOG_AV_DAY.as_view(), name="archive_day"),

]


urlpatterns += [

    path("search/", views.Blog_search.as_view(), name="search"),
    path("contact/", views.Blog_contact.as_view(), name="contact"),

]

urlpatterns += [

    re_path(r"^site/(?P<slug>[-\w]+)/$", views.BLOG_DetailView.as_view(), name="slug"),

]




urlpatterns += [

    #path("commnet/<int:pk>/"        , views.COMMNET_DetailView.as_view(),    name="commnet_detail"),
    path("comment/create/"          , views.COMMENT_CreateView.as_view(),    name="commnet_create"),
    path("comment/<int:pk>/update/" , views.COMMENT_UpdateView.as_view(),    name="commnet_update"),
    path("comment/<int:pk>/delete/" , views.COMMENT_DeleteView.as_view(),    name="commnet_delete"),

]