#!/usr/local/bin/python3

import os, sys, io, cgi , datetime



class PAGE_BASE:
    def __init__(self):
        self.setTemplateHTML = r'LIB_JINJA2/page_without_sidebar.html'
        self.setTemplateHTML = r'LIB_JINJA2/extra_404_error.html'
        self.setTemplateHTML = r'LIB_JINJA2/BASE_PAGE_level2.html'

        self.JINJA_FILEPATH = "./../"

        self.setTitle = "AAAA"
        self.setMainTitle = "OUTLINER"
        self.dbName = ""
        self.DBPATH = "./db"

        self.isLOGIN = "0"
        self.isDEBUG = "0"
        self.isPAGE_LOCK = "0"
        self.hasBBS = "0"
        self.hasMEMO = "0"
        self.hasPAGE = "0"
        self.hasLOGIN_CHECK = "0"

        self.LOGIN_USER = ""

        self.MEMO_DB_tableName = "MEMO_base"

        self.setIndexSubTitle = "BBB"
        self.setIndexImage = "../assets/img/user/user-9.jpg"
        self.bodyPre = ""
        self.mainLogName = "AMOISOO"

        if (os.path.basename(__file__) == "index.py"):self.sethomeAddress = r"./"
        else:self.sethomeAddress = r"./" + os.path.basename(__file__)


        self.init()

    def init(self):
        # -----------------------------------------------------
        form = cgi.FieldStorage()
        self.getDBName = form.getvalue('book', '')
        self.getPAGEName = form.getvalue('page', '')
        self.getTYPE = form.getvalue('type', '')
        # -----------------------------------------------------
        if (self.getDBName != ""):      self.dbName = self.getDBName
        if (self.getPAGEName != ""):    self.pageName = "page_" + self.getPAGEName

        # -----------------------------------------------------
        if (self.getDBName == ""):
            self.setIndexTitle = self.dbName
        else:
            self.setIndexTitle = self.getDBName

        self.IMAGE_DB_NAME = self.dbName  # "AfterEffectsEffects"




    def head(self):
        pass

    def bodyNoSel(self):
        html = ""

        getList = os.listdir(path=self.DBPATH)
        getList.sort()
        fileBase = """ <a href="%s?book=%s"><h4>%s</h4></a> """
        html += "<br>"
        for i in getList:
            if (i[-5:] != ".txml"): continue
            if (i[0:2] == "._"): continue

            fileName = i.split(".")[0]
            html += fileBase % (self.sethomeAddress, fileName, fileName) + ""

        return html

    def COOK_init(self):
        html = """
            <script language="javascript">

                document.cookie = "amoisoo_logins_key=%s;"
                document.cookie = "amoisoo_logins_exp=%s;"
                document.cookie = "amoisoo_logins_user=%s;"
            </script>
        """
        import datetime

        #getUSER = self.LOGIN.CMD_SINGLE_USER(get_username)

        #getSession = self.SESSION.CMD_INSERT_SESSION(setUSERNAME)
        getDate = datetime.datetime.now()
        setDate = str(getDate).split(".")[0]

        sessionUUID = "12345"

        return html  % (sessionUUID, setDate ,self.dbName)

    def COOKIE_info(self):
        html = "cookie"
        #print(os.environ["HTTP_COOKIE"])

        if "HTTP_COOKIE" in os.environ:
            html =  os.environ["HTTP_COOKIE"]
        else:
            html =  "NO Cookie"

        return html

    def COOKIE_init(self):
        print("Set-Cookie:amoisoo_logins_key=%s;" % "UUID" )
        print("Set-Cookie:amoisoo_logins_user=%s;" % "USERNAME" )
        print("Set-Cookie:amoisoo_logins_exp=%s;" % self.dbName )

    def COOKIE_check(self):

        # has cookie
        if "HTTP_COOKIE" in os.environ:
            getcookie = os.environ["HTTP_COOKIE"]
            cookieList = getcookie.split(";")
            html = ""
            hasCookieUUID = ""
            hasCookieUSER = ""
            hasCookieSession = ""

            COOKIE_LIST = {}

            for i in cookieList:
                getItem = i.split("=")
                html += str(getItem) + "<br>"
                cookieTitle = getItem[0].replace(" ", "")
                if (cookieTitle == "amoisoo_logins_key"):
                    hasCookieUUID = "1"
                    COOKIE_LIST["amoisoo_logins_key"] = getItem[1]

                if (cookieTitle == "amoisoo_logins_user"):
                    hasCookieUSER = "1"
                    COOKIE_LIST["amoisoo_logins_user"] = getItem[1]

                if (cookieTitle == "amoisoo_logins_exp"):
                    hasCookieSession = "1"
                    COOKIE_LIST["amoisoo_logins_exp"] = getItem[1]


            # has key
            if (hasCookieUUID == "1" and hasCookieUSER == "1" and hasCookieSession == "1"):
                html += "have Cookie"
                html += str(COOKIE_LIST)

                # no value
                if( COOKIE_LIST["amoisoo_logins_key"] == "" or COOKIE_LIST["amoisoo_logins_user"] == "" or COOKIE_LIST["amoisoo_logins_exp"] == "" ):
                    html += """
                    <script language="javascript">

                    setTimeout("location.href='./?type=login'",100)
                    </script>
                    """
                    return [1, html]

                # ok : compare - cookie and db session compare
                #else:return [0, html]

            # no has key
            else:
                html += "<h3>has not Cookie</h3> "
                html += """<h4>COOKIE : %s</h4>""" % (getcookie)
                html += """<h4>COOKIE : %s</h4>""" % (cookieList)
                html += """<h4>UUID : %s</h4>""" % (hasCookieUUID)
                html += """<h4>USER : %s</h4>""" % (hasCookieUSER)
                html += """<h4>SESSION : %s</h4>""" % (hasCookieSession)

                html += """<h3>%s</h3>""" % (self.COOKIE_info())
                html += """
                <script language="javascript">

                setTimeout("location.href='./?type=login'",100)
                </script>

                """
                return [1, html]

            #---------------------------------------------------------------------
            # COMPARE
            #---------------------------------------------------------------------
            HOST = "amoisoo.com"
            USER = "conie6mm"
            PASSWORD = "Leekyou7811#"
            DBNAME = "user.amoisoo.com"
            SESSION_TIME = 10  # unit is minite # PUBLIC_ENV.SESSION_TIME
            getPath = os.path.dirname(os.path.abspath(__file__))
            getPath = os.path.dirname(getPath) + "/LIB_COMMON"
            sys.path.append(getPath)

            html += getPath
            import LOGIN_SESSION
            SESSION = LOGIN_SESSION.SESSION(HOST, USER, PASSWORD, DBNAME, SESSION_TIME)
            COOKIE_LIST["amoisoo_logins_key"]


            try:
                #getSession = SESSION.CMD_SESSION_REFRESH_NAME(COOKIE_LIST["amoisoo_logins_user"])
                getSession = SESSION.CMD_SINGLE_SESSION(COOKIE_LIST["amoisoo_logins_key"])
                # getSession = SESSION.CMD_SESSION_REFRESH("e4227fbf_9d60_4357_b3d7_035921f76e9f")

                session_UUID = getSession[1]
                session_data = getSession[2] # email
                session_date = getSession[3]
                html = ""

                sessionTime = getSession[3].replace(" ", "")
                currentTime = str(datetime.datetime.now()).split(".")[0].replace(" ", "")
                getLoginExp = COOKIE_LIST["amoisoo_logins_exp"]
                if (getLoginExp  < sessionTime and currentTime < sessionTime):
                    html = "time ok<br>" + currentTime + "<br>"+ sessionTime
                    self.isLOGIN == "1"
                    self.LOGIN_USER = COOKIE_LIST["amoisoo_logins_user"]
                    SESSION.CMD_SESSION_REFRESH(COOKIE_LIST["amoisoo_logins_key"])

                else:
                    html = "time out"
                    html += """
                    <script language="javascript">
                    setTimeout("location.href='./?type=login'",100)
                    </script>
    
                    """
                    return [1, html]
            except:
                html += """
                <script language="javascript">
                setTimeout("location.href='./?type=login'",100)
                </script>

                """
                return [1, html]


            return [0, html]

        else:
            html = "NO Cookie"
            html += """<h3>%s</h3>""" % (self.COOKIE_info())
            html += """
            <script language="javascript">
            setTimeout("location.href='./?type=login'",100)
            </script>

            """
            return [1, html]

    def bodyMain(self):
        html = ""
        #----------------------------------
        if(self.hasLOGIN_CHECK == "1"):
            cookieCheck = self.COOKIE_check()
            if(cookieCheck[0]== 1):
                return cookieCheck[1]
            elif(cookieCheck[0]== 0):
                html += """<div align = "right" >%s</div>""" % self.LOGIN_USER+ "<br>"
                html += cookieCheck[1]


        #----------------------------------

        #html += """<br><br>123<br><br><br><br><h4>%s</h4>""" % (self.COOKIE_info())



        if (self.havPAGE == "0"):
            html += "<br> NOPAGE </br>"
            self.setTemplateHTML = r'LIB_JINJA2/extra_404_error.html'
            return html
        elif (self.havPAGE == "2"):
            html += self.bodyNoSel()
            return html

        # import OUTLINER_IO_TREE
        # O_TREE = OUTLINER_IO_TREE.IO_IMPORT()
        # DATA_text = O_TREE.IO_DATA_reOrder( "html5.txml"  , "0")
        # DATA_MAIN = DATA_text[0]
        # DATA_CHILD = DATA_text[1]

        breadCrumbBase = """
			<ol class="breadcrumb pull-right">
                <li class="breadcrumb-item"><a href="%s?book=%s">%s</a></li>
                %s
			</ol>
        """

        breadCrumbBaseItem = """ <li class="breadcrumb-item"><a href="javascript:;">%s</a></li> """
        breadCrumbBaseItemList = ""

        try:
            self.SELLIST_TITLE.reverse()
            for i in self.SELLIST_TITLE:
                breadCrumbBaseItemList += breadCrumbBaseItem % (i)

            html += breadCrumbBase % (self.sethomeAddress , self.dbName, self.dbName, breadCrumbBaseItemList)

            if (self.getPageDATA[13][0] == ""):
                setSubTitle = ""
            else:
                setSubTitle = " - " + self.getPageDATA[13][0]

            html += """ <h1 class="page-header">%s <small> %s</small></h1> """ % (
            str(self.getPageDATA[0][0]), setSubTitle)
            # html += str(self.SELLIST)

            html += "<hr>"
        except:
            pass

        if (self.SELLIST == []):
            return "NO Sel"

        if(self.isPAGE_LOCK == "1"):
            return "<h2>PAGE LOCK</h2>"


        COMP = self.getPageDATA[10]
        CONTEXT = self.getPageDATA[11]

        if (COMP == "File" and CONTEXT == "TABPAGE"):
            # html += str(self.getPageDATA[14]) + "<br><br><hr>"
            import OUTLINER_FILE_PAGE
            OUTLINER = OUTLINER_FILE_PAGE.OUTLINER()
            html += OUTLINER.render(self.getPageDATA[14], "1" , self.IMAGE_DB_NAME)

        elif ((COMP == "File" and CONTEXT == "TREE") or (COMP == "File" and CONTEXT == "LIST")):
            # html += "TREE"
            import OUTLINER_IO_TREE
            O_TREE = OUTLINER_IO_TREE.IO_IMPORT()
            DATA_text = O_TREE.IO_DATA_reOrder(self.getPageDATA[14], "1")
            DATA_MAIN = DATA_text[0]
            DATA_CHILD = DATA_text[1]

            import OUTLINER_FILE_PAGE_COMP
            COMP_TREE = OUTLINER_FILE_PAGE_COMP.HTML()
            COMP_TREE.setDBName = self.IMAGE_DB_NAME
            html += COMP_TREE.render(DATA_MAIN, DATA_CHILD , "aaa")



        elif (COMP == "File" and CONTEXT == "TABLE"):
            # html += "TABLE<br>"
            import OUTLINER_IO_TABLE
            TABLE = OUTLINER_IO_TABLE.FILE_TABLE()
            # html += self.getPageDATA[14]
            # Note 14 - data position is 31
            DATA_table = TABLE.HTML_TABLE_BODY(self.getPageDATA[31], "1", "-1", "0")
            html += (DATA_table[0])

            if (DATA_table[1] != ""): # setNote
                html += ("<br>" + DATA_table[1])


        elif (COMP == "File" and CONTEXT == "html"):
            html += "html"
        elif (COMP == "File" and CONTEXT == "plain"):
            # html += "plain"

            getText = self.getPageDATA[16]
            stringList = getText.split("\n")

            for i in stringList:
                html += i + "<br>"
            html += "<hr>"

        # html += OUTLINER.render( self.dbName )


        reuslt = html

        if(self.hasBBS == "1"):
            reuslt += self.BODY_BBS()
        if(self.hasPAGE == "1"):
            reuslt += self.BODY_PAGE()

        return reuslt

    def BODY_BBS(self):
        if(self.hasLOGIN_CHECK == "0"): return ""

        if (self.LOGIN_USER != ""):
            import BBS_PAGE_COLOR
            BBS = BBS_PAGE_COLOR.HTML()
            result = BBS.BODY_BBS(self.dbName, self.getPAGEName)
            return result
        else:
            return ""
    def BODY_PAGE(self):



        if(self.LOGIN_USER == "lee@amoisoo.com" or self.hasLOGIN_CHECK == "0"):

            result = ""

            setAJAX = "" """AJAX_PAGE_BASE( '../ajax/color_page/page_list.py' , 'memo.amoisoo.com' , '%s', '%s' )""" % (self.dbName, self.getPAGEName)
            result += """ <button class="btn btn-success btn-xs" onclick="%s" > PAGE LIST</button>  """ % setAJAX

            setScriptExcute = """ <script> %s ; </script> """ % setAJAX
            result +=setScriptExcute

            setAJAX = "" """AJAX_PAGE_BASE( '../ajax/color_page/page_form_new.py' , 'memo.amoisoo.com' , '%s', '%s' )""" % (self.dbName, self.getPAGEName)
            result += """ <button class="btn btn-success btn-xs" onclick="%s" > NEW</button>  """ % setAJAX

            return result
        else:
            return ""

    def BODY_BBS_oldDELTE(self):

        reuslt = """
			<div class="row">
			    <!-- begin col-6 -->
			    <div class="col-lg-12">
			        <!-- begin panel -->
			        <div class="panel panel-inverse" data-sortable-id="ui-media-object-1">
                        <!-- begin panel-heading -->
                        <div class="panel-heading">
                            <div class="panel-heading-btn">
                                <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-default" data-click="panel-expand"><i class="fa fa-expand"></i></a>
                                <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-success" data-click="panel-reload"><i class="fa fa-redo"></i></a>
                                <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-warning" data-click="panel-collapse"><i class="fa fa-minus"></i></a>
                                <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-danger" data-click="panel-remove"><i class="fa fa-times"></i></a>
                            </div>
                            <h4 class="panel-title">Default Media Object</h4>
                        </div>
                        <!-- end panel-heading -->
                        <!-- begin panel-body -->
                        <div class="panel-body">
							<div class="media media-sm">
								<a class="media-left" href="javascript:;">
									<img src="../assets/img/user/user-1.jpg" alt="" class="media-object" />
								</a>
								<div class="media-body">
									<h4 class="media-heading">Media heading</h4>
									<p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla.</p>
								</div>
							</div>
							<div class="media media-sm">
								<a class="media-left" href="javascript:;">
									<img src="../assets/img/user/user-2.jpg" alt="" class="media-object" />
								</a>
								<div class="media-body">
									<h4 class="media-heading">Media heading</h4>
									<p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla.</p>
									<div class="media">
										<a class="pull-left" href="javascript:;">
										    <img src="../assets/img/user/user-3.jpg" alt="" class="media-object" />
									    </a>
										<div class="media-body">
											<h4 class="media-heading">Nested media heading</h4>
											<p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla.</p>
										</div>
									</div>
								</div>
							</div>
							<div class="media media-sm">
								<a class="media-left" href="javascript:;">
									<img src="../assets/img/user/user-4.jpg" alt="" class="media-object" />
								</a>
								<div class="media-body">
									<h4 class="media-heading">Media heading</h4>
									<p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla.</p>
								</div>
							</div>
							<div class="media media-sm">
								<a class="media-left" href="javascript:;">
									<img src="../assets/img/user/user-10.jpg" alt="" class="media-object" />
								</a>
								<div class="media-body">
									<h4 class="media-heading">Media heading</h4>
									<p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla.</p>
								</div>
							</div>
						</div>
						<!-- end panel-body -->
                    </div>
			        <!-- end panel -->
				</div>
			    <!-- end col-6 -->
			    <!-- begin col-6 -->
			    <!-- end col-6 -->
			</div>
        """

        return reuslt


    def naviHtml(self):
        html = ""
        itemMenu = """


                %s 

        """
        itemBaseList = ""

        itemBase = """ <li><a href="./?book=%s">%s</a></li> """

        getList = os.listdir(path='.')



        import OUTLINER_IO_TREE
        O_TREE = OUTLINER_IO_TREE.IO_IMPORT()
        DATA_text = O_TREE.IO_DATA_reOrder((self.DBPATH + "/" + self.dbName + ".txml"), "0")
        DATA_MAIN = DATA_text[0]
        DATA_CHILD = DATA_text[1]
        DATA_allList = DATA_text[2]

        # breadcrumb = O_TREE.getBreadcrumb(DATA_allList , "bfdfab16_7d52_4af5_8de3_697ed5bd8fd8" )
        self.SELLIST = []
        self.SELLIST_TITLE = []
        if (self.getPAGEName != ""):

            getPage = self.getPAGEName.split("page_")

            self.havPAGE = O_TREE.havePAGE(DATA_allList, getPage[1])

            if (self.havPAGE == "1"):
                getTREEBread = O_TREE.getBreadcrumb(DATA_allList, getPage[1])
                self.SELLIST = getTREEBread[0]
                self.SELLIST_TITLE = getTREEBread[1]
                self.getPageDATA = O_TREE.getDATA(DATA_allList, getPage[1])

        else:
            self.havPAGE = "2"

        import OUTLINER_FILE_NAVI
        NAVIMENU = OUTLINER_FILE_NAVI.HTML()
        naviMenuResult = NAVIMENU.render(DATA_MAIN, DATA_CHILD, self.SELLIST, self.dbName, self.sethomeAddress)

        return itemMenu % (naviMenuResult)

    def setFooterInfo(self):
        from datetime import datetime
        # <a href = "../" > HOME </a><>
        setFooterInfo = """
            <br><br><br><br><br>
            <br><br><br><br><br>
            <div id="footer" class="footer">
                <a href = "../" > MAIN INDEX </a>
                &nbsp;&nbsp;&nbsp;&nbsp; %s 
                &nbsp;&nbsp;&nbsp;&nbsp; %s 
                &nbsp;&nbsp;&nbsp;&nbsp; %s 
                &nbsp;&nbsp;&nbsp;&nbsp; %s <br>
                
                &copy; amoisoo - All Rights Reserved
                <br> MAIL : <a href="mailto:contact@amoisoo.com">contact@amoisoo.com</a>
                <br>%s  -  %s (JST, +0900)
                
            </div>
            <br><br>
        """



        year = datetime.now().strftime("%Y-%m-%d")
        setTime = datetime.now().strftime("%H:%M:%S")

        setAJAX = "" """AJAX_SEND_MAIL_BASE( '../ajax/bbs/form_supportMail.py' , 'bbs.amoisoo.com' , '%s', '%s' )"""  % (self.dbName, self.getPAGEName)
        sendMail = """ <a  href="#" onclick="%s" > Support Mail</a>  """ % setAJAX

        setAJAX = "" """AJAX_MEMO_BASE( '../ajax/bbs/form_memo_list.py' , 'memo.amoisoo.com' , '%s', '%s' )"""  % (self.MEMO_DB_tableName, self.getPAGEName)
        setMEMO = """ <a href="#" onclick="%s" > Memo</a>  """ % setAJAX

        register = """ <a href= "./?type=register"> Register </a> """

        if(self.isLOGIN == "0"):
            login = """ <a href= "./?type=logout"> Logout </a> """

        elif (self.isLOGIN == "1"):
            login = """ <a href= "./?type=login"> Login </a> """

        result = setFooterInfo % ( "" , "","" , "",  year, setTime )


        return result

    def setHeaderDBMenuList(self):
        setHeaderDBMenuList = """
            <a href="./" class="dropdown-item">Home</a>
                    <div class="dropdown-divider"></div>
            <a href="./css3.py" class="dropdown-item"><span class="badge badge-primary pull-right"></span>CSS3</a>
            <a href="./html5.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>HTML5</a>
            <a href="./js.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>JavaScripts</a>
            <a href="./web.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>Web</a>


                    <div class="dropdown-divider"></div>
            <a href="./cg.py" class="dropdown-item"><span class="badge badge-primary pull-right"></span>CG</a>
            <a href="./maya.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>maya</a>
            <a href="./adobe.py" class="dropdown-item">Adobe</a>

                    <div class="dropdown-divider"></div>
            <a href="./iphone.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>iPhone</a>
            <a href="./swift.py" class="dropdown-item"><span class="badge badge-danger pull-right">2</span>Swift</a>
                    <div class="dropdown-divider"></div>

            <a href="./linux.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>Linux</a>
            <a href="./python.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>Python</a>
            <a href="./dev.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>Dev</a>
            <a href="./qt.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>Qt</a>



                    <div class="dropdown-divider"></div>




            <a href="./mac.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>mac</a>
                    <div class="dropdown-divider"></div>

            <a href="./outliner.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>Outliner</a>

                    <div class="dropdown-divider"></div>
            <a href="./doc.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>Doc</a>
            <a href="./english.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>English</a>
            <a href="./movie.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>movie</a>

            <a href="./physical.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>physical</a>



                    <div class="dropdown-divider"></div>
            <a href="./game.py" class="dropdown-item"><span class="badge badge-danger pull-right"></span>Game</a>

        """

        return setHeaderDBMenuList

    def menuMega(self):
        import PAGE_NAVI_MEGA
        HTML = PAGE_NAVI_MEGA.HTML()
        result = HTML.menuMega()

        return result

    def setIndexCategory(self):

        setIndexCategory = """ <li><a href="%s"><i class="fa fa-cog"></i> %s </a></li> """ % (
        self.sethomeAddress + "?book=Painter", "Painter 2018")
        setIndexCategory += """ <li><a href="%s"><i class="fa fa-cog"></i> %s </a></li> """ % (
        self.sethomeAddress + "?book=PainterBrushUltimate", "Painter Brush Ultimate")

        return setIndexCategory

    def setHeaderNotificationList(self):
        if(self.hasMEMO == "0"):
            return ""
        elif(self.hasMEMO == "1") :
            import BBS_PAGE_COLOR
            BBS = BBS_PAGE_COLOR.HTML()

            result = ""
            result += BBS.setHeaderNotificationList(self.MEMO_DB_tableName , self.getPAGEName)
            return result

    def setHeaderNotificationList_oldDelete(self):
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

    def setNaviSideBar(self):
        setNaviSideBar = """
            <!-- begin sidebar minify button -->
            <li><a href="javascript:;" class="sidebar-minify-btn" data-click="sidebar-minify"><i class="fa fa-angle-double-left"></i></a></li>
            <!-- end sidebar minify button -->
        """
        return setNaviSideBar

    def render(self , PAGE_TYPE = "0"):

        from jinja2 import Environment, FileSystemLoader

        env = Environment(loader=FileSystemLoader(self.JINJA_FILEPATH, encoding='utf8'))

        tpl = env.get_template(self.setTemplateHTML)



        if(self.getTYPE == "login"):

            html = tpl.render({
                'shop': 'ddd'
                , "init_BODY": self.LOGIN()
            })
        elif(self.getTYPE == "logout"): # logout
            html = tpl.render({
                'shop': 'ddd'

                , "init_BODY": self.LOGOUT()

            })
        elif(self.getTYPE == "register"): # blank page
            html = tpl.render({
                'shop': 'ddd'

                , "init_BODY": self.REGISTER()

            })

        elif(PAGE_TYPE == "1" or self.getTYPE == "blank"): # blank page
            html = tpl.render({
                'shop': 'ddd'

                , "cookie":    ""# self.COOK_init()

                #------------------------------
                , "init_NAVI": self.init_HTML_NAVI_type2()
                , "init_BODY": self.init_HTML_BODY_type2()
                #------------------------------
                , "homeAddress": self.sethomeAddress
                # ------------------------------
                , "footerInfo": self.setFooterInfo()
            })
        elif(PAGE_TYPE == "0" ): # blank page
            html = tpl.render({
                'shop': 'ddd'

                , "cookie":    ""# self.COOK_init()

                #------------------------------
                , "init_HEADER": self.init_HTML_HEADER()
                , "init_NAVI": self.init_HTML_NAVI()
                , "init_BODY": self.init_HTML_BODY()
                #------------------------------
                , "homeAddress": self.sethomeAddress
                # ------------------------------
                , "footerInfo": self.setFooterInfo()

            })




        #print("Set-Cookie: domain=.mac.amoisoo.com;colorpage=%s;" % self.dbName)
        #print("Set-Cookie: colorpage=%s;" % self.dbName )

        #self.COOKIE_init()


        print("Content-type: text/html\n")

        return html

    def LOGOUT(self):
        html = """
        <script>
                document.cookie = "amoisoo_logins_key=;"    ;
                document.cookie = "amoisoo_logins_user=;"    ;
                document.cookie = "amoisoo_logins_exp=;"   ;
                setTimeout("location.href='./?type=login'",1000);
        </script>
        
    <div id="page-container" class="fade">
        <!-- begin login -->

        <h3>%s </h3>

        <div class="login bg-black animated fadeInDown">
            <!-- begin brand -->

            <div class="login-header">
                <div class="brand">

                    <a href="./"> <span class="logo"></span>  </a>
                    <b>AMOISOO</b> LOGOUT
                    <small>   </small>
                </div>
                <div class="icon">
                    <i class="fa fa-lock"></i>
                </div>
            </div>
            <!-- end brand -->
            <!-- begin login-content -->
            <div class="login-content">

              <br> 다시 로그인하<a href="./?type=login"> Login</a> 


            </div>
            <!-- end login-content -->
        </div>
        <!-- end login -->


        <!-- begin theme-panel -->
        <!-- end theme-panel -->
    </div>

        """
        cookieInfo = ""
        if(self.isDEBUG  == "1"):
            cookieInfo = self.COOKIE_info()

        return html % cookieInfo

    def LOGIN(self):
        html = """
    <div id="page-container" class="fade">
        <!-- begin login -->
        
        <h3>%s </h3>

        <div class="login bg-black animated fadeInDown">
            <!-- begin brand -->
            
            <div class="login-header">
                <div class="brand">
                     
                    <a href="./"> <span class="logo"></span>  </a>
                    <b>AMOISOO</b> LOGIN
                    <small>   </small>
                </div>
                <div class="icon">
                    <i class="fa fa-lock"></i>
                </div>
            </div>
            <!-- end brand -->
            <!-- begin login-content -->
            <div class="login-content">

                <form action="#" method="POST" class="margin-bottom-0">
                    <div class="form-group m-b-20">
                        <input id="login_email" name="login_email" type="text" class="form-control form-control-lg inverse-mode" placeholder="Email Address" required />
                    </div>
                    <div class="form-group m-b-20">
                        <input id="login_password"  name="login_password" type="password" class="form-control form-control-lg inverse-mode" placeholder="Password" required />
                    </div>
                    
                    
                    <div class="LOGIN_MESSAGE" id="LOGIN_MESSAGE">
                    
                              
                            

                    </div>
                    
                    

                            <br>Already a member? Click <a href="./?type=register">here</a> to register.
                </form>

                        <br> %s
            </div>
            <!-- end login-content -->
        </div>
        <!-- end login -->


        <!-- begin theme-panel -->
        <!-- end theme-panel -->
    </div>

        """
		#AJAX_LOGIN_APPLY(address, setSchema, dbName, setUUID)
        import base64

        cookieInfo = ""
        if(self.isDEBUG  == "1"):
            cookieInfo = self.COOKIE_info()

        try:
            COOKIE = os.environ["HTTP_COOKIE"]
            data = base64.b64encode(COOKIE.encode('utf-8'))
            setCOOKIE = data.decode('utf-8')
        except:
            setCOOKIE = ""
        setAJAX = "" """AJAX_LOGIN_APPLY( '../ajax/login/login.py' , '%s' , '%s', '%s' )"""  % (setCOOKIE ,  "", "")
        CHECK = """ <button class="btn btn-success  btn-block btn-lg" onclick="%s" > Login</button>  """ % setAJAX


        return html % ( cookieInfo  , CHECK)

    def REGISTER(self):
        html = """
	<div id="page-container" class="fade">
	    <!-- begin register -->
        <div class="register register-with-news-feed">
            <!-- begin news-feed -->
            <div class="news-feed">
                <div class="news-image" style="background-image: url(%s)"></div>
                <div class="news-caption">
                    <h4 class="caption-title"><b>AMOISOO</b> Register</h4>
                    <p>
                        유저등록 
                    </p>
                </div>
            </div>
            <!-- end news-feed -->
            <!-- begin right-content -->
            <div class="right-content">
                <!-- begin register-header -->
                <h1 class="register-header">
                    Sign Up
                    <small>  <a href="./">HOME</a>  </small>
                </h1>
                <!-- end register-header -->
                <!-- begin register-content -->
                <div class="register-content">
                    <form action="../ajax/login/register_apply.py" method="POST" class="margin-bottom-0">
                        <label class="control-label">Name <span class="text-danger">*</span></label>
                        <div class="row row-space-10">
                            <div class="col-md-12 ">
                                <input type="text" name="reg_username" class="form-control" placeholder="User name" required />
                            </div>

                        </div><br>

                        <label class="control-label">Email <span class="text-danger">*</span></label>
                        <div class="row m-b-15">
                            <div class="col-md-12">
                                <input type="text" name="reg_email" class="form-control" placeholder="Email address" required />
                            </div>
                        </div>



                        <label class="control-label">Password <span class="text-danger">*</span></label>
                        <div class="row m-b-15">
                            <div class="col-md-12">
                                <input type="password" name="reg_password" class="form-control" placeholder="Password" required />
                            </div>
                        </div>

                        <label class="control-label">Re-enter Password <span class="text-danger">*</span></label>
                        <div class="row m-b-15">
                            <div class="col-md-12">
                                <input type="password" name="reg_password_re" class="form-control" placeholder="Re-enter Password" required />
                            </div>
                        </div>

                        <div class="checkbox checkbox-css m-b-30">
                        	<div class="checkbox checkbox-css m-b-30">
								<input type="checkbox" id="agreement_checkbox" value="">
								<label for="agreement_checkbox">
									By clicking Sign Up, you agree to our <a href="javascript:;">Terms</a> and that you have read our <a href="javascript:;">Data Policy</a>, including our <a href="javascript:;">Cookie Use</a>.
								</label>
							</div>
                        </div>
                        <div class="register-buttons">
                            <button type="submit" class="btn btn-primary btn-block btn-lg">Sign Up</button>
                        </div>
                        <div class="m-t-20 m-b-40 p-b-40 text-inverse">
                            Already a member? Click <a href="./?type=login">here</a> to login.
                            
                            
                            <br>
                            %s
                            
                            <h3> %s </h3>
                        </div>
                        <hr />
                        <p class="text-center">
                            &copy; AMOISOO All Right Reserved 2018
                            
                            
                        </p>
                    </form>
                </div>
                <!-- end register-content -->
            </div>
            <!-- end right-content -->
        </div>
        <!-- end register -->
        

	</div>

        """
        import random
        getNum = random.randint(1, 17)

        backImage = "../assets/img/login-bg/login-bg-%s.jpg" % getNum

        #setCookie = """ <h4>%s<h4> """ % (self.COOKIE())
        #cookieInfo = str(getNum) + "" + self.COOKIE_SET()  + setCookie

        cookieInfo = ""
        if(self.isDEBUG  == "1"):
            cookieInfo = self.COOKIE_info()
        return html % (backImage , "" ,  cookieInfo)


    def init_HTML_NAVI_type2(self):
        html = """


        """






        setNAVE         = self.naviHtml()




        return html

    def init_HTML_BODY_type2(self):
        # <div id="content"  class="content" ">
        #
        html = """
	<div id="page-container" class="fade page-without-sidebar page-header-fixed">

		<div id="content" class="content">

			%s

			%s

			<div id = "view_body"></div>

			<div id = "view_bbs"></div>


		</div>
		

		<a href="javascript:;" class="btn btn-icon btn-circle btn-success btn-scroll-to-top fade" data-click="scroll-top"><i class="fa fa-angle-up"></i></a>
	</div>

        """


        bodyPre = self.bodyPre
        outliner = self.bodyMain()
        setValue = ( bodyPre , outliner )

        return html% setValue


    def init_HTML_HEADER(self):
        html = """
        <!-- begin #header -->
		<div id="header" class="header navbar-default">
			<!-- begin navbar-header -->
			<div class="navbar-header">


				<a href="%s" class="navbar-brand"><span class="navbar-logo"></span> <b> %s </b> %s </a>
				<button type="button" class="navbar-toggle" data-click="sidebar-toggled">
					<span class="icon-bar">aa</span>
					<span class="icon-bar">bb</span>
					<span class="icon-bar">cc</span>
				</button>
				
			</div>
			<!-- end navbar-header -->



			%s



			<!-- begin header-nav -->
			<ul class="navbar-nav navbar-right">
				%s

				%s

				<li class="dropdown navbar-user">
					<a href="javascript:;" class="dropdown-toggle" data-toggle="dropdown">
						<img src="../assets/img/user/user-14.jpg" alt="" />
						<span class="d-none d-md-inline">%s</span> <b class="caret"></b>
					</a>
					<div class="dropdown-menu dropdown-menu-right">
						%s
					</div>
				</li>

			</ul>
			<!-- end header navigation right -->

		</div>
		<!-- end #header -->
        """


        homeAddress                 = self.sethomeAddress
        mainLogName                 = self.mainLogName
        mainTitle                 = self.setMainTitle
        naviMenuMega                = self.menuMega()
        searchNavi                  = self.searchNavi()
        headerNotificationList      = self.setHeaderNotificationList()
        headerDBMenuList            = self.setHeaderDBMenuList()
        loginName                   = self.LOGIN_USER
        setValue = ( homeAddress , mainLogName , mainTitle , naviMenuMega , searchNavi, headerNotificationList, loginName,  headerDBMenuList )

        return html % setValue

    def init_HTML_NAVI(self):
        html = """

		<!-- begin #sidebar -->
		<div id="sidebar" class="sidebar">
			<!-- begin sidebar scrollbar -->
			<div data-scrollbar="true" data-height="100%s">
				<!-- begin sidebar user -->
				<ul class="nav">
					<li class="nav-profile">
						<a href="javascript:;" data-toggle="nav-profile">
							<div class="cover with-shadow"></div>
							<div class="image">
								<img src="%s" alt="" />
							</div>
							<div class="info">
								<b class="caret pull-right"></b>
								%s
								<small>%s</small>
							</div>
						</a>
					</li>
					<li>
						<ul class="nav nav-profile">
							%s
                        </ul>
					</li>
				</ul>
				<!-- end sidebar user -->
				<!-- begin sidebar nav -->
				<ul class="nav">
					<li class="nav-header">INDEX</li>
                    %s

                    %s
				</ul>

				<!-- end sidebar nav -->
			</div>
			<!-- end sidebar scrollbar -->
		</div>
		<div class="sidebar-bg"></div>
		<!-- end #sidebar -->
        """


        setIndexImage   = self.setIndexImage
        indexTitle      = self.setIndexTitle
        indexSubTitle   = self.setIndexSubTitle
        indexCategory   = self.setIndexCategory()
        setNAVE         = self.naviHtml()

        naviSideBar     = self.setNaviSideBar()

        setValue = ("%", setIndexImage , indexTitle ,  indexSubTitle , indexCategory, setNAVE , naviSideBar)



        return html % setValue
    def init_HTML_BODY(self):
        html = """
		<!-- begin #content -->
		<div id="content" class="content">

			%s

			%s

			<div id = "view_body"></div>

			<div id = "view_bbs"></div>


		</div>
		<!-- end #content -->

        """


        bodyPre = self.bodyPre
        outliner = self.bodyMain()
        setValue = ( bodyPre , outliner )

        return html % setValue
