import os, sys, cgi
getPath = os.path.dirname(os.path.abspath(__file__))
getPath = os.path.dirname(getPath)
sys.path.append(getPath + "/LIB")

from xml.sax.saxutils import escape

class HTML:
    def __init__(self):

        self.TITLE_LEN = 17
        #self.imagePath = r"../outliner/imgOutliner"



    def render(self , DATA_MAIN , DATA_CHILD , getSelList , dbName , sethomeAddress):
        html = ""

        topMenu = """
					<li class="has-sub %s  ">
					    <a href="javascript:;">
					        <b class="caret"></b>
					        %s
					        <i class="fa fa-th-large"></i>
					        <span>%s %s</span>
					    </a>
						<ul class="sub-menu">
							        %s
						</ul>
						

					</li>
        """

        for i in DATA_MAIN:

            uuid = ("id_" + i[6])
            chilItem = self.getChild( i[6] , DATA_CHILD  , getSelList , dbName , sethomeAddress)

            setSel = "  "
            if( i[2] in  getSelList):
                setSel = " active "

            setTitle = ""
            setTitleLen = self.TITLE_LEN
            if( len(i[0][0]) < setTitleLen):setTitle = i[0][0]
            else:setTitle = i[0][0][:setTitleLen] + "..."
            setTitle = setTitle.replace(" ", "&nbsp;")

            if (i[12] == ""):setTag = ""
            else:setTag = """ <span class="label label-theme m-l-5">%s</span> """ % (i[12])

            if(i[10] == "File"): # File
                itemBase = """<li class="%s"><a href="%s?book=%s&page=page_%s"><i class="fa fa-th-large"></i> <span>%s %s</span></a></li>"""
                html += itemBase % (setSel  , sethomeAddress , dbName , i[6] , setTitle , setTag   )

            else: # Menu
                if (uuid in DATA_CHILD.keys()): # have child
                    getChild = DATA_CHILD[uuid]

                    childCount = """ <span class="badge pull-right">%s</span> """ % str(len(getChild))
                    html += topMenu  % ( setSel , childCount, setTitle , setTag, chilItem )
                else:
                    childCount = ""

                    html += topMenu  % ( setSel , childCount, setTitle , setTag, chilItem )

        return html




    def getChild(self, id , DATA_CHILD , getSelList , dbName , sethomeAddress):
        #menuItem = """ <li><a href="./?page=page_%s">%s</a></li> """

        html = ""

        uuid = ("id_" + id )


        if (uuid in DATA_CHILD.keys()):
            getChild = DATA_CHILD[uuid]


            chilItem = ""
            for j in getChild:
                #chilItem += menuItem % (j[0][0])
                chilItem += self.loopChild(j, DATA_CHILD , getSelList , dbName , sethomeAddress)

                #chilItem += self.getChild( j[6] , DATA_CHILD )

        else:
            return ""
            return """ <li><a href="email_system.html">NOCHILD</a></li> """

        return chilItem


    def loopChild(self, item , DATA_CHILD , getSelList , dbName , sethomeAddress):
        html = ""

        menu = """
            <li class="has-sub  %s ">
                <a href="javascript:;">
                    

                    <b class="caret pull-right"></b> 
                    %s 
                    %s  %s
                </a>
                <ul class="sub-menu">
                    %s  
                </ul>
            </li>
        """



        if (item[12] == ""):setTag = ""
        else:setTag = """ <span class="label label-theme m-l-5">%s</span> """ % (item[12])

        uuid = ("id_" + item[6] )

        if (uuid in DATA_CHILD.keys()):
            setSel = "  "
            if (item[2] in getSelList):
                setSel = " active "

            getChild = DATA_CHILD[uuid]
            getItemList = ""
            for i in getChild:
                getItemList += self.loopChild( i , DATA_CHILD , getSelList , dbName , sethomeAddress )

            childCount = """ <span class="badge pull-right">%s</span> """ % str(len(getChild))

            html += menu % (setSel ,childCount ,  item[0][0] ,  setTag , getItemList)


        else:
            setSel = "  "
            if (item[2] in getSelList):
                setSel = """ class="active" """

            setTitleLen = self.TITLE_LEN

            if( len(item[0][0]) < setTitleLen):setTitle = item[0][0]
            else:setTitle = item[0][0][:setTitleLen] + "..."
            setTitle = setTitle.replace(" ", "&nbsp;")


            html += """ <li %s  ><a href="%s?book=%s&page=page_%s">%s %s </a></li> """ % ( setSel  , sethomeAddress , dbName , item[6] ,   setTitle , setTag  )

        return html









