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
    def __init__(self , serverName, dbName, pageUUID ):

        self.setDBName =  dbName
        self.tableName = "public_index"
        self.db = MYSQL.DB(serverName, "conie6mm", "Leekyou7811#", "BOOK_"+ self.setDBName)
        # db = MYSQL.DB("13.71.132.251", "conie6mm", "Leekyou7811#", "Outliner")

        self.toplist = self.db.SELECT_LOOP_PARENT_LIST(self.tableName, 0)
        self.subChildList = self.db.SELECT_LOOP_CHILD_LIST(self.tableName)

        self.pageUUID = pageUUID
    def DB_LIST(self):
        return self.db.LIST_DB()


    def NAVI_BREADCRUMB(self,  setUUID):
        if(setUUID == ""):return []

        curList = self.db.SELECT_SINGLE_UUID("public_index", (setUUID[5:]))

        if(curList == []): return setUUID[5:]
        #return str(curList)

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
        aa_string = str(getIndex)
        #bb_string = str(getTitle)

        return getIndex
        return aa_string



    def subchild(self , getID, uuidList):
        html = """
            <ul class="sub-menu">
                %s
            </ul>
        """
        getList = self.subChildList[getID]
        menuList = ""
        for i in getList:
            setTag = ""
            if (i[9] == "new"): setTag = """<span class="badge badge-success float-right"> %s </span>""" % i[9]
            elif (i[9] == "info"): setTag = """<span class="badge badge-danger float-right"> %s </span>""" % i[9]
            elif (i[9] != ""): setTag = """<span class="badge badge-danger float-right"> %s </span>""" % i[9]
            if (("id_" + i[2]) in self.subChildList):
                # under level  cihld - loop
                # print("----", "id_" + i[2] )
                mainMenuActive = ""
                if (i[0] in uuidList): mainMenuActive = """ active """
                menuList += """<li class="has-sub %s "><a  href="#"><b class="caret"></b>%s %s  </a>  %s</li>""" % (mainMenuActive , setTag , (i[1]), self.subchild("id_" + i[2],uuidList)  )
                # menuList += """<li><a href="#">zzzzz</a></li>"""
                # """ % (j[1] , subchild( ("id_" + j[2])    ))

                #if (i[20] == "True"): menuList += """<li class="divider"></li> """

            else:
                # under level no cihld
                mainMenuActive = ""
                if (i[0] in uuidList): mainMenuActive = """ class="active" """

                menuList += """	<li %s ><a href="?book=%s&page=%s" data-toggle="tooltip" data-placement="top" >%s  %s </a></li> """ % (mainMenuActive , self.setDBName , i[6], setTag ,  i[1])

                #if (i[20] == "True"): menuList += """<li class="divider"></li> """

        return html % menuList

    def render(self):
        getPageUUID = []
        try:getPageUUID = self.NAVI_BREADCRUMB(self.pageUUID)
        except:getPageUUID = []

        naviHtml = ""
        for i in self.toplist:
            setTag = ""
            if(i[12] != ""): setTag = """ <span class="label label-theme m-l-5">%s</span></span> """ % (i[12])

            #--------------------------------------------
            # only top level
            #--------------------------------------------

            # <span class="badge pull-right">10</span><b class="caret"></b>
            # top level : depth is 0
            mainMenuActive = ""

            setMainTitle = i[1]
            titleLenSize = 18
            if( len(i[1]) > titleLenSize):
                setMainTitle = i[1][:titleLenSize] + "..."

            if(i[0] in getPageUUID): mainMenuActive = " active "
            naviHtml += """<li class="has-sub %s "> 
                            <a href="javascript:;">  <b class="caret"></b> <i class="fa fa-th-large"></i><span> %s </span>
                                     %s 
                            </a>
                            <ul class="sub-menu">
            """ % ( mainMenuActive ,  (  setMainTitle) , setTag)


            #--------------------------------------------
            # child, child in child
            #--------------------------------------------
            childList = self.db.SELECT_LOOP_CHILD(self.tableName, i[0])
            for j in childList:
                # print(("id_" + j[2]))

                setTag = ""
                if(j[9] == "new"):setTag = """<span class="badge badge-success float-right"> %s </span>""" % j[9]
                elif(j[9] == "info"):setTag = """<span class="badge badge-danger float-right"> %s </span>""" % j[9]
                elif(j[9] != ""):setTag = """<span class="badge badge-danger float-right"> %s </span>""" % j[9]

                if (("id_" + j[2]) in self.subChildList): # child in child case
                    subMenuActive = ""
                    if (j[0] in getPageUUID): subMenuActive = "active"

                    naviHtml += """
                        <li class="has-sub  %s " > 
                            <a href="javascript:;"><b class="caret"></b> %s %s </a> 
                            %s
                        </li>
                    """ % (subMenuActive , setTag , j[1], self.subchild( ("id_" + j[2]  ), getPageUUID ))
                    #if(j[20] == "True"):naviHtml += """<li class="divider"></li> """

                else: # only one level child
                    #naviHtml += """<li><a href="?book=%s&page=%s">%s %s</a></li>""" % (setTag , self.setDBName , j[6], j[1])
                    subMenuActive = ""
                    if (j[0] in getPageUUID): subMenuActive = """ class="active"  """

                    naviHtml += """	<li %s ><a href="?book=%s&page=%s" data-toggle="tooltip" data-placement="top" >%s  %s </a></li> """ % (subMenuActive , self.setDBName , j[6], setTag , j[1]  )
                    #if(j[20] == "True"):naviHtml += """<li class="divider"></li> """
            naviHtml += "</ul></li>"

        return naviHtml

