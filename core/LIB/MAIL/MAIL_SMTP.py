#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import smtplib
#from email.MIMEText import MIMEText
#from email.Header import Header
#from email.Utils import formatdate

from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate
from datetime import datetime


class SMTP:
    def __init__(self, LOGIN = "conie6mm@gmail.com" , PASSWORD = "cgbook80"):

        self.SMTP       = "smtp.gmail.com"
        self.LOGIN      = LOGIN
        self.PASSWORD   = PASSWORD
        self.FROM       = "conie6mm@gmail.com"
        self.TEXTTYPE   = "html" #"plain"

    def header(self):
        html = """
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0"/>



  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css/froala_editor.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//froala_style.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//plugins/code_view.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//plugins/colors.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//plugins/emoticons.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//plugins/image_manager.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//plugins/image.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//plugins/line_breaker.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//plugins/table.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//plugins/char_counter.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//plugins/video.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//plugins/fullscreen.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//plugins/file.css">
  <link rel="stylesheet" href="http://support.amoisoo.com/LIB_FROALA3/css//plugins/quick_insert.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.3.0/codemirror.min.css">

<style>
    body {
      
    }


    table,td,th {
        border-collapse: collapse;
        border:1px solid #333;
        }
    
    
    div#editor {
      width: 95%;
      margin: auto;
      text-align: left;
}
</style>

</head>
        """

        return html

    def MAIL_SEND(self, setMailList , setTitle , setBody):
        #ENCODING = "iso-2022-jp"
        ENCODING = "UTF-8"

        SET_MAILLIST    = setMailList
        SET_TITLE   = setTitle
        SET_BODY    = self.header() + "\n<body>\n\n" + setBody + "\n\n</body>"

        message = MIMEText( SET_BODY.encode(ENCODING) , self.TEXTTYPE , ENCODING,)

        message["Subject"]  = str(Header(SET_TITLE , ENCODING))
        message["From"]     = "%s <%s>" %(str(Header(u"From",ENCODING)  ), self.FROM     )
        message["To"]       = "%s <%s>" %(str(Header(u"To",ENCODING)    ), SET_MAILLIST )
        message["Date"]     = formatdate()

        s = smtplib.SMTP(self.SMTP, 587)

        s.ehlo()

        s.starttls()

        try:
            s.login(self.LOGIN  , self.PASSWORD)
            #conie6mm.shop error

            s.sendmail( self.FROM , SET_MAILLIST , message.as_string(),)

            s.close()
            return SET_BODY
            #return ("Success send mail")

        except:
            return ("Error")

class SENDMAIL(SMTP):
    def __init__(self, user = "contact@amoisoo.com", password = "Leekyou7811#", getmail = "contact@amoisoo.com"):
        super(SENDMAIL, self).__init__()

        from datetime import datetime

        self.MAIL = SMTP(user, password)

        self.GETMAIL_ADDRESS = [ "lee@amoisoo.com", "support@amoisoo.com" , "contact@amoisoo.com" ]
        self.GETMAIL_ADDRESS = [ getmail ]

        self.supportType = "[support]"
        self.title = self.supportType + "[" + (datetime.now().strftime("%H:%M:%S")) + "]" + "title"

    def message(self , customType , setType , userAddress ,title, message ):
        result = "[" + (datetime.now().strftime("%Y-%m-%d")) + "]["
        result += (datetime.now().strftime("%H:%M:%S")) + "]" + "<br>"

        if(customType == 0): #server
            result += "USER MAIL : "+ userAddress +"<br>"
        result += ("[%s]" % (setType)) + "<br>"

        result += "<hr><h2>%s</h2><hr>" % (title)

        result += "<pre>"+ message + "</pre>"
        #noteList = message.split("\n")
        #for i in noteList:
        #    result += i + "<br>"

        result += "<hr>"
        if(customType == 1): #customer
            result += "<br><br> Customer"
        return result

    def send(self , setType, userAddress , title , message ):

        # server
        newTitle = ("[%s]" % (setType)) + title

        result = self.MAIL.MAIL_SEND( self.GETMAIL_ADDRESS , newTitle , self.message(0, setType , userAddress , title, message ) )
        # customer
        #self.MAIL.MAIL_SEND( userAddress , title , self.message(1 , setType , userAddress , title, message ) )

        self.resultView(setType, message)

        return result
    def resultView(self , setType , message):
        print("Content-type: text/html")
        print("")
        print("ok<br><br>")
        print( ("[%s]"%(setType)) , "<br><br>")
        print((datetime.now().strftime("%Y-%m-%d")), "<br>")
        print(datetime.now().strftime("%H:%M:%S"), "<br><hr>")
        print(message)



"""
SENDMAIL_USER   = "devkr@amoisoo.com"
SENDMAIL_PASS   = "Leekyou7811#"

GETMAIL_ADDRESS = "conie80@naver.com"
CUSTOMER_MAIL = GETMAIL_ADDRESS
MESSAGE_TITLE       = "aaa"
MESSAGE_NOTE     = "bbbb"
MESSAGE_TYPE = "QnA"

mail = SENDMAIL(SENDMAIL_USER , SENDMAIL_PASS , GETMAIL_ADDRESS)
mail.send( MESSAGE_TYPE , CUSTOMER_MAIL , MESSAGE_TITLE , MESSAGE_NOTE )

"""