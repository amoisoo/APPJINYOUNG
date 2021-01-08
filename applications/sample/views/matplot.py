from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView , View





def sample(request):
    uri = None

    import matplotlib.pyplot as plt
    import  io
    import urllib , base64
    plt.title( "Sample")

    plt.plot( range(10) )


    fig = plt.gcf()
    buffer = io.BytesIO()
    fig.savefig( buffer , format = "png" )
    buffer.seek(0)
    string = base64.b64encode( buffer.read() )
    uri = urllib.parse.quote( string )


    object_list = {"title": "Matplot Sample", "data": uri, "detail": mark_safe("datail<b>detail</b>detail")}
    # object_list = PostModel.objects.all()
    return render(request, 'doc/matplot/sample.html', object_list)




import matplotlib.pyplot as plt
import io
import urllib, base64
def plt_2_imageBase64( plt ):

    fig = plt.gcf()
    buffer = io.BytesIO()
    fig.savefig(buffer, format="png")
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    data = urllib.parse.quote(string)
    return data


def plot(request):
    data = None

    plt.title("Sample")
    plt.plot(range(10)  , color = 'red' , label = 'sky')
    plt.plot([40,30,20]   , color = 'blue' , label = 'blue')
    plt.legend()
    data = plt_2_imageBase64( plt )

    object_list = {"title": "Matplot Sample", "data": data, "detail": mark_safe("datail<b>detail</b>detail")}
    # object_list = PostModel.objects.all()
    return render(request, 'doc/matplot/sample.html', object_list)

def plot_np(request):
    data = None
    import numpy as np
    t = np.arange( 0,100 , 0.01)
    y = np.sin(t)

    plt.title("Sample")
    plt.plot(t, y  , color = 'red' , label = 'sky')
    data = plt_2_imageBase64( plt )

    object_list = {"title": "Matplot Sample", "data": data, "detail": mark_safe("datail<b>detail</b>detail")}
    # object_list = PostModel.objects.all()
    return render(request, 'doc/matplot/sample.html', object_list)

def hist(request):
    data = None

    plt.title("Sample")
    plt.hist( [1,1,2,3,4,5,6,6,7,8,9,10]  )
    plt.legend()
    data = plt_2_imageBase64( plt )

    object_list = {"title": "Matplot Sample", "data": data, "detail": mark_safe("datail<b>detail</b>detail")}
    # object_list = PostModel.objects.all()
    return render(request, 'doc/matplot/sample.html', object_list)



def pie(request):
    data = None

    plt.title("Sample")
    plt.pie( [30, 40, 70, 65  ]  )
    plt.legend()
    data = plt_2_imageBase64( plt )

    object_list = {"title": "Matplot Sample", "data": data, "detail": mark_safe("datail<b>detail</b>detail")}
    # object_list = PostModel.objects.all()
    return render(request, 'doc/matplot/sample.html', object_list)














