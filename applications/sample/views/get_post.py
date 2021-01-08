
from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView , View


class INDEX_TEMPLATE(TemplateView):
    template_name = 'sample/get_post/index.html'


class PAGE_view(View):
    def get(self, request, *args, **kwargs):

        get = request.GET.get('page')

        if (get == None):
            view = INDEX_TEMPLATE.as_view()
            return view(request, *args, **kwargs)

        else:
            html = "aaa" + get

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