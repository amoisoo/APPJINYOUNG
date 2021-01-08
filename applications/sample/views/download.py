from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView , View


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

def system(request):
    import os, sys
    sysv_version = sys.version
    html = "<html><body> Python Version <br/>%s.</body></html>" % sysv_version
    return HttpResponse(html)


#https://qiita.com/t-iguchi/items/ac9638dbdbe509515148
#https://wayhome25.github.io/django/2017/03/19/django-ep3-fbv/

#https://dev-yakuza.posstree.com/django/response-model-to-json/
import csv
import urllib
def download(request , num = 10):

    response = HttpResponse(content_type='text/csv; charset=utf-8')
    filename = urllib.parse.quote((u'촬영장.csv').encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    writer = csv.writer(response)
    for post in range(num):
        writer.writerow( str(post) )
    return response

