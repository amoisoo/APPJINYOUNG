from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, View


def index(request):
    html = """
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <h2><a href="../">Application Samples</a><br/></h2>

    <a href="./time">time</a><br/>
    <a href="./jump">jump</a><br/>
    <a href="./temp">temp</a><br/>

    {{ MEDIA_URL }}
    <a href="{{ MEDIA_URL }}/download/bootstrap.zip">Download</a><br/>
    <a href="./download">download</a><br/><br/>

    <a href="./sample">Sample</a><br/>
    <a href="./bootstrap/index.html">bootstrap</a><br/>
    <a href="skote">skote</a><br/>


    """
    return HttpResponse(mark_safe(html))


def time(request):
    import datetime
    now = datetime.datetime.now()
    html = "<html><body>지금 POST 시간은 <br>%s.</body></html>" % now
    return HttpResponse(html)


def jump(request):
    return HttpResponseRedirect("http://google.com/")


def temp(request):
    object_list = {"title": "asdfasdfa", "note": "note", "detail": mark_safe("datail<b>detail</b>detail")}
    # object_list = PostModel.objects.all()
    return render(request, 'sample/temp.html', object_list)

def system(request):
    import os, sys
    sysv_version = sys.version
    html = "<html><body> Python Version <br/>%s.</body></html>" % sysv_version
    return HttpResponse(html)


def sample(request):
    object_list = {"title": "asdfasdfa", "note": "note", "detail": mark_safe("datail<b>detail</b>detail")}
    # object_list = PostModel.objects.all()
    return render(request, 'sample/download.html', object_list)





class INDEX_COLORADMIN(TemplateView):
    template_name = 'COLORADMIN_ADMIN/index.html'


class INDEX_SKOTE(TemplateView):
    template_name = 'SKOTE/index.html'


