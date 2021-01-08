from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils.html import mark_safe
# from django.shortcuts import render_to_response --> delete old version : change render
# Create your views here.
from django.conf import settings
from django.http import JsonResponse


from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView , View
import os, sys

def temp(request):
    object_list = {"title": "title", "note": "note", "detail": mark_safe("datail<b>detail</b>detail")}
    # object_list = PostModel.objects.all()
    return render(request, 'SKOTE/APP_ARBRE/index.html', object_list)

from core.LIB.ARBRE.OUTLINER_IO_TEXT import IO_IMPORT
from core.LIB.ARBRE.OUTLINER_IO_TABLE import FILE_TABLE as IO_TABLE
from core.LIB.ARBRE.OUTLINER_IO_TREE import IO_IMPORT as  IO_TREE
from core.LIB.ARBRE.OUTLINER_IO_PAGE import FILE_PAGE as IO_TABPAGE

def MENU_SUB_REODER( DATA ):
    result = {}


    for item in DATA: #create list
        if not ( item['depth'] in result.keys() ):
            result[  item['depth']  ] = [  ]



    for item in DATA:  # create list
        if (  item['depth'] in result.keys()):
            result[ item['depth' ]].append( item )


    print(result)
    return result

def CURRENT_DATA( DATA_allList  , uuid ):

    for i in DATA_allList:
        #print(uuid,   i[ 'uuid' ] == uuid  )

        if( i[ 'uuid' ] == uuid   ):
            return i

    return {}


class ARBRE_TEMPLATE(TemplateView):
    template_name = 'COLORADMIN_ADMIN/APP_ARBRE/arbre.html'
    template_name = 'SKOTE/APP_ARBRE/arbre.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #-----------------------------------------
        POST_LIST = self.request.GET
        context['GET_LIST']  = POST_LIST
        context['GET_ID']  =   self.request.GET.get('id')

        setObject = {}
        setObject['layout'] = "LEFT" # LEFT
        context['PAGE_SETTINGS'] = setObject
        #-----------------------------------------
        #dirPath = 'data'  + os.path.join(settings.MEDIA_URL, 'LIBDB/DEV/Dev_Linux')
        dirPath = 'data'  + os.path.join(settings.ARBRE_URL, 'WEB/CSS3')
        #filePath = 'data'  + os.path.join(settings.MEDIA_URL, 'LIBDB/WEB/CSS3/CSS3_02_Selector.txml')

        print("POST LIST", POST_LIST.keys())
        FILE_NAME = 'CSS3_02_Selector.txml'
        try:
            if  ( "db" in POST_LIST.keys() ):FILE_NAME = POST_LIST['db']
        except:pass

        filePath =  dirPath + '/'  + FILE_NAME
        context['DB_NAME']      = FILE_NAME
        context['DB_NAME_ONLY']      = FILE_NAME.split('.')[0]

        context['DB_LIST']      = os.listdir(dirPath)
        context['FILE_PATH']    = filePath
        #-----------------------------------------







        #-----------------------------------------
        GET_ID = self.request.GET.get('id')
        getTable            = IO_TREE().IO_DATA(   filePath  )
        getCurrentItem      = CURRENT_DATA( getTable , GET_ID   )
        context['object']  = getCurrentItem

        MENU_TOP = []
        MENU_SUB = []
        for i in getTable:
            if(i['depth'] == '0'):MENU_TOP.append(i)
            else:MENU_SUB.append(i)
        setMENU_SUB = MENU_SUB_REODER( MENU_SUB )
        context['MENU_LIST'] = MENU_TOP
        context['MENU_LIST_SUB'] = setMENU_SUB
        #-----------------------------------------

        #print( "DATA"  ,getCurrentItem  )


        if(  getCurrentItem != {}):
            if(getCurrentItem['context'] == "TABPAGE"):

                GETDATA = IO_TABPAGE().IO_DATA( getCurrentItem['data']  , '1'  )

                context['PAGE_TAB_WIDGET'] = GETDATA[0]
                context['PAGE_TAB_SETTINGS'] = GETDATA[1]
                context['PAGE_TAB_DATA'] = GETDATA[2]

            elif(getCurrentItem['context'] == "TABLE"):

                getTable = IO_TABLE().IO_DATA(getCurrentItem['dates']  , '1')
                context['TABLES0'] = getTable[0]
                context['TABLES1'] = getTable[1]

                getTable = IO_TABLE().HTML_TABLE_BODY(getCurrentItem['dates']  , '1')
                context['TABLES3'] = getTable[0]

                getTable = IO_TABLE().ITEM_GRID(getCurrentItem['dates'], '1')
                context['TABLES4'] = getTable
                context['TABLES5'] = getTable[1]
            elif(getCurrentItem['context'] == "TREE"):
                print('TREETREE' , getCurrentItem )

                getTable = IO_TREE().IO_DATA(  getCurrentItem['data'], '1' )

                context['TREE'] = getCurrentItem

                MENU_TOP = []
                MENU_SUB = []
                for i in getTable:
                    if (i['depth'] == '0'):
                        MENU_TOP.append(i)
                    else:
                        MENU_SUB.append(i)
                setMENU_SUB = MENU_SUB_REODER(MENU_SUB)
                context['PAGE_LIST'] = MENU_TOP
                context['PAGE_CHILD_LIST'] = setMENU_SUB

            elif(getCurrentItem['context'] == "LIST"):
                pass


            elif(getCurrentItem['context'] == "html"):
                pass
            elif(getCurrentItem['context'] == "plain"):
                pass

        #getTable = IO_TABLE().IO_DATA(   getCurrentItem['dates'] )
        #print(getTable)

        #context['DATA_TABLE'] = getTable

        return context
#
class TREE_TEMPLATE(TemplateView):
    template_name = 'SKOTE/APP_ARBRE/arbre.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #-----------------------------------------
        POST_LIST = self.request.GET
        context['GET_LIST']  = POST_LIST

        setObject = {}
        setObject['layout'] = "" # LEFT
        context['PAGE_SETTINGS'] = setObject
        #-----------------------------------------
        dirPath = 'data'  + os.path.join(settings.MEDIA_URL, 'LIBDB/WEB/CSS3')
        #filePath = 'data'  + os.path.join(settings.MEDIA_URL, 'LIBDB/WEB/CSS3/CSS3_02_Selector.txml')

        print(POST_LIST.keys())
        FILE_NAME = 'CSS3_02_Selector.txml'
        try:
            if  ( "db" in POST_LIST.keys() ):FILE_NAME = POST_LIST['db']
        except:pass

        filePath =  dirPath + '/'  + FILE_NAME
        context['DB_NAME']      = FILE_NAME

        context['DB_LIST']      = os.listdir(dirPath)
        context['FILE_PATH']    = filePath
        #-----------------------------------------







        #-----------------------------------------
        GET_ID = self.request.GET.get('id')
        getTable            = IO_TREE().IO_DATA(   filePath  )
        getCurrentItem      = CURRENT_DATA( getTable , GET_ID   )
        context['object']  = getCurrentItem

        MENU_TOP = []
        MENU_SUB = []
        for i in getTable:
            if(i['depth'] == '0'):MENU_TOP.append(i)
            else:MENU_SUB.append(i)
        setMENU_SUB = MENU_SUB_REODER( MENU_SUB )
        context['MENU_LIST'] = MENU_TOP
        context['MENU_LIST_SUB'] = setMENU_SUB
        #-----------------------------------------





        #getTable = IO_TABLE().IO_DATA(   getCurrentItem['dates'] )
        #print(getTable)

        #context['DATA_TABLE'] = getTable

        return context

#table
class INDEX_TEMPLATE(TemplateView):
    template_name = 'SKOTE/APP_ARBRE/index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        filePath = 'data'  + os.path.join(settings.MEDIA_URL, 'LIBDB/WEB/CSS3/CSS3_05_List.txml')

        # return HttpResponse(p)
        context['URL_BOOK']  = self.request.GET.get('slug')
        context['GET_LIST']  = self.request.GET
        context['FILE_PATH']  = filePath

        getTable = IO_TREE().IO_DATA(   filePath  )
        getTable = IO_TREE().IO_DATA(   filePath  )
        print(getTable)

        context['MENU_LIST_SUB'] = getTable


        getTable = IO_TABLE().HTML_TABLE_BODY(   filePath  )
        print(getTable)

        context['MENU_LIST_SUB'] = getTable[0]


        return context




class INDEX_TABLE(TemplateView):
    template_name = 'SKOTE/APP_ARBRE/index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #filePath = os.path.join(settings.STATIC_URL, 'FROALA_CHART/sample_json/CHART_COMP_pie.json')
        filePath =  'data/media/LIBDB/WEB/CSS3/box.tablexml'
        filePath = 'data'  + os.path.join(settings.MEDIA_URL, 'LIBDB/WEB/CSS3/borderIndex.tablexml')
        filePath = 'data'  + os.path.join(settings.MEDIA_URL, 'LIBDB/WEB/Framework/uikit3_list.tablexml')

        # return HttpResponse(p)
        context['URL_BOOK']  = self.request.GET.get('slug')
        context['GET_LIST']  = self.request.GET
        context['FILE_PATH']  = filePath

        getTable = IO_TABLE().HTML_TABLE_BODY(   filePath  )
        print(getTable)

        context['MENU_LIST_SUB'] = getTable[0]


        return context






class INDEX_VIEW(View):
    def get(self, request, *args, **kwargs):

        print(request.GET.get('slug'))

        view = INDEX_TEMPLATE.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        #getType = request.POST.get('comment')

        view = INDEX_TEMPLATE.as_view()
        return view(request, *args, **kwargs)





def index(request):
    html = """

    <h2><a href="../">Application Arbres</a><br/></h2>

    <a href="./time">time</a><br/>
    <a href="./jump">jump</a><br/>
    <a href="./temp">temp</a><br/><br/>

    <a href="./arbre">Arbre</a><br/><br/>



    <a href="#">OUTLINER_FILE_NAVI</a><br/>
    <a href="#">OUTLINER_FILE_PAGE</a><br/>
    <a href="#">OUTLINER_FILE_PAGE_COMP</a><br/><br/>
    
    <a href="#">OUTLINER_IO_ARBRE</a><br/>
    <a href="#">OUTLINER_IO_GRAPHICS</a><br/>
    <a href="#">OUTLINER_IO_PAGE</a><br/>
    <a href="#">OUTLINER_IO_TABLE</a><br/>
    <a href="#">OUTLINER_IO_TEXT</a><br/>
    <a href="#">OUTLINER_IO_TREE</a><br/>

    """
    return HttpResponse(mark_safe(html))


def time(request):
    import datetime
    now = datetime.datetime.now()
    html = "<html><body>지금 POST 시간은 <br>%s.</body></html>" % now
    return HttpResponse(html)


def jump(request):
    return HttpResponseRedirect("http://google.com/")




