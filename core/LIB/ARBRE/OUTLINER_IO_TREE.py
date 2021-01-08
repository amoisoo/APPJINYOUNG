import sys, os
import binascii
from PyQt5.QtCore import *


from PyQt5 import QtXml


class IO_IMPORT:
    def __init__(self):
        pass


    def IO_DATA(self, file = "html5TagList.tablexml", isRaw = "0"):

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



    def getChild(self, serachIndex , allList):
        result = []

        for i in allList:
            if (i[3] == serachIndex):
                result.append(i)

        return result


    def havePAGE(self , DATA_allList , uuid ):
        for i in DATA_allList:
            if (i[6] == uuid):
                return "1"
        return "0"
    def getBreadcrumbLoop(self , DATA_allList  , id_sort):
        result = []

        for i in DATA_allList:
            if( i[2] == id_sort ):
                result.append( i[3] )
                result.append( i[0][0] )
                return result

        return result


    def getBreadcrumb(self , DATA_allList  , uuid):

        # data[2] depth
        # ID_SORT i[2]
        # Parent i[3]
        html = ""
        getList = []
        getListString = []
        currentID = None
        parentID = None
        getRawDATA = []
        for i in DATA_allList:
            if( i[6] == uuid ):
                currentID = i[2]
                parentID = i[2]
                getList.append( i[2] )
                #getList.append( i[3] )
                getRawDATA.append( i[14] )

                #getListString.append( i[0][0] )

                break


        while True:

            getDATA = self.getBreadcrumbLoop(DATA_allList, parentID)
            parentID = getDATA[0]
            getListString.append( getDATA[1]  )
            if(parentID == "0"):
                break
            getList.append(str(parentID))

        result = []
        result.append( getList )
        result.append( getListString )
        result.append( getRawDATA )
        return result
        return """ <li class="nav-header"><i class="fa fa-th-large"></i> %s  </li> """ % str(getList)


    def getDATA(self , DATA_allList  , uuid ):
        for i in DATA_allList:
            if( i[6] == uuid ):
                return i

    def IO_DATA_reOrder(self, file = "html5TagList.tablexml", isRaw = "0"  ):
        allList = self.IO_DATA(file, isRaw)


        topItem = []
        childList = {}
        for i in allList:
            if(i[3] == "0"):topItem.append( i )

            child = self.getChild(i[2], allList)
            if(child != []):
                #print(i[0][0], i[1], i[6], "<br><br>")
                childList[("id_" + i[6] )] = child # child
                #for i in child:
                #   print(i[0] , "<br>")
                #print("-" * 50, "<br>")


        for i in topItem:
            #print(i[0][0],  "<br>")
            uuid = "id_" + i[6]
            #print( "id_" + i[6] , "<br><br><br>" )
            if (uuid in childList.keys()):

                get = childList[uuid]
                #for i in get:
                #    print(i[0][0], "<br>")

            #print("-" * 50, "<br>")

        result = []
        result.append(topItem)
        result.append(childList)
        result.append(allList)
        return result

        #getList = childList["id_92b6ec0b_7d28_4874_8f05_d2c25d747b56"]

    #--------------------------------
    def CMD_XMLInterator(self, setFile): # list parsing

        #fileName = "../qml/SUB_MODEL10.xml"

        #file = QFile(fileName)
        #file.open(QIODevice.ReadOnly)
        #print(file)

        doc = QtXml.QDomDocument()
        doc.setContent(setFile)

        topElement = doc.documentElement()
        domNode = topElement.firstChild()

        result = []


        while not domNode.isNull():

            domElement = domNode.toElement()
            if (not domElement.isNull() ):
                #print("         ", domElement.tagName()) # record

                isExpend = domElement.attribute("Expand")
                indexNum = domElement.attribute("Index")
                parentNum = domElement.attribute("ParentIndex")

                node = domElement.firstChild()
                record = {}
                index = 1
                while not node.isNull():
                    element = node.toElement()
                    #print(element.tagName() , element.text())
                    if(element.tagName() == "TITLE"   ):
                        getText     = element.text()
                        getColor    = element.attribute("color")
                        getBack     = element.attribute("background")
                        getInfo = []
                        getInfo.append(getText)
                        getInfo.append(getColor)
                        getInfo.append(getBack)
                        getInfo.append(isExpend)
                        getInfo.append(parentNum)

                        record['title'] = element.text()
                        record['title_option'] = getInfo
                    elif(element.tagName() == "SUBTITLE"):
                        getText     = element.text()
                        getColor    = element.attribute("color")
                        getBack     = element.attribute("background")
                        getInfo = []
                        getInfo.append(getText)
                        getInfo.append(getColor)
                        getInfo.append(getBack)
                        record['subtitle'] = element.text()
                        record['subtitle_option'] = getInfo

                    elif(element.tagName() == "ID"):record['id'] = element.text()
                    elif(element.tagName() == "ID_SORT"):record['id_sort'] = element.text()
                    elif(element.tagName() == "DEPTH"):record['depth'] = element.text()
                    elif(element.tagName() == "PROTECTION"):record['protection'] = element.text()
                    elif(element.tagName() == "PREFIX"):record['prefix'] = element.text()
                    elif(element.tagName() == "TABLENAME"):record['uuid'] = element.text() # UUID
                    elif(element.tagName() == "VISIBLE"):record['visible'] = element.text()
                    elif(element.tagName() == "VIEWLAYOUT"):record['layout'] = element.text()
                    elif(element.tagName() == "TAG"):record['tag'] = element.text()
                    elif(element.tagName() == "COMPONENTS"):record['component'] = element.text()
                    elif(element.tagName() == "CONTEXT"):record['context'] = element.text()
                    elif(element.tagName() == "CATEGORY"):record['gategory'] = element.text()
                    elif(element.tagName() == "DATA"):record['data'] = element.text()
                    elif(element.tagName() == "OPTIONS"):record['options'] = element.text()
                    elif(element.tagName() == "NOTE"):record['note'] = element.text()
                    elif(element.tagName() == "CODE"):record['code'] = element.text()
                    elif(element.tagName() == "CSS"):record['css'] = element.text()
                    elif(element.tagName() == "LINK"):record['link'] = element.text()
                    elif(element.tagName() == "SEPARATOR"):record['separator'] = element.text()
                    elif(element.tagName() == "ICON"):record['icon'] = element.text()
                    elif(element.tagName() == "IMAGE"):record['image'] = element.text()
                    elif(element.tagName() == "TODOS"):record['todos'] = element.text()
                    elif(element.tagName() == "PRIORITY"):record['priority'] = element.text()
                    elif(element.tagName() == "STATUS"):record['status'] = element.text()
                    elif(element.tagName() == "RATING"):record['rating'] = element.text()
                    elif(element.tagName() == "START"):record['start'] = element.text()
                    elif(element.tagName() == "END"):record['end'] = element.text()
                    elif(element.tagName() == "DUE"):record['due'] = element.text()
                    elif(element.tagName() == "ALERT"):record['alert'] = element.text()
                    elif(element.tagName() == "DATES"):record['dates'] = element.text()
                    elif(element.tagName() == "TIMES"):record['times'] = element.text()
                    elif(element.tagName() == "REPEAT"):record['repeat'] = element.text()
                    elif(element.tagName() == "CREATED"):record['created'] = element.text()
                    elif(element.tagName() == "MODIFED"):record['modified'] = element.text()
                    elif(element.tagName() == "USER"):record['user'] = element.text()
                    elif(element.tagName() == "LOCATION"):record['location'] = element.text()

                    else:
                        record[index] = element.text()

                    node = node.nextSibling()
                    index += 1
                #print(record)
                result.append(record)

            domNode = domNode.nextSibling()

        #print(result)
        #file.close()
        return result





























