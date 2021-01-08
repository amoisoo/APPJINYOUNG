#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
# coding: utf-8
import os, sys, cgi
import io
import html
import sqlite3
from datetime import datetime

getPath = os.path.dirname(os.path.abspath(__file__))
getPath = os.path.dirname(getPath)
sys.path.append(getPath + "/LIB_COMMON")

import MYSQL

class HTML:
    def __init__(self, serverName, dbName, pageName, homeAddress, daName):

        self.setDBName = dbName

        self.tableName = pageName
        self.db = MYSQL.DB(serverName, "conie6mm", "Leekyou7811#", "BOOK_"+ self.setDBName)
        # db = MYSQL.DB("13.71.132.251", "conie6mm", "Leekyou7811#", "Outliner")

        self.toplist = self.db.SELECT_LOOP_PARENT_LIST(self.tableName, 0)
        self.subChildList = self.db.SELECT_LOOP_CHILD_LIST(self.tableName)


        self.homeAddress = homeAddress
        self.dbName = daName

        #self.imagePath = r"../imgOutliner"
        # level top , level2
        #
        self.imagePath = r"../outliner/imgOutliner"

    def subchild(self , getID, parentTytpe = None , mode = None , tableName = None ):
        html = """
                %s
        """
        getList = self.subChildList[getID]
        menuList = ""


        for index, i in enumerate(getList):
            if (("id_" + i[2]) in self.subChildList):
                if(i[10]  == "Grid" and i[11] == "plain"):
                    menuList += """<div class="container"><div id="portfolio" class="portfolio-gutter"><div class="row mix-grid">%s %s""" % ("", self.subchild("id_" + i[2], i[10] , 1 , i[6]) )
                    menuList += "</div></div></div>"
                elif(i[10]  == "Grid" and i[11] == "LIST"):
                    menuList += """<div class="container"><div class="row"> <div class="col-md-12 col-sm-12"><ul class="grid grid-4 grid-xs-3"> %s %s""" % ("", self.subchild("id_" + i[2], i[10] , 2 , i[6])  )
                    menuList += "</ul></div></div></div>"
                elif(i[10]  == "Horizontal"):
                    menuList += """
				<div class="container">
					<div class="text-center">
						<div class="owl-carousel owl-padding-1 m-0 buttons-autohide controlls-over" data-plugin-options='{"singleItem": false, "items": "4", "autoPlay": 3500, "navigation": true, "pagination": false}'>
                            %s %s
						</div>
					</div>
				</div>
                    """ % ("", self.subchild("id_" + i[2], i[10]))

                elif(i[10]  == "Tab"):
                    tabList         = self.subchild("id_" + i[2], i[10] , 1 , i[6])
                    contenList      = self.subchild("id_" + i[2], i[10] , 2 , i[6])
                    setDATA = (i[1], tabList ,contenList )
                    menuList += """
                        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
                                    <h4>%s</h4>
                                    <ul class="nav nav-tabs">%s</ul>
                                    <div class="tab-content">%s</div>
                        </div></div></div>
                    """ % setDATA

                elif(i[10]  == "Accordion"):
                    # <div class="toggle toggle-transparent toggle-bordered-full">
                    menuList += """
                        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
                            <div class="row">
                                <div class="col-md-2">
                                    
                                </div>
                                <div class="col-md-10">
                                        <div class="toggle toggle-transparent-body">
                                            %s %s
                                        </div>
                                </div>
                            </div>


                        </div></div></div><br>
                    """ % ("", self.subchild("id_" + str(i[2]), i[10]))

                else:
                    menuList += """AAAAAA  %s %s<br>""" % (i[1], self.subchild("id_" + i[2], i[10]))
            else:
                #menuList += self.COMP_LIST(i)

                if(parentTytpe  == "Grid" and mode == 1):
                    menuList +=  self.COMPITEM_grid(i)
                elif(parentTytpe  == "Grid" and mode == 2):
                    menuList +=  self.COMPITEM_gridList(i)
                elif(parentTytpe  == "Horizontal"):
                    menuList += self.COMPITEM_horizontal(i)
                elif(parentTytpe  == "Accordion"):
                    menuList += self.COMPITEM_accordian(i)
                elif(parentTytpe  == "Tab" and mode == 1):
                    menuList += self.COMPITEM_tabA(i , index ,  tableName)
                elif(parentTytpe  == "Tab" and mode == 2):
                    menuList += self.COMPITEM_tabB(i , index,  tableName )
                else:
                    menuList += self.COMP_LIST(i)
        return html % menuList

    def NAVI_BREADCRUMB(self, setTitle , subTitle ,setUUID):
        naviHtml = """
			<!-- begin breadcrumb -->

                <ol class="breadcrumb pull-right">
                    <li class="breadcrumb-item"><a href="%s%s">HOME</a></li>

                    %s
                </ol>
			<!-- begin page-header -->

                <h1 class="page-header">%s <small>%s</small></h1>

        """


        curList = self.db.SELECT_SINGLE_UUID("public_index", (setUUID))
        allList = self.db.CMD_import("public_index")

        setIndex = int(curList[3])

        getTitle = []
        getTitle.append( curList[1] )
        getIndex = []
        getIndex.append( curList[0] )


        if(curList[3] != "0"):
            #newData = MYSQL_DB.SELECT_SINGLE_ID( "public_index",  curList[3])
            #print(newData)
            while True:
                newData = self.db.SELECT_SINGLE_ID("public_index",  setIndex)

                if (newData[3] == "0"):
                    getIndex.append(newData[0])
                    getTitle.append(newData[1])

                    break
                else:
                    setIndex = int(newData[3])
                    getIndex.append(newData[0])
                    getTitle.append(newData[1])

        getIndex.reverse()
        getTitle.reverse()


        result = ""
        for k, i in enumerate(getTitle):
            #result += """ <li "><a href="./db_menuDetail.wsgi?main=%s&id=%s">%s</a></li> """ % ( DB_PFRIFIX_TABLE_NAME, getIndex[k], getTitle[k] )
            result += """ <li class="breadcrumb-item active">  %s</li> """ % (   getTitle[k] )

        #aa_string = str(getIndex)
        #bb_string = str(getTitle)
        final = ""
        final += naviHtml % (self.homeAddress ,  "", result , setTitle, subTitle)
        #final += naviHtml % (self.homeAddress ,  self.dbName, result , setTitle, subTitle)

        #final += "<br>" + aa_string
        #final += "<br>" + bb_string

        return final


    def TREE(self):
        naviHtml = ""


        naviHtml += "<br>"
        topHeaderList = []

        for i in self.toplist:
            if( i[10] == "Header" ):
                topHeaderList.append( i[0] )

        for i in self.toplist:

            #if (len(topHeaderList) != 1 and len(topHeaderList) != 0):
            #    if (i[10] in topHeaderList): naviHtml = """ </div> </div> """


            # CHILD LIST
            childList = self.db.SELECT_LOOP_CHILD(self.tableName, i[0])

            childHTML = ""
            for j in childList:

                # print(("id_" + j[2]))
                if (("id_" + j[2]) in self.subChildList):
                    childHTML += "" + self.COMP_LIST(j)
                    childHTML += """
                            %s
                    """ % ( self.subchild(("id_" + j[2])))
                else:
                    childHTML += "" + self.COMP_LIST(j)


            depathFirst = self.COMP_LIST(i)
            # BASE HEADER
            naviHtml += """
                            %s
                            %s
                            
            """ % ( depathFirst , childHTML)
            if( i[0] in  topHeaderList):
                naviHtml += """ </div> </div> """

        #naviHtml = str(topHeaderList)
        return naviHtml


    def render(self,  mode=0):
        if(self.tableName == ""): # if top
            return self.TREE()


        info = self.db.SELECT_SINGLE_UUID("public_index", self.tableName[5:])
        if(info[11] == "plain"):

            html = """"""
            html += info[1] + "<br><br><br>"

            getString = info[16].split("\n")
            setString = ""
            for i in getString:
                setString += i + "<br>"

            html += setString

            NAVI_BREADCRUMB = self.NAVI_BREADCRUMB("", "", info[6])
            result = NAVI_BREADCRUMB + "<br>" + self.COMP_text(info)
            return result
        elif(info[11] == "html"):

            NAVI_BREADCRUMB = self.NAVI_BREADCRUMB("", "", info[6])
            result = NAVI_BREADCRUMB


            return result + "<br>" + info[16][459: -14]

        else: # TREE
            naviHtml = ""
            if(mode == 1):
                naviHtml = """

                        <!-- Welcome -->
                        <br>
                            <div class="container">
            
                                <div class="text-center">
                                    <h1 class="mb-0"> <span>%s</span> </h1>
                                    <h2 class="col-sm-10 offset-sm-1 mb-0 fw-300 text-muted fs-20"> %s </h2>
                                </div>
            
                            </div><br>
                        <!-- Welcome -->
                """ % (info[1] , info[13])
                naviHtml += self.NAVI_BREADCRUMB("", "", info[6])

            elif(mode == 0):

                naviHtml += self.NAVI_BREADCRUMB(info[1],info[13], info[6])
            naviHtml += self.TREE()
            return naviHtml

    def COMP_LIST(self, item):
        result = ""

        if(item[10]     == "Title")     : result = self.COMP_title(item)
        elif(item[10]   == "Header"): result = self.COMP_header(item)
        elif(item[10]   == "Parameter1"): result = self.COMP_parameter1(item)
        elif(item[10]   == "Parameter2"): result = self.COMP_parameter2(item)
        elif(item[10]   == "Section")   : result = self.COMP_section(item)
        elif(item[10]   == "Code")      : result = self.COMP_code(item)
        elif(item[10]   == "Text")      : result = self.COMP_text(item)
        elif(item[10]   == "Grid")      : result = self.COMP_grid(item)
        elif(item[10]   == "ImageView")      : result = self.COMP_image(item)
        elif(item[10]   == "ImageToggle")      : result = self.COMP_image(item)
        elif(item[10]   == "ImageText1")      : result = self.COMP_image(item)
        elif(item[10]   == "ImageGIF")      : result = self.COMP_imageGIF(item)
        elif(item[10]   == "Youtube")      : result = self.COMP_youtube(item)
        #elif(item[10]   == "ImageView") : result = self.COMP_image(item)
        else : resutl = "ERROR"

        return result


    def COMPITEM_gridList(self, item):
        dbItem = """ <li class="col-md-5th col-sm-2th col-6"> <a href = "?book=%s" > %s </a> </li> """
        return dbItem % (item[1], item[1])

    def COMPITEM_grid(self, item):



        html = """
            <div class="col-md-5th col-sm-4 mix development">

                <div class="item-box">
                    <figure>
                        <span class="item-hover">
                            <span class="overlay dark-5"></span>
                            <span class="inner">

                                <!-- lightbox -->
                                <a class="ico-rounded lightbox" href="%s" data-plugin-options='{"type":"image"}'>
                                    <span class="fa fa-plus fs-20"></span>
                                </a>

                            </span>
                        </span>
                        <img class="img-fluid" src="%s" width="600" height="399" alt="">
                    </figure>
                </div>

            </div>
        """

        # assets/images/mockups/1200x800/20-min.jpg
        # assets/images/mockups/600x399/20-min.jpg
        setImage = self.imagePath + r"/" + self.setDBName + r"_image/" + item[22]

        return html % (setImage  , setImage)

    def COMPITEM_accordian(self , item):
        html = """
                <div class="toggle">
                    <label>%s</label>
                    <div class="toggle-content">
                        <p>%s</p>
                    </div>
                </div>
        """

        getString = item[16].split("\n")
        setString = ""
        for i in getString:
            setString += i + "<br>"

        return html % (str(item[1]), setString)

    def COMPITEM_horizontal(self, item):
        html = """
							<div class="item-box">
								<figure>
									<span class="item-hover">
										<span class="overlay dark-5"></span>
										<span class="inner">

											<!-- lightbox -->
											<a class="ico-rounded lightbox" href="%s" data-plugin-options='{"type":"image"}'>
												<span class="fa fa-plus fs-20"></span>
											</a>



										</span>
									</span>

									<img class="img-fluid" src="%s" width="600" height="399" alt="">
								</figure>

								<div class="item-box-desc">
									<h3>%s</h3>
									<ul class="list-inline categories m-0">
										<li><a href="#">%s</a></li>
									</ul>
								</div>

							</div>
        """
        #<a class="ico-rounded lightbox" href="assets/images/mockups/1200x800/16-min.jpg" data-plugin-options='{"type":"image"}'>
        # <img class="img-fluid" src="assets/images/mockups/600x399/16-min.jpg" width="600" height="399" alt="">

        setImage = self.imagePath + r"/" + self.setDBName + r"_image/" + item[22]

        return html % (setImage  , setImage ,  item[1] ,  item[13])

    def COMPITEM_tabA(self, item , index, setID):
        if(index == 0):
            html = """<li class="nav-item"><a class="nav-link active" href="#%s"        data-toggle="tab">%s</a></li>"""
        else:
            html = """<li class="nav-item"><a class="nav-link " href="#%s"        data-toggle="tab">%s</a></li>"""

        return html  % ( str(index) + "_" + setID, item[1])

    def COMPITEM_tabB(self, item , index, setID):
        if(index == 0):
            html = """ <div class="tab-pane active" id="%s"><p>%s</p></div>"""
        else:
            html = """ <div class="tab-pane fade" id="%s"><p>%s</p></div>"""

        return html  % ( str(index) + "_" + setID, item[16]  )

    def COMP_title(self, item):
        html = """


<ul class="result-list">
    <li>
        <a href="#" class="result-image" style="background-image: url(../assets/img/gallery/gallery-51.jpg)"></a>
        <div class="result-info">
            <h4 class="title"><a href="javascript:;">  %s </a></h4>
            <p class="location">  %s </p>
            <p class="desc">
                %s 
            </p>
            <div class="btn-row">


            </div>
        </div>

    </li>

</ul>
<br>
        """

        return html % ( item[1] ,  item[35] ,  item[16] )


    def COMP_header(self, item):
        html = """
 
			<div class="panel panel-inverse"  >
			<div class="panel-heading" data-click="panel-collapse" ><div class="panel-heading-btn">

        """
        #html += """   <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-warning" data-click="panel-collapse"><i class="fa fa-minus"></i></a>  """

        #html += """   <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-default" data-click="panel-expand"><i class="fa fa-expand"></i></a> """
        #html += """   <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-success" data-click="panel-reload"><i class="fa fa-redo"></i></a>  """
        #html += """   <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-danger" data-click="panel-remove"><i class="fa fa-times"></i></a>  """

        html += """  	</div><h4 class="panel-title">%s</h4></div>  """

        html += """ <div class="panel-body">    """

        # TREE function add - final tag add
        #html += """ </div> </div> """

        setTitle = ""
        if(item[1] == ""):setTitle = "_"
        else:setTitle = item[1]

        return html % (setTitle )
        return html % ("", item[1] , item[13])

    def COMP_image(self, item):
        html = """
        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
            <div class="row">
                <div class="col-md-2">

                </div>

                <div class="col-md-8">
                        <img src="%s" alt="image01"/>
                </div>
            </div>
        </div></div></div><br>
        """

        setImage  = self.imagePath + r"/" + self.setDBName + r"_image/"  + item[22]

        return html % (setImage)

    def COMP_imageGIF(self, item):
        html = """
        <br>
        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
            <div class="row">
                <div class="col-md-2">

                </div>

                <div class="col-md-8">
                        <img src="%s" alt="image01"/>
                </div>
            </div>
        </div></div></div>
        """

        setImage  = self.imagePath + r"/" + self.setDBName + r"_image/"  + item[22]

        return html % (setImage)


    def COMP_parameter1(self, item):
        html = """
        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
            <div class="row">
                <div class="col-md-2">
                    
                </div>
                <div class="col-md-8">
                    <h5 class="mb-8">%s</h5>
                    <p> %s </p>
                </div>
            </div>
        </div></div></div>
        """
        if(item[20] == "True"):
            html += "<hr />"

        getString = item[16].split("\n")
        setString = ""
        for i in getString:
            setString += i + "<br>"

        return html % (str(item[1]), setString)

    def COMP_parameter2(self, item):
        html = """

        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">

            <div class="row">
            
                <div class="col-md-2">
                </div>
                
                <div class="col-md-8">
                    <h5 class="mb-8">%s</h5>
                    <p> %s </p>
                </div>
                
                        %s
            </div>
        </div></div></div>

        """

        setImage = ""
        if(item[22] != ""):

            imageHtml = """
                <div class="col-md-2">
                    <img src="%s" class="img-fluid" alt="company logo">
                </div>
            """
            setImage = imageHtml % (self.imagePath + r"/" + self.setDBName + r"_image/" + item[22])

        if (item[20] == "True"):
            html += "<hr />"

        return html % (  str(item[1]), item[16], setImage )

    def COMP_section(self, item):
        html = ""

        if (item[20] == "True"):
            html += "<hr />"

        html += """
        <br>
         <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">

            <div class="heading-title heading-border">
                <h4>%s <span>%s</span></h4>
                <p class="font-lato fs-14">%s</p>
            </div>


            %s
            
        </div></div></div>

        """

        if(item[16] != ""):
            getString = item[16].split("\n")
            setString = ""
            for i in getString:
                setString += i + "<br>"


            titleBase = """
                <div class="row">
                    <div class="col-md-2">
                        
                    </div>
                    <div class="col-md-8">
                        
                        <p> %s </p>
                    </div>
                </div>
            """

            netTitle = titleBase % setString
        else:
            netTitle = ""

        return html % ("", str(item[1]), item[13] , netTitle )

    def COMP_code(self, item):
        html = """

        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
            <div class="row">
                <div class="col-md-2">
                </div>
                
                <div class="col-md-8">
                    %s
                    <div class="alert alert-warning mb-30"><!-- WARNING -->
                        %s
                        %s
                    </div>
                </div>
            </div>
        </div></div></div>
        """
        if (item[20] == "True"):
            html += "<hr />"


        setTitle = ""
        if(item[1] != ""):
            setTitle = """ <h5 class="mb-8">%s</h5> """ % item[1]

        setSubTitle = ""
        if(item[13] != ""):
            setSubTitle = """ <strong>%s</strong> <br><br> """ % item[13]

        getString = item[17].split("\n")
        setString = ""
        for i in getString:
            #setString += i + "<br>"
            setString += i.replace(" " , "&nbsp;&nbsp;") + "<br>"

        return html % (setTitle, setSubTitle , setString)

        setCode = "<pre>%s</pre>" % item[17]
        return html % (setTitle, setSubTitle , setCode)

    def COMP_text(self, item):
        html = """
         <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">

            <div class="row">
                <div class="col-md-2">

                </div>
                <div class="col-md-8">
                        %s
                    <p> <pre>%s </pre></p>
                </div>
            </div>
        </div></div></div>

        """
        if (item[20] == "True"):html += "<hr />"

        setTitle = ""
        if(item[1] != ""):
            setTitle = """ <h4 class="mb-8">%s</h4> """ % item[1]

        return html % (setTitle, item[16])

    def COMP_grid(self, item):
        html = """
        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
            <div class="row">
                <div class="col-md-2">

                </div>
                <div class="col-md-8">
                    <h4 class="mb-8">%s</h4>
                    <p> %s </p>
                </div>
            </div>
        </div></div></div>
        """
        if (item[20] == "True"):
            html += "<hr />"

        return html % (str(item[1]), item[16])

    def COMP_youtube(self, item):

        html = """
            <div class="row">
                <div class="col-md-4">
                </div>
                <div class="col-md-6">

                <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
                <iframe width="560" height="315" src="%s" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                </div>
    </div>
        </div></div></div>
        """
        if (item[20] == "True"):
            html += "<hr />"

        return html % ( item[16])
