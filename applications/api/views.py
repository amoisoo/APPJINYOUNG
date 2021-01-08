from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.
from django.utils.text import slugify
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView


def index(request):
    html = """

    <h2><a href="../">Application API</a><br/></h2>

    <a href="./time">time</a><br/>
    <a href="./jump">jump</a><br/>
    <a href="./temp">temp</a><br/><br/>

    <a href="./api">API</a><br/>
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
    object_list = {"title": "title", "note": "note", "detail": mark_safe("datail<b>detail</b>detail")}
    # object_list = PostModel.objects.all()
    return render(request, 'COLORADMIN_FRONT/index.html', object_list)



class INDEX_TEMPLATE(TemplateView):
    template_name = 'blog/index.html'

