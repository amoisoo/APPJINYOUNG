from django.shortcuts import render
from django.utils.html import mark_safe
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView


from django.conf import settings
import os, sys


class INDEX_TEMPLATE(TemplateView):
    template_name = 'COLORADMIN_ADMIN/APP_DOC/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        dirPath = 'data'  + os.path.join(settings.MEDIA_URL, 'LIBDB/QT/QtBase')
        dirPath = "templates/doc/"

        forlderList = []
        fileList = []

        for item in os.listdir(dirPath):
            if os.path.isdir(dirPath + item):
                forlderList.append(item)
            elif os.path.isfile(dirPath +item):
                fileList.append(item)


        context['FOLDER_LIST']      = forlderList
        context['FILE_LIST']      = fileList



        return context







def index(request):
    object_list = {"title": "asdfasdfa", "note": "note", "detail": mark_safe("datail<b>detail</b>detail")}

    # object_list = PostModel.objects.all()
    return render(request, 'doc/home.html', object_list)

class INDEX2_TEMPLATE(TemplateView):
    template_name = 'index.html'

def time(request):
    import datetime
    now = datetime.datetime.now()
    html = "<html><body>지금 POST 시간은 <br>%s.</body></html>" % now
    return HttpResponse(html)


def jump(request):
    return HttpResponseRedirect("http://google.com/")




from django.contrib.auth.decorators import login_required
from django.template import loader
from django import template
from django.shortcuts import render, get_object_or_404, redirect


#@login_required(login_url="/login/")
def pages(request):
    DATA_context = {"title": "타이틀을 지정합니다", "note": "메세지를 입력하세요"}

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that templates.
    url_root = '00_sample/'
    url_root = 'doc/'

    try:
        url_size = request.path.split('/')
        print("PAGES", len(url_size)  , url_size)
        if( len(url_size) == 2 ):

            load_template = request.path.split('/')[-1]
            #return HttpResponse( load_template )

            #html_template = loader.get_template( 'aaa.html')
            html_template = loader.get_template(url_root + load_template)
            return HttpResponse(html_template.render(DATA_context, request))

        elif( len(url_size) == 3 ) :
            url_path = request.path.split('/')[1] # subpath
            url_file = request.path.split('/')[2] # .html filename
            url_html = request.path.split('/')[-1]
            html_template = loader.get_template( url_root + url_path + '/' + url_file)
            return HttpResponse(html_template.render(DATA_context, request))

        elif( len(url_size) == 4 ) :


            url_path = request.path.split('/')[1]  + r'/' + request.path.split('/')[2]
            url_file = request.path.split('/')[3] # .html filename
            url_html = request.path.split('/')[-1]
            html_template = loader.get_template( url_root + url_path + '/' + url_file)
            print( url_root + url_path + '/' + url_file)

            return HttpResponse(html_template.render(DATA_context, request))

        elif( len(url_size) == 5 ) :
            url_path = request.path.split('/')[1]  + r'/' + request.path.split('/')[2]+ r'/'+ request.path.split('/')[3]

            url_file = request.path.split('/')[4] # .html filename

            url_html = request.path.split('/')[-1]
            html_template = loader.get_template( url_root + url_path + '/' + url_file)
            return HttpResponse(html_template.render(DATA_context, request))


    except template.TemplateDoesNotExist:
        print("PAGES", "ERROR")

        html_template = loader.get_template('SKOTE/APP_ACCOUNTS/404.html')
        return HttpResponse(html_template.render(DATA_context, request))

    except:

        html_template = loader.get_template('SKOTE/APP_ACCOUNTS/500.html')
        return HttpResponse(html_template.render(DATA_context, request))



