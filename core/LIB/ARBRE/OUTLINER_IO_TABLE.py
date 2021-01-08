
import sys, os
import binascii
from PyQt5.QtCore import *


from PyQt5 import QtXml




class FILE_TABLE:
    def __init__(self):
        pass

    def IO_DATA(self, file = "box.tablexml", isRaw = "0"):

        if(isRaw == "0"):
            fileName = file
            file = QFile(fileName)
            file.open(QIODevice.ReadOnly)
            file.close()
        elif(isRaw == "1"):
            getInfoUnHexBinary = binascii.unhexlify(file)
            file = str(getInfoUnHexBinary, "utf-8")

        LIST = self.CMD_XMLInterator(file)
        return LIST




    def IO_TABLE(self, file = "html5TagList.tablexml" , isRaw = "0" ):
        LIST = self.IO_DATA(file)


        TableInfo = LIST[0]
        SceneSettings = LIST[1]
        Sanpshot = LIST[2]
        TableItem = LIST[3]
        TableHeaderItem = LIST[4]
        try:ContextList = LIST[5]
        except:ContextList = None
        try:SelectionList = LIST[6]
        except:SelectionList = []
        #---------------------------------

        ROW = int(TableInfo["row"])
        COL = int(TableInfo["col"])



    def ITEM_GRID(self, file = "html5TagList.tablexml" , isRaw = "0" , gridType = "-1"):
        LIST = self.IO_DATA(file, isRaw)

        TableInfo = LIST[0]
        SceneSettings = LIST[1]

        TableItem = LIST[3]
        TableHeaderItem = LIST[4]

        ROW = int(TableInfo["row"])

        if(gridType == "-1"):
            COL = int(TableInfo["col"])
        elif (gridType == "0"):
            COL = int(SceneSettings["QML_GRID_count"])
        else :
            COL = int(gridType)
        trList = []
        baseItem = []
        for index, i in enumerate(TableItem):
            next = index % COL
            if (index != 0 and next == 0):
                trList.append(baseItem)
                baseItem = []


            baseItem.append(i)
        trList.append(baseItem)

        result = []
        result.append(TableHeaderItem)
        result.append(trList)
        result.append(TableInfo)
        result.append(SceneSettings)
        return result

    def TYPE_OUTLINER(self, DATA):
        TABLE_HEADER             = DATA[0]
        TABLE_DATA              = DATA[1]
        TABLE_TABLE_INFO        = DATA[2]
        TABLE_SCENE_SETTINGS    = DATA[3]
        html = ""

        baseBody = """

        <div class="row">
        	<div class="col-md-12">
        		<div class="m-b-10 f-s-10 m-t-5"><b class="text-inverse">%s</b></div>

        		<div class="row row-space-2">



                    %s
                </div>
        	</div>

        </div>


        """
        baseItem = """
        			<div class="col-md-2 col-sm-2 m-b-2">
        			    <h5> %s </h5>

        			</div>
        """


        html += TABLE_SCENE_SETTINGS["SCENE_DOC_TYPE"]  + "&nbsp;&nbsp;&nbsp;&nbsp;"
        html += TABLE_SCENE_SETTINGS["OUTPUT_TYPE"]  + "<br>"
        html += "Col : "+ TABLE_TABLE_INFO["col"]  + "<br><br><br>"
        html += "Grid : "+ TABLE_SCENE_SETTINGS["QML_GRID_count"]  + "<br><hr>"

        col = int(TABLE_SCENE_SETTINGS["QML_GRID_count"])
        setItem = ""


        for index, i in enumerate(TABLE_DATA):
            num = index % col
            setItem += baseItem % (i[0]["TEXT"])
            #html += str(i[0]["TEXT"]) + "&nbsp;&nbsp;&nbsp;&nbsp;"

            #if(num == (col -1) ): html += "<br>"
        result = baseBody % ( "", setItem)

        return result

    def HTML_TABLE_BODY(self, file = "html5TagList.tablexml" , isRaw = "0" , gridType = "-1" , hasTitle = "0"):
        result = []

        TABLE = self.ITEM_GRID( file , isRaw  , gridType)
        html = ""
        #html += str(TABLE[0]) + "<br><br><br>"
        #html += str(TABLE[1]) + "<br><br><br>"
        #html += str(TABLE[2]) + "<br><br><br>"
        #html += str(TABLE[3]) + "<br><br><br>"
        #html += """ <table  width = "100%"  border = 1 cellspacing = 0 cellpadding = 2 > """

        TABLE_DATA        = TABLE[1]
        TABLE_TABLE_INFO        = TABLE[2]
        TABLE_SCENE_SETTINGS    = TABLE[3]



        #html += ""+ str(TABLE_SCENE_SETTINGS)  + "<br><br><br>"

        if(TABLE_SCENE_SETTINGS["SCENE_DOC_TYPE"]  == "OUTLINER"):


            html += self.TYPE_OUTLINER( TABLE )

            result.append( html )
            result.append( "" )

            return result

        #---------------------------------------------
        if(hasTitle == "1"):
            html += "<h2>%s</h2>" % (TABLE[3]["SCENE_TITLE"])
            html += """<h5 style = "text-align: right; " >%s</h5>""" % (TABLE[3]["SCENE_CREATE_DATE"])


        html += """\n<table class=" table-hover"  style = "background : #ffffff ;" width = "100%"   border = 1 cellspacing = 0 cellpadding = 2 > """
        # table table-bordered
        #--------------------------------------

        if(TABLE[2]["isHidden"] == "False"):
            html += "\n    <thead>\n        <tr>"
            for i in TABLE[0]:
                tableHeader = """<th>%s</th>"""
                html += tableHeader %   (i["TEXT"])
            html += "</tr>\n    </thead>"

        #--------------------------------------
        html += "\n    <tbody>\n"
        firstIndexCount = 0
        nextIndexCount = 0

        rowCount = len(TABLE[1]) - 1
        for index, i in enumerate(TABLE[1]):
            tr_base = """ <tr  >% </tr> """
            baseItem = ""
            if(index == 0):
                firstIndexCount = len(i)
                nextIndexCount = len(i)
            else: nextIndexCount = len(i)
            for index_j , j in enumerate(i) :

                TEXT = j["TEXT"]


                if("#000000" != j["COLOR_text"]):COLOR_TEXT = (j["COLOR_text"])
                else:COLOR_TEXT = ""

                if("#000000" != j["COLOR_back"]):COLOR_BG = """bgcolor="%s" """ % (j["COLOR_back"])
                else:COLOR_BG = ""

                AlIGN = ""
                if(j["TEXT_Aligin"] == "0")    :AlIGN = """ style = "text-align: left;  color : %s " """ % (COLOR_TEXT)
                elif(j["TEXT_Aligin"] == "132")  :AlIGN = """ style = "text-align: center; color : %s " """ % (COLOR_TEXT)
                elif(j["TEXT_Aligin"] == "130")  :AlIGN = """ style = "text-align: right; color : %s " """ % (COLOR_TEXT)

                baseItem += """    <td  height="12px" %s %s >%s</td> """ % (COLOR_BG , AlIGN , TEXT)

            tempCount = ""
            if ((firstIndexCount - nextIndexCount) != 0):
                tempCount = "<td></td>" * (firstIndexCount - nextIndexCount)

            # one item : only 1 row : end no title : ignore
            if ( rowCount == index and TEXT == "" and len(i) == 1):
                pass
            else:
                html +=  "        <tr>"+ baseItem + tempCount + "</tr>" + "\n"



        html += "    </tbody>\n"
        #--------------------------------------

        html += "</table>\n"


        #--------------------------------------
        #--------------------------------------
        #--------------------------------------
        note = ""
        getNote = TABLE[3]["SCENE_NOTE"].split("\n")
        for i in getNote:
            note += i.replace(" ", "&nbsp;")
            note += "<br>"

        #--------------------------------------
        #--------------------------------------
        #--------------------------------------

        result.append( html )
        result.append( note )

        return result




    def CMD_XMLInterator(self, setFile):  # list parsing

        # fileName = "../qml/SUB_MODEL10.xml"

        # file = QFile(fileName)
        # file.open(QIODevice.ReadOnly)
        # print(file)
        # print(setFile)
        doc = QtXml.QDomDocument()
        doc.setContent(setFile)

        # --------------------------------------------------------
        # Item
        # --------------------------------------------------------
        topElement = doc.documentElement()  # QDomElement
        domNode = topElement.firstChild()  # QDomNode

        resultList = []

        result = []
        while not domNode.isNull():

            domElement = domNode.toElement()
            if (not domElement.isNull()):
                # print("         ", domElement.tagName()) # record

                # indexNum = domElement.attribute("Index")

                node = domElement.firstChild()
                record = {}
                # print("-"*50)

                if (domElement.tagName() == "TableInfo" or domElement.tagName() == "Settings"):
                    while not node.isNull():
                        element = node.toElement()
                        # print(element.tagName() , element.text())
                        record[element.tagName()] = element.text()
                        node = node.nextSibling()

                elif (
                        domElement.tagName() == "Table" or domElement.tagName() == "TableHeader" or domElement.tagName() == "Selection"):
                    record = []
                    while not node.isNull():
                        element = node.toElement()
                        recordItem = {}
                        if (not element.isNull()):

                            node2 = element.firstChild()
                            while not node2.isNull():
                                element2 = node2.toElement()
                                # print(element2.tagName() , element2.text())
                                recordItem[element2.tagName()] = element2.text()
                                node2 = node2.nextSibling()
                            record.append(recordItem)
                        node = node.nextSibling()

                elif (domElement.tagName() == "Snapshot"):
                    record = []
                    while not node.isNull():
                        element = node.toElement()
                        recordItem = {}
                        if (not element.isNull()):

                            node2 = element.firstChild()
                            while not node2.isNull():
                                element2 = node2.toElement()
                                recordItem[element2.tagName()] = element2.text()
                                node2 = node2.nextSibling()
                            record.append(recordItem)
                        node = node.nextSibling()
                elif (domElement.tagName() == "ContextList"):
                    record = []

                    while not node.isNull():
                        recordSub = []
                        element = node.toElement()
                        recordItems = []
                        recordItem = []
                        if (not element.isNull()):

                            node2 = element.firstChild()
                            recordSub.append(element.tagName())

                            while not node2.isNull():
                                element2 = node2.toElement()
                                recordItem.append(element2.text())
                                node2 = node2.nextSibling()
                            recordSub.append(recordItem)
                        node = node.nextSibling()
                        record.append(recordSub)

                else:
                    while not node.isNull():
                        element = node.toElement()

                        node = node.nextSibling()

                # print(record)

                result.append(record)

            domNode = domNode.nextSibling()

        return result

#IO = FILE_TABLE()
#getLIST = IO.IO_DATA()
#print(getLIST)
