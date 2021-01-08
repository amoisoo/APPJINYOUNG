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

    def CMD_XMLInteratora(self, setFile): # list parsing

        doc = QtXml.QDomDocument()
        doc.setContent(setFile)

        topElement = doc.documentElement()
        print(topElement)
        domNode = topElement.firstChild()
        print(domNode)
        result = []
        while not domNode.isNull():
            domElement = domNode.toElement()

            domElement = domNode.toElement()
            if (not domElement.isNull() ):
                #print("         ", domElement.tagName()) # record

                isExpend = domElement.attribute("Type")


            node = domElement.firstChild()
            item_Info = [isExpend]
            while not node.isNull():
                element = node.toElement()
                # print(element.tagName() , element.text())
                #if (element.tagName() == "posX"):
                #    getText = element.text()
                #    item_Info.append(getText)
                #elif (element.tagName() == "posY"):
                #    element.text()
                #    item_Info.append(getText)

                item_Info.append(element.text())

                node = node.nextSibling()
                #item_Info.append( info )
            #print(item_Info)

            domNode = domNode.nextSibling()
            result.append( item_Info )

        print("-"*50)
        domNode = topElement.childNodes()
        print(domNode)



        return result
