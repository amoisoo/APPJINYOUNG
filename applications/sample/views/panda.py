from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, View



import os, sys
from django.http import HttpResponse
import json


# from froala_editor import Image
# from froala_editor import DjangoAdapter

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





def jsonfile(request):
    # return HttpResponse(open("data/static/FROALA_CHART/sample_json/CHART_COMP_pie.json", 'rb').read())

    from django.conf import settings
    from django.http import JsonResponse

    p = os.path.join(settings.STATIC_URL, 'FROALA_CHART/sample_json/CHART_COMP_pie.json')
    # return HttpResponse(p)
    getFile = open('data/static/FROALA_CHART/sample_json/CHART_COMP_pie.json', 'rb')
    json_data = getFile.read()
    return HttpResponse(json_data)




def excel(request):

    import pandas as pd

    import pandas as pd
    # pip install xlrd
    filePath = 'data/zztest/panda.xls'

    #data = pd.read_excel(filePath, sheet_name='Sheet1')
    data = pd.read_excel(filePath)
    data.to_csv('./pandas_csv.csv', index=False)

    html = ""
    html += str(data.shape )+ "<br/>"

    print(data.head())
    for i in data.head():
        print(i )
        html += ( i  +  "<br/>")

    html += (  "<pre>%s</pre><br/>" % (str(data.head())) )

    return HttpResponse(mark_safe(html))



























