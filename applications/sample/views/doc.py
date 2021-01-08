from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, View



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
    url_root = '00_sample/'
    url_root = '00_sample/'

    try:

        url_size = request.path.split('/')

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
            return HttpResponse(html_template.render(DATA_context, request))


    except template.TemplateDoesNotExist:

        html_template = loader.get_template('COLORADMIN_ADMIN/404.html')
        return HttpResponse(html_template.render(DATA_context, request))

    except:

        html_template = loader.get_template('500.html')
        return HttpResponse(html_template.render(DATA_context, request))
























