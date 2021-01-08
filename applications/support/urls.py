from django.urls import path

from . import views


app_name = "support"


urlpatterns = [
    #path('', views.index, name='supports'),
    path('', views.INDEX_TEMPLATE.as_view()  , name='index'),
    path(r"time", views.time),
    path(r"jump", views.jump),
    path(r"temp", views.temp),

    path('qna/', views.INDEX_QNA.as_view(), name='qna'),
    path('download/', views.INDEX_DOWNLOAD.as_view(), name='download'),
    path('help/', views.INDEX_HELP.as_view(), name='help'),
    path('doc/', views.INDEX_DOC.as_view(), name='doc'),
    path('doc/css/', views.INDEX_DOC_CSS.as_view(), name='css'),

    path('newslatter/', views.INDEX_NEWSLATTER.as_view(), name='newslatter'),
    path('git/', views.INDEX_DOC_GIT.as_view(), name='git'),

]