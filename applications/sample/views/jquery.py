
from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect , JsonResponse
from django.views.generic import TemplateView , View


class INDEX_TEMPLATE(TemplateView):
    template_name = 'sample/get_post/index.html'


from django.views.decorators.csrf import csrf_exempt

class PAGE_view(View):
    @csrf_exempt
    def get(self, request, *args, **kwargs):

        get = request.GET.get('page')

        if (get == None):
            import datetime
            now = datetime.datetime.now()

            result = {}
            result.update({'title': '아무것도 없습니다.'})
            result.update({'note': '설정하세요.'})
            result.update({'get': get})
            result.update({'time': now})

            return JsonResponse(result)



        else:



            import datetime
            now = datetime.datetime.now()

            result = {}

            from applications.blog.models import Blog

            from django.core.serializers import serialize
            #data = serialize("json", Comment.objects.all() )
            getDATA  = Blog.objects.all()


            for i in getDATA:
                print( i.note )

            data = serialize("json", getDATA)



            result.update({'title': '정보를 얻었습니다.'})
            result.update({'data': data })
            #result.update({'raw': getDATA})
            result.update({'get': get})
            result.update({'time': now})

            return JsonResponse(result)


            html = "JQEURY : " + get
            return HttpResponse(html)

    def post(self, request, *args, **kwargs):
        # view = PAGE_DeleteView.as_view()

        getType = request.POST.get('comment')
        if (getType == "comment_type"):
            view = INDEX_TEMPLATE.as_view()
            # view = PAGE_UpdateView.as_view()
            return view(request, *args, **kwargs)
        else:
            view = INDEX_TEMPLATE.as_view()
            # view = PAGE_UpdateView.as_view()
            return view(request, *args, **kwargs)