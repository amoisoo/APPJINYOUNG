import os, sys , io , cgi
class HTML:
    def __init__(self , setHomeAddress = "" ):
        #super(HTML, self).__init__()
        self.sethomeAddress = ""
        self.mainLogName = "MEMO &nbsp;"

    def setHeaderNotificationList(self, TABLENAME, getPAGEName):

        bodyBase = """
        <li class="dropdown"  >
            <a href="javascript:;" data-toggle="dropdown" class="dropdown-toggle f-s-14"><i class="fa fa-bell"></i><span class="label">%s</span></a>

            <ul class="dropdown-menu media-list dropdown-menu-right"  style = "width : 400px;" >
                        %s



                        %s
                            %s
                        %s
            </ul>
        </li>

        """

        baseItem = """
                <li class="media">
                    <a href="javascript:;">
                            %s

                        <div class="media-body">
                            %s

                        </div>
                    </a>
                </li>
        """

        itemList = ""

        urlMEMOE = """ <li class="dropdown-footer text-center"><a href="./memo/new.py?book=%s&page=%s">Write</a></li> """ % (TABLENAME , getPAGEName)
        urlMEMOLIST = """ <li class="dropdown-footer text-center"><a href="./memo/?book=%s&page=%s">List</a></li> """ % (TABLENAME , getPAGEName)

        getRecord = self.MEMO_LIST(TABLENAME)
        listCount = str(len(getRecord))
        self.memoViewCount = 6
        self.memoLargeView = 4

        if (getRecord == []):
            result = bodyBase % ("0", urlMEMOE, "", itemList, urlMEMOLIST)

            return result

        getRecord.reverse()

        for index, i in enumerate(getRecord):
            if (index == self.memoViewCount): break
            leftItem = """
                        <div class="media-left">
                            <i class="fa fa-bug media-object bg-silver-darker"></i>
                        </div>
            """
            leftItem = ""

            titleIcon = """ <i class="fa fa-exclamation-circle text-danger"></i>  """
            title = """ <h6 class="media-heading">%s %s</h6> """
            setTitle = title % (i[1], "")

            setMemo = "<p>%s</p>" % i[16]
            setTime = """ <div class="text-muted f-s-11">3 minutes ago</div> """
            # setTime = ""

            setInfo = ""
            if (self.memoLargeView >= self.memoViewCount):
                setInfo += setTitle
                # setInfo += setMemo
                setInfo += setTime

            else:
                setInfo += setTitle
                setInfo += """ <div class="text-muted f-s-11">%s</div> """ % (i[34])

            itemList += baseItem % (leftItem, setInfo)

        if (int(listCount) < self.memoViewCount):
            memoCount = """ <li class="dropdown-header">Memo (%s)</li> """ % str(listCount)

        else:
            memoCount = """ <li class="dropdown-header">Memo (%s)</li> """ % str(self.memoViewCount)

        result = bodyBase % (listCount, urlMEMOE, memoCount, itemList, urlMEMOLIST)

        return result

    def BODY_BBS(self, dbName, getPAGEName):

        if(getPAGEName == ""):
            return "No Sel Page "

        # collapse
        #  <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-warning" data-click="panel-collapse"><i class="fa fa-minus"></i></a>
        #  <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-default" data-click="panel-expand"><i class="fa fa-expand"></i></a>
        bodyBASE = ""

        bodyBASE += """
                <script> AJAX_EXE( '../ajax/bbs/bbs.py', 'bbs.amoisoo.com' , '%s' , '%s' )  </script>
        """ % (dbName, getPAGEName)

        # bodyBASE += """ <button onclick="AJAX_EXE( '../ajax/bbs/bbs2.py' , 'Memo')" > bbs2 </button>   """

        newButton = """ <button class="btn btn-success btn-xs" onclick="AJAX_EXE( '../ajax/bbs/form_new.py' , 'bbs.amoisoo.com' , '%s', '%s' )" > New Comment</button>  """ % (
        dbName, getPAGEName)
        # bodyBASE += """ <button onclick="getInfo4( '../ajax/bbs/form.py' , 'memo.amoisoo.com' , '%s' )" > memo form </button>  """ % (dbName)

        # bodyBASE += """ <button onclick="AJAX_EXE( '../ajax/bbs/bbs.py', 'bbs.amoisoo.com' , '%s' )" > bbs list</button>    """ % (dbName)
        # bodyBASE += """ <button onclick="AJAX_EXE( '../ajax/bbs/bbs.py', 'memo.amoisoo.com' , '%s' )" > memo list </button>    """ % (dbName)
        # bodyBASE += """  <button onclick="AJAX_EXE( 'http://book.amoisoo.com/ajax/plaintext.py' ) "> amoisoo plain </button>  """
        # bodyBASE += """  <button onclick="AJAX_EXE( 'http://book.amoisoo.com/ajax/bbs.py')" > amoisoo bbs </button>  """

        refreshButton = """ <a onclick="%s" href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-success" data-click="panel-reload"><i class="fa fa-redo"></i></a> """
        refreshCode = """ AJAX_EXE( '../ajax/bbs/bbs.py', 'bbs.amoisoo.com' , '%s' , '%s') """ % (dbName, getPAGEName)
        setRefreshButton = refreshButton % (refreshCode)

        bodyBASE += """

			<div class="row">
			    <div class="col-lg-12">


			        <div class="panel panel-inverse" data-sortable-id="ui-media-object-1">

                        <div class="panel-heading">
                            <div class="panel-heading-btn">
                                %s 
                            </div>
                            <h4 class="panel-title">%s &nbsp; %s   </h4>
                        </div>

                        <div class="panel-body" id="view">
                            <!-- ----------------------------------------------------- -->
                            %s
                            <!-- ----------------------------------------------------- -->

						</div>
                    </div>
				</div>

			</div>
        """

        baseItem = """
                <div class="media media-sm">
                    <a class="media-left" href="javascript:;">
                        <img src="../assets/img/user/user-4.jpg" alt="" class="media-object" />
                    </a>
                    <div class="media-body">
                        <h4 class="media-heading">Media heading</h4>
                        <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla.</p>
                    </div>
                </div>
        """

        baseItemBody = """
                <div class="media media-sm">
                    <a class="media-left" href="javascript:;">
                        <img   src="../assets/img/user/user-2.jpg" alt="" class="media-object" />
                    </a>
                    <div class="media-body">
                        <h4 class="media-heading">Media heading</h4>
                        <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla.</p>

                        %s
                    </div>
                </div>
        """

        baseItemChild = """
                <div class="media">
                    <a class="pull-left" href="javascript:;">
                        <img   src="../assets/img/user/user-3.jpg" alt="" class="media-object" />
                    </a>
                    <div class="media-body">
                        <h4 class="media-heading">Nested media heading</h4>
                        <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla.</p>

                        %s
                    </div>
                </div>
        """

        itemList = ""

        itemList += baseItemBody % (baseItemChild % (baseItemChild % (baseItemChild % "")))

        itemList += baseItemBody % (baseItemChild % (baseItemChild % ""))
        itemList += baseItemBody % ("")

        itemList += baseItemBody % (baseItemChild % "")

        # itemList += baseItemBody % ( baseItemChild   % baseItemChild )
        itemList += baseItem

        result = bodyBASE % (setRefreshButton, newButton, ("Comments (%s)" % (dbName)), "")

        return result

    def MEMO_LIST(self, TABLENAME="memo2"):

        getPath = os.path.dirname(os.path.abspath(__file__))
        getPath = os.path.dirname(getPath)
        sys.path.append(getPath + "/LIB_COMMON")
        import MYSQL
        HOST = "amoisoo.com"
        USER = "conie6mm"
        PASSWORD = "Leekyou7811#"
        DBNAME = "memo.amoisoo.com"
        db = MYSQL.DB(HOST, USER, PASSWORD, DBNAME)
        # TABLENAME = "memo2"
        try:
            getRecord = db.CMD_import(TABLENAME)
        except:
            getRecord = []
        return getRecord


