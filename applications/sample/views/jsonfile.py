from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, View



import os, sys
from django.http import HttpResponse
import json
from django.http import JsonResponse


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


def json(request):
    # error resolve : https://blog.softhints.com/python-common-beginners-mistakes/
    import json

    data = {'team': 'Brazil', 'position': 1, 'host': True, 'lastGame': 'Win'}
    dictToJson = json.dumps(data)
    return HttpResponse(json.dumps(dictToJson), content_type="application/json")

    response = {'error': str(sys.exc_info()[1])}

    return HttpResponse(json.dumps(response), content_type="application/json")


def jsonfile(request):
    # return HttpResponse(open("data/static/FROALA_CHART/sample_json/CHART_COMP_pie.json", 'rb').read())

    from django.conf import settings
    from django.http import JsonResponse

    p = os.path.join(settings.STATIC_URL, 'FROALA_CHART/sample_json/CHART_COMP_pie.json')
    # return HttpResponse(p)
    getFile = open('data/static/FROALA_CHART/sample_json/CHART_COMP_pie.json', 'rb')
    json_data = getFile.read()
    return HttpResponse(json_data)




    with open('data/static/FROALA_CHART/sample_json/CHART_COMP_pie.json', 'rb') as json_file:
        json_data = json_file.read()
        obj = json.loads(json_data)
    return JsonResponse(obj)

    from django.contrib.staticfiles.storage import staticfiles_storage
    p = staticfiles_storage.path('FROALA_CHART/sample_json/CHART_COMP_pie.json')  # staticfiles path

    return HttpResponse(p)

    with open('/static/FROALA_CHART/sample_json/CHART_COMP_pie.json') as json_file:
        json_data = json_file.read()
        obj = json.loads(json_data)
    return JsonResponse(obj)


def jsonread(request):
    import json
    filePath = 'data/static/test/json/data.json'
    filePath = 'data/arbre/testjson/data.json'
    getDATA = json.load(open(filePath, encoding='utf-8'))
    html = ''
    for i in getDATA:
        html+= i + "<br/>"

    return HttpResponse(mark_safe(html))


    import json
    filePath = 'data/static/test/json/data.json'
    filePath = 'data/arbre/testjson/data.json'
    getDATA = json.load(open(filePath, encoding='utf-8'))
    return HttpResponse(mark_safe(getDATA))


def json_response(request):
    import datetime
    now = datetime.datetime.now()

    result  = {}
    result.update( {'aaa' : 'aaaa'} )
    result.update( {'bbb' : 'bbbb'} )
    result.update( {'ddd' : 'dddd'} )
    result.update( {'eee' : 'eeee'} )
    result.update( {'time' : now} )


    return JsonResponse(result)



    return HttpResponse(json.dumps(response), content_type="application/json")



























