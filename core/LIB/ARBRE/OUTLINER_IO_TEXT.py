import sys, os
import binascii
from PyQt5.QtCore import *


from PyQt5 import QtXml


class IO_IMPORT:
    def __init__(self):
        pass


    def IO_DATA(self, file = "box.tablexml", isRaw = "0"):
        #return file
        #return  ['aaa', 'bbb', 'ccc', 'ddddd', 'eee']


        if(isRaw == "0"):
            fileName = file
            file = QFile(fileName)
            file.open(QIODevice.ReadOnly)
            file.close()
            return "OK"
        elif(isRaw == "1"):
            getInfoUnHexBinary = binascii.unhexlify(file)
            file = str(getInfoUnHexBinary, "utf-8")
            return "NG"

        LIST = self.CMD_XMLInterator(file)
        return LIST




    #--------------------------------
    def CMD_XMLInterator(self, setFile): # list parsing

        #fileName = "../qml/SUB_MODEL10.xml"

        #file = QFile(fileName)
        #file.open(QIODevice.ReadOnly)
        #print(file)
        #print(setFile)


        doc = QtXml.QDomDocument()
        doc.setContent(setFile)

        #--------------------------------------------------------
        # Item
        #--------------------------------------------------------
        topElement = doc.documentElement() #QDomElement
        domNode = topElement.firstChild() #QDomNode


        resultList = []

        result = []
        while not domNode.isNull():

            domElement = domNode.toElement()
            if (not domElement.isNull() ):
                #print("         ", domElement.tagName()) # record

                #indexNum = domElement.attribute("Index")

                node = domElement.firstChild()
                record = {}
                #print("-"*50)

                if( domElement.tagName() == "EDITOR_WIDGET" or domElement.tagName() == "SCENE_SETTINGS" ):
                    while not node.isNull():
                        element = node.toElement()
                        #print(element.tagName() , element.text())
                        record[element.tagName()] =  element.text()
                        node = node.nextSibling()

                elif( domElement.tagName() == "BOOK" or domElement.tagName() == "TableHeader"  ):
                    record = []
                    while not node.isNull():
                        element = node.toElement()
                        recordItem = {}
                        if (not element.isNull()):

                            node2 = element.firstChild()
                            while not node2.isNull():
                                element2 = node2.toElement()
                                #print(element2.tagName() , element2.text())
                                recordItem[element2.tagName()] = element2.text()
                                node2 = node2.nextSibling()
                            record.append( recordItem )
                        node = node.nextSibling()

                elif( domElement.tagName() == "Snapshot" ):
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
                            record.append( recordItem )
                        node = node.nextSibling()
                elif( domElement.tagName() == "ContextList" ):
                    record = []

                    while not node.isNull():
                        recordSub = []
                        element = node.toElement()
                        recordItems = []
                        recordItem = []
                        if (not element.isNull()):

                            node2 = element.firstChild()
                            recordSub.append(  element.tagName() )

                            while not node2.isNull():
                                element2 = node2.toElement()
                                recordItem.append( element2.text()  )
                                node2 = node2.nextSibling()
                            recordSub.append( recordItem )
                        node = node.nextSibling()
                        record.append( recordSub )
                else :
                    while not node.isNull():
                        element = node.toElement()

                        node = node.nextSibling()

                #print(record)

                result.append(record)

            domNode = domNode.nextSibling()







        return result



