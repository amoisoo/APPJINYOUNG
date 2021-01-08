#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
# coding: utf-8
import os, sys, cgi
import io
import html
#import sqlite3
from datetime import datetime

# from PyQt5.QtCore import *

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

#######################################################################
#######################################################################
#getPath = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(getPath + "/LIB")
#getPath = os.path.dirname(getPath) + "/LIB"
#sys.path.append(getPath)

#######################################################################
#######################################################################
getPath = os.path.dirname(os.path.abspath(__file__))
getPath = os.path.dirname(getPath)
sys.path.append(getPath + "/LIB")
getPath = os.path.dirname(getPath) + "/LIB"
sys.path.append(getPath)
#######################################################################
#######################################################################


import PAGE_SETTINGS
import PAGE_NAVI
import PAGE_BODY
import PAGE_NAVI_MEGA

#######################################################################
#######################################################################




class HTML:
    def __init__(self):

        form                    = cgi.FieldStorage()
        DB_PFRIFIX_TABLE_NAME   = form.getvalue('main', '')
        DB_TABLE_NAME           = DB_PFRIFIX_TABLE_NAME[4:]
        DB_ID                   = form.getvalue('id', '')
        SUB_ID                  = form.getvalue('subid', '')

        self.getDBName          = form.getvalue('book', '')
        self.getPAGEName        = form.getvalue('page', '')


        self.dbName             = ""
        self.pageName           = ""

        if (self.getDBName != ""):      self.dbName     = self.getDBName
        if (self.getPAGEName != ""):    self.pageName   = "page_" + self.getPAGEName

        self.setMainTitle       = self.getDBName
        self.bodyPre           = ""#self.getPAGEName

        #-----------------------------------------------------
        self.setMainLogName     = "AMOISOO"
        self.sethomeAddress     = r"./" + os.path.basename(__file__)

        #-----------------------------------------------------
        if(self.getDBName == ""):self.setIndexTitle      = self.dbName
        else:self.setIndexTitle      = self.getDBName

        self.setIndexSubTitle   = "BBB"
        self.setIndexImage      = "../assets/img/user/user-9.jpg"


        self.setTitle           = r"amosoo"
        self.setTemplateHTML = r'LIB_JINJA2/BASE_PAGE.html'
        self.JINJA_FILEPATH = "./"


        self.CMD_initPage()

    def CMD_initPage(self):
        self.SETTINGS = PAGE_SETTINGS.SETTINGS()
        self.SETTINGS.MYSQL().HOST
        self.NAVI = PAGE_NAVI.HTML(self.SETTINGS.MYSQL().HOST, self.dbName , self.pageName)
        self.COMP = PAGE_BODY.HTML(self.SETTINGS.MYSQL().HOST, self.getDBName, self.pageName, self.sethomeAddress , self.dbName)


    def naviHtml(self):return self.NAVI.render()
    def outlinerHTML(self):return self.COMP.render()


    def setFooterInfo(self):
        setFooterInfo = """
            <br><br><br><br><br>
            <br><br><br><br><br>
            <div id="footer" class="footer">
                %s  -  %s (JST, +0900)
                <br> MAIL : contact@amoisoo.com
                <br> &copy; amoisoo - All Rights Reserved
            </div>
            <br><br>
        """
        year = datetime.now().strftime("%Y-%m-%d")
        setTime = datetime.now().strftime("%H:%M:%S")
        return setFooterInfo  % (year , setTime)

    def setHeaderNotificationList(self):
        setHeaderNotificationList = """
				<li class="dropdown">
					<a href="javascript:;" data-toggle="dropdown" class="dropdown-toggle f-s-14"><i class="fa fa-bell"></i><span class="label">23</span></a>

					<ul class="dropdown-menu media-list dropdown-menu-right">
        						<li class="dropdown-header">NOTIFICATIONS (5)</li>


        						<li class="media">
        							<a href="javascript:;">
        								<div class="media-left">
        									<i class="fa fa-bug media-object bg-silver-darker"></i>
        								</div>
        								<div class="media-body">
        									<h6 class="media-heading">Server Error Reports <i class="fa fa-exclamation-circle text-danger"></i></h6>
        									<div class="text-muted f-s-11">3 minutes ago</div>
        								</div>
        							</a>
        						</li>

        						<li class="media">
        							<a href="javascript:;">
        								<div class="media-left">
        									<i class="fa fa-bug media-object bg-silver-darker"></i>
        								</div>
        								<div class="media-body">
        									<h6 class="media-heading">Server Error Reports <i class="fa fa-exclamation-circle text-danger"></i></h6>
        									<div class="text-muted f-s-11">3 minutes ago</div>
        								</div>
        							</a>
        						</li>

        						<li class="media">
        							<a href="javascript:;">
        								<div class="media-left">
        									<img src="../assets/img/user/user-1.jpg" class="media-object" alt="" />
        									<i class="fab fa-facebook-messenger text-primary media-object-icon"></i>
        								</div>
        								<div class="media-body">
        									<h6 class="media-heading">John Smith</h6>
        									<p>Quisque pulvinar tellus sit amet sem scelerisque tincidunt.</p>
        									<div class="text-muted f-s-11">25 minutes ago</div>
        								</div>
        							</a>
        						</li>
        						<li class="media">
        							<a href="javascript:;">
        								<div class="media-left">
        									<img src="../assets/img/user/user-2.jpg" class="media-object" alt="" />
        									<i class="fab fa-facebook-messenger text-primary media-object-icon"></i>
        								</div>
        								<div class="media-body">
        									<h6 class="media-heading">Olivia</h6>
        									<p>Quisque pulvinar tellus sit amet sem scelerisque tincidunt.</p>
        									<div class="text-muted f-s-11">35 minutes ago</div>
        								</div>
        							</a>
        						</li>
        						<li class="media">
        							<a href="javascript:;">
        								<div class="media-left">
        									<i class="fa fa-plus media-object bg-silver-darker"></i>
        								</div>
        								<div class="media-body">
        									<h6 class="media-heading"> New User Registered</h6>
        									<div class="text-muted f-s-11">1 hour ago</div>
        								</div>
        							</a>
        						</li>
        						<li class="media">
        							<a href="javascript:;">
        								<div class="media-left">
        									<i class="fa fa-envelope media-object bg-silver-darker"></i>
        									<i class="fab fa-google text-warning media-object-icon f-s-14"></i>
        								</div>
        								<div class="media-body">
        									<h6 class="media-heading"> New Email From John</h6>
        									<div class="text-muted f-s-11">2 hour ago</div>
        								</div>
        							</a>
        						</li>
        						<li class="dropdown-footer text-center"><a href="javascript:;">View more</a></li>

                    </ul>
				</li>

        """

        return setHeaderNotificationList

    def setHeaderDBMenuList(self):
        setHeaderDBMenuList = """
            <a href="../swift/" class="dropdown-item">swift</a>
            <a href="../iphone/" class="dropdown-item">iphone</a>
                    <div class="dropdown-divider"></div>
            <a href="../web/" class="dropdown-item">web</a>
                    <div class="dropdown-divider"></div>

            <a href="../dev/" class="dropdown-item">Dev</a>
            <a href="../linux/" class="dropdown-item">linux</a>
            <a href="../python/" class="dropdown-item">python</a>
            <a href="../qt/" class="dropdown-item">qt</a>

                    <div class="dropdown-divider"></div>

            <a href="../physical/" class="dropdown-item">physical</a>

                    <div class="dropdown-divider"></div>

            <a href="../mac/" class="dropdown-item">mac</a>


                    <div class="dropdown-divider"></div>
            <a href="../cg/" class="dropdown-item"><span class="badge badge-danger pull-right">2</span>CG</a>
            <a href="../adobe/" class="dropdown-item">Adobe</a>
            <a href="../maya/" class="dropdown-item">maya</a>


                    <div class="dropdown-divider"></div>

            <a href="../doc/" class="dropdown-item">doc</a>
            <a href="../movie/" class="dropdown-item">movie</a>


        """
        return setHeaderDBMenuList



    def setIndexCategory(self):

        setIndexCategory = """ <li><a href="%s"><i class="fa fa-cog"></i> %s </a></li> """ % (self.sethomeAddress + "?book=Painter", "Painter 2018")
        setIndexCategory += """ <li><a href="%s"><i class="fa fa-cog"></i> %s </a></li> """ % (self.sethomeAddress + "?book=PainterBrushUltimate", "Painter Brush Ultimate")

        return setIndexCategory




    def searchNavi(self):
        result = """
				<li>
					<form class="navbar-form">
						<div class="form-group">
							<input type="text" class="form-control" placeholder="Enter keyword" />
							<button type="submit" class="btn btn-search"><i class="fa fa-search"></i></button>
						</div>
					</form>
				</li>
        """
        
        
        return ""


    def render(self):
        from jinja2 import Environment, FileSystemLoader

        env = Environment(loader=FileSystemLoader(self.JINJA_FILEPATH , encoding='utf8'))
        tpl = env.get_template(self.setTemplateHTML)

        html = """Content-Type: text/html; charset=utf-8\n """

        html = tpl.render({
            'shop'                      : 'ddd'
            , "bodyPre"                 : self.bodyPre
            , "outliner"                : self.outlinerHTML()

            , "navi"                    : self.naviHtml()
            , "naviSideBar"             : self.setNaviSideBar()
            , "naviMenuMega"             : self.menuMega()

            , "homeAddress"             : self.sethomeAddress

            , "title"                   : self.setTitle
            , "mainTitle"               : self.setMainTitle

            , "headerDBMenuList"        : self.setHeaderDBMenuList()
            , "headerNotificationList"  : self.setHeaderNotificationList()
            , "searchNavi"              : self.searchNavi()

            , "indexTitle"              : self.setIndexTitle
            , "indexSubTitle"           : self.setIndexSubTitle
            , "indexImage"              : self.setIndexImage
            , "indexCategory"           : self.setIndexCategory()

            , "mainLogName"             : self.setMainLogName
            , "footerInfo"              : self.setFooterInfo()

        })

        return html


    def menuMega(self):
        HTML = PAGE_NAVI_MEGA.HTML()
        result = HTML.menuMega()

        return result


"""

print('Content-Type: text/html; charset=utf-8\n')
AAA = MAIN()
print(AAA.render())


"""

