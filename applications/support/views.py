from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView


def index(request):
    html = """

    <h2><a href="../">Application Supports</a><br/></h2>

    <a href="./time">time</a><br/>
    <a href="./jump">jump</a><br/>
    <a href="./temp">temp</a><br/><br/>

    <a href="./support">Support</a><br/>
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
    return render(request, 'Main/temp.html', object_list)



class INDEX_TEMPLATE(TemplateView):
    template_name = 'COLORADMIN_ADMIN/APP_SUPPORT/index.html'



class INDEX_QNA(TemplateView):
    template_name = 'COLORADMIN_ADMIN/APP_SUPPORT/qna.html'


class INDEX_DOWNLOAD(TemplateView):
    template_name = 'COLORADMIN_ADMIN/APP_SUPPORT/download.html'

class INDEX_HELP(TemplateView):
    template_name = 'COLORADMIN_ADMIN/APP_SUPPORT/help.html'


class INDEX_DOC(TemplateView):
    template_name = 'COLORADMIN_ADMIN/APP_SUPPORT/doc.html'


class INDEX_DOC_CSS(TemplateView):
    template_name = 'COLORADMIN_ADMIN/APP_SUPPORT/css.html'


class INDEX_NEWSLATTER(TemplateView):
    template_name = 'COLORADMIN_ADMIN/APP_SUPPORT/newslatter.html'

class INDEX_DOC_GIT(TemplateView):
    template_name = 'COLORADMIN_ADMIN/APP_SUPPORT/DOC/git.html'