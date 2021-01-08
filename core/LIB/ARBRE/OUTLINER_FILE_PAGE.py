

import os, sys, cgi
getPath = os.path.dirname(os.path.abspath(__file__))
getPath = os.path.dirname(getPath)
sys.path.append(getPath + "/LIB")

import OUTLINER_IO_PAGE
PAGE = OUTLINER_IO_PAGE.FILE_PAGE()

import OUTLINER_IO_TABLE
TABLE = OUTLINER_IO_TABLE.FILE_TABLE()
import OUTLINER_IO_TEXT
O_TEXT = OUTLINER_IO_TEXT.IO_IMPORT()

import OUTLINER_IO_TREE
O_TREE = OUTLINER_IO_TREE.IO_IMPORT()
import OUTLINER_IO_ARBRE
O_ARBRE = OUTLINER_IO_ARBRE.IO_IMPORT()
import OUTLINER_IO_GRAPHICS
O_GRAPHICS = OUTLINER_IO_ARBRE.IO_IMPORT()

import OUTLINER_FILE_PAGE_COMP
COMP_TREE = OUTLINER_FILE_PAGE_COMP.HTML()

class OUTLINER:
    def __init__(self):
        self.viewMode = "0"

    def MODE_single(self, PAGELIST, dbName):
        html = ""

        for i in PAGELIST:
            # print( i["INDEX"] , i["WHATS_THIS"] ,  i["TEXT"]  )
            html += self.CMD_generator(i , dbName)


        return html

    def MODE_tab(self , PAGELIST, dbName):
        html = ""

        naviTab = """ <ul class="nav nav-tabs nav-tabs-inverse"> %s </ul> """
        naviItem = """ <li class="nav-item"><a href="%s" data-toggle="tab" class="nav-link %s "><i class="fa fa-fw fa-lg fa-genderless"></i>  <span class="d-none d-lg-inline"> %s </span></a></li> """
        naviItemList = ""

        for index , i in enumerate(PAGELIST):
            if(index == 0 ):
                setActive = "active"
            else:
                setActive = ""
            naviItemList += naviItem % ( ("#tabID" + str(index) ) , setActive , i["TEXT"] )
        html += naviTab % (naviItemList)

        tabBody = """ <div class="tab-content"> %s  </div> """
        tabBodyItem = """ <div class="tab-pane fade %s " id="%s"> %s </div> """
        tabBodyItemList = ""



        for index , i in enumerate(PAGELIST):
            if(index == 0 ):setActive = " active show "
            else:setActive = ""
            tabItemBody = "<hr>"

            tabItemBody += self.CMD_generator(i , dbName)

            #----------------------

            id = ("tabID" + str(index))

            item = """
                    <h3 class="m-b-5"><b>%s</b></h3>
                    <p class="m-b-20">
                        %s 
                    </p>
                    <hr>
            """% ("" + i["TEXT"] ,"" + tabItemBody)


            tabBodyItemList += tabBodyItem % (setActive, id ,  item  )

        html += tabBody % (tabBodyItemList)

        return html


    def MODE_tabVersion2(self , PAGELIST, dbName):
        html = """
    <div class="profile">
        <div class="profile-header">
            <div class="profile-header-cover"></div>
            
            <div class="profile-header-content">
                
                    %s                
                <div class="profile-header-info">
                    <h4 class="m-t-10 m-b-5">%s</h4>
                    <p class="m-b-10">%s</p>
                    %s
                </div>

            </div>
            
            
            <ul class="profile-header-tab nav nav-tabs">

                %s
            </ul>
        </div>
    </div>
    
    <div class="profile-content">
        <div class="tab-content p-0">
            %s
        </div>
    </div>
        """



        naviItemList = ""
        naviItem = """ <li class="nav-item"><a href="%s" class="nav-link %s" data-toggle="tab">%s</a></li> """
        for index , i in enumerate(PAGELIST):
            if(index == 0 ):
                setActive = "active"
            else:
                setActive = ""
            naviItemList += naviItem % (("#tabID" + str(index)), setActive, i["TEXT"])

        tabBodyItemList = ""


        bodyItem = """
            		<div class="tab-pane fade %s " id="%s">
            		    %s
            		</div>

        """
        for index , i in enumerate(PAGELIST):
            if(index == 0 ):setActive = "  show active "
            else:setActive = " fade in "
            tabItemBody = ""

            tabItemBody += self.CMD_generator(i , dbName)
            id = ("tabID" + str(index))
            tabItemBody += "<hr>"

            tabBodyItemList += bodyItem % ( setActive, id , tabItemBody )

        mainTitle = "&nbsp;"
        subTitle = "&nbsp;"
        editButton = """ <a href="#" class="btn btn-xs btn-yellow">Edit Profile</a> """
        editButton = """ <p> &nbsp; </p> """
        profileImage = """                 <div class="profile-header-img"><img src="../assets/img/user/user-8.jpg" alt=""></div> """
        profileImage = ""
        return html % (profileImage , mainTitle , subTitle ,editButton,  naviItemList , tabBodyItemList )




    def CMD_generator(self, i , dbName):
        tabItemBody = ""
        if (i["WHATS_THIS"] == "TABLE"):

            # DATA_table = TABLE.IO_DATA_RAW( i["DATA"] )
            # file, israw , gridtype , hastitle
            DATA_table = TABLE.HTML_TABLE_BODY(i["DATA"], "1", "-1", "0")
            # html += (DATA_table[0] , "<br>", DATA_table[1] ,"<br><br>")

            tabItemBody += (DATA_table[0])
            if (DATA_table[1] != ""):
                tabItemBody += ("<br>" + DATA_table[1])
            # html += "<br>"

        elif (i["WHATS_THIS"] == "TEXTEDIT_PLAIN"):
            DATA_text = O_TEXT.IO_DATA(i["DATA"], "1")
            dataHTML = DATA_text[0]["DATA_TEXT"]

            dataHTML = dataHTML.replace(" ", "&nbsp;&nbsp;")
            textList = dataHTML.split("\n")
            setTEXTMain = ""
            for textItem in textList:
                setTEXTMain += textItem + "<br>"

            comp = """
            <div class="panel panel-inverse">


                <div class="panel-body">%s</div>
            </div>
            """

            tabItemBody += comp % setTEXTMain

        elif (i["WHATS_THIS"] == "TEXTEDIT_HTML"):

            tabItemBody += ("aaa<br>")

            DATA_text = O_TEXT.IO_DATA(i["DATA"], "1")

            # dataHTML = DATA_text[0]["DATA_HTML"].split( "</body></html>" )
            # dataHTML = dataHTML[0]

            # html += dataHTML


        elif (i["WHATS_THIS"] == "TREE" or i["WHATS_THIS"] == "LIST"):

            tabItemBody += "<br>"

            DATA_text = O_TREE.IO_DATA_reOrder(i["DATA"], "1")
            DATA_MAIN = DATA_text[0]
            DATA_CHILD = DATA_text[1]
            #COMP_TREE.setDBName = self.IMAGE_DB_NAME
            #COMP_TREE.setDBName = "AAAAA"
            COMP_TREE.setDBName = dbName
            tabItemBody += COMP_TREE.render(DATA_MAIN, DATA_CHILD )

            tabItemBody += ("<br>")
            tabItemBody += ("<br>")

        return tabItemBody

    def render(self , fileName , fileMode = "0" , dbName = "" ):

        #--------------------------------------

        getLIst = PAGE.IO_DATA( fileName , fileMode)
        PAGELIST = getLIst[2]

        SCENE = getLIst[1]

        self.viewMode = SCENE["OUTPUT_TYPE"]

        html = ""
        if(self.viewMode == "0" or self.viewMode == ""):
            #html += self.MODE_tab(PAGELIST , dbName)
            html += self.MODE_tabVersion2(PAGELIST , dbName)
        elif(self.viewMode == "1"):
            html += self.MODE_single(PAGELIST, dbName)

        return html



#outliner = OUTLINER()
#html = outliner.render("bbbbb.opagetab")
#print(html)
