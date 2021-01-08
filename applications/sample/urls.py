from django.urls import path , re_path


from django.conf.urls.static import static
from django.conf import settings


from applications.sample.views import views
from applications.sample.views import matplot
from applications.sample.views import jsonfile
from applications.sample.views import panda
from applications.sample.views import download
from applications.sample.views import doc
from applications.sample.views import get_post
from applications.sample.views import jquery
from applications.sample.views import cookie_view


app_name = "sample"
urlpatterns = [
    path('', views.index, name='index'),
#  path('', views.INDEX_TEMPLATE.as_view()  , name='index'),
    path(r"time/", views.time),
    path(r"jump/", views.jump),
    path(r"temp/", views.temp),
    path(r"sample/", views.sample),

    path(r"system/", views.system),


    path('coloradmin', views.INDEX_COLORADMIN.as_view()  , name='coloradmin'),
    path('skote', views.INDEX_SKOTE.as_view()  , name='skote'),


]


urlpatterns += [

    re_path(r'^.*\.html', doc.pages, name='pages'),

]

urlpatterns += [

    path(r"matplot/", matplot.sample),
    path(r"matplot/plot/", matplot.plot),
    path(r"matplot/plot_np/", matplot.plot_np),
    path(r"matplot/hist/", matplot.hist),
    path(r"matplot/pie/", matplot.pie),

]

urlpatterns += [

    path(r"json/json/", jsonfile.json),
    path(r"json/jsonfile/", jsonfile.jsonfile),
    path(r"json/jsonread/", jsonfile.jsonread),
    path(r"json/json_response/", jsonfile.json_response),

]

urlpatterns += [

    path(r"panda/", panda.excel),

]

urlpatterns += [

    path(r"download/", download.download),

]

urlpatterns += [

    path(r"cookie/index/", cookie_view.index),

]


urlpatterns += [

    path(r"download/", download.download),

]


urlpatterns += [

    path(r"get_post/", get_post.PAGE_view.as_view()),

]

urlpatterns += [

    path(r"jquery/", jquery.PAGE_view.as_view()),

]

urlpatterns += [


]+ static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )


