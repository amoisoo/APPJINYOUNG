import os, sys, cgi
getPath = os.path.dirname(os.path.abspath(__file__))
getPath = os.path.dirname(getPath)
sys.path.append(getPath + "/LIB")

import OUTLINER_IO_TABLE
TABLE = OUTLINER_IO_TABLE.FILE_TABLE()
import html

class HTML:
    def __init__(self):
        self.imagePath = r"../outliner/imgOutliner"
        self.setDBName = ""

    def render(self , topItem, childItemList, fileName = ""):
        #self.setDBName = fileName
        html = ""


        for i in topItem:

            html += self.COMP_LIST(i, childItemList)


        return html

    def COMP_LIST(self , childItem, childItemList):
        result = ""

        if( childItem[10] == "Title"):
            result += self.COMP_title(childItem , childItemList)

        elif (childItem[10] == "Section"):
            result += self.COMP_section(childItem, childItemList)

        elif (childItem[10] == "SectionSub"):
            result += self.COMP_sectionSub(childItem, childItemList)

        elif (childItem[10] == "Parameter1"):
            result += self.COMP_parameter1(childItem)

        elif (childItem[10] == "Parameter2"):
            result += self.COMP_parameter2(childItem)

        elif (childItem[10] == "Code"):
            result += self.COMP_code(childItem)

        elif (childItem[10] == "Text"):
            result += self.COMP_text(childItem)
        elif (childItem[10] == "Detail"):
            result += self.COMP_detail(childItem, childItemList)

        elif (childItem[10] == "Note"):
            result += self.COMP_note(childItem, childItemList)
        elif (childItem[10] == "Memo"):
            result += self.COMP_memo(childItem, childItemList)
        elif (childItem[10] == "Card"):
            result += self.COMP_card(childItem, childItemList)
        elif (childItem[10] == "Info"):
            result += self.COMP_info(childItem, childItemList)
        elif (childItem[10] == "Youtube"):
            result += self.COMP_youtube(childItem)


        elif (childItem[10] == "TABLE"):
            result += self.COMP_table(childItem)

        elif (childItem[10] == "ImageView"):
            result += self.COMP_image(childItem)
        elif (childItem[10] == "ImageToggle"):
            result += self.COMP_imageToggle(childItem)
        elif (childItem[10] == "Grid"):
            result += self.COMP_LAYOUT_grid(childItem, childItemList)

        elif (childItem[10] == "Horizontal"):
            result += self.COMP_LAYOUT_horizontal(childItem, childItemList)

        elif (childItem[10] == "Tab"):
            result += self.COMP_LAYOUT_tab(childItem, childItemList)

        elif (childItem[10] == "Accordion"):
            result += self.COMP_LAYOUT_accordion(childItem, childItemList)

        elif (childItem[10] == "List"):
            result += self.COMP_LAYOUT_list(childItem, childItemList)


        else:
            result += self.COMP_header(childItem , childItemList)

        return result
    #------------------------------------------------
    #------------------------------------------------
    # COMP
    #------------------------------------------------
    #------------------------------------------------

    def COMP_header(self, item , childItemList):
        html = ""
        comp = """
        <div class="panel panel-inverse">
            <div class="panel-heading"  data-click="panel-collapse">
                <div class="panel-heading-btn" >  %s </div>
                <h4 class="panel-title">%s</h4>
            </div>
            
            <div class="panel-body  ">%s</div>
        </div>
        """

        #body = item[16]
        body = ""

        uuid =  ("id_" + item[6])

        if (uuid in childItemList.keys()):
            #getChild = childItem[  ]
            getChild = childItemList[ uuid ]
            for childItem in getChild:

                body += self.COMP_LIST(childItem, childItemList)



        else:
            body = ""

        title = item[0][0]
        if(title == ""):
            title = "&nbsp;"

        html += comp % ( item[13][0] , title , body )

        return html


    def COMP_section(self, item , childItemList):
        html = ""



        html += """
        <br>
         <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">

            <div class="heading-title heading-border">
                <h5>%s <span>%s</span></h5>
                <p class="font-lato fs-14">%s</p>
            </div>


            %s

        </div></div></div>

        """
        if (item[20] == "True"):
            html += "<hr />"

        if (item[16] != ""):
            getString = item[16].split("\n")
            setString = ""
            for i in getString:
                setString += i + "<br>"

            titleBase = """
                <div class="row">
                    <div class="col-md-2">

                    </div>
                    <div class="col-md-8">

                        <p> %s </p>
                    </div>
                </div>
            """

            netTitle = titleBase % setString
        else:
            netTitle = ""
        id = "" #item[1]
        subTitle = item[13][0]

        result = ""
        result += html % (id, str(item[0][0]), subTitle, netTitle)

        uuid =  ("id_" + item[6])

        if (uuid in childItemList.keys()):
            #getChild = childItem[  ]
            getChild = childItemList[ uuid ]
            for childItem in getChild:
                result += self.COMP_LIST(childItem, childItemList)

        return result
    def COMP_sectionSub(self, childItem , childItemList):


        uuid =  ("id_" + childItem[6])
        html = ""

        if (uuid in childItemList.keys()):
            getDATA = childItemList[uuid]


            for i in getDATA:

                html += self.COMP_LIST(i, childItemList)

        return html

    #------------------------------------------------
    #------------------------------------------------
    # COMP
    #------------------------------------------------
    #------------------------------------------------

    def COMP_note(self, childItem , childItemList):

        itemBase = """
            <div class="note %s ">
                    %s
              <div class="note-content">
              
                %s
                %s 
                
              </div>
            </div>
        """

        itemBase = """
        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
            <div class="row">
                <div class="col-md-2">
                </div>
                
                <div class="col-md-8">

                <div class="note %s ">
                        %s
                  <div class="note-content">
                  
                    %s
                    %s 
                    
                  </div>
                </div>

                </div>
            </div>
        </div></div></div>
        """


        cssColor = childItem[18]
        setColor = ""
        if(cssColor == "")              :setColor = "note-secondary"
        elif(cssColor == "primary")     :setColor = "note-primary"
        elif(cssColor == "secondary")   :setColor = "note-secondary"
        elif(cssColor == "success")     :setColor = "note-success"
        elif(cssColor == "danger")      :setColor = "note-danger"
        elif(cssColor == "warning")     :setColor = "note-warning"
        elif(cssColor == "yellow")      :setColor = "note-yellow"
        elif(cssColor == "info")        :setColor = "note-info"
        elif(cssColor == "lime")        :setColor = "note-lime"
        elif(cssColor == "purple")      :setColor = "note-purple"
        elif(cssColor == "light")       :setColor = "note-light"
        elif(cssColor == "dark")        :setColor = "note-dark"
        else                            :setColor = "note-danger"

        icon = ""#"""<div class="note-icon"><i class="fab fa-facebook-f"></i></div>"""
        if(childItem[0][0] == ""):title = ""
        else:title = """<h5><b>%s</b></h5>"""  % childItem[0][0]
        subTitle = """<p> %s</p>""" % childItem[13][0]
        note = """%s""" % childItem[16]



        html = itemBase % ( setColor , icon ,title ,note )

        return html

    def COMP_memo(self, childItem , childItemList):
        html = ""
        html = """

			<div class="row">
			    <div class="col-lg-12 col-md-12">
					
                    %s

			    </div>
			</div>
                """

        html = """
        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
            <div class="row">
                <div class="col-md-2">
                </div>

                <div class="col-md-8">

                    %s

                </div>
            </div>
        </div></div></div>
        """

        baseItem = """

					<div class="card %s text-center bg-white">
						<div class="card-block">
							<blockquote class="card-blockquote">
                                    %s
                                    %s
							</blockquote>
						</div>
					</div>


                    """

        cssColor = childItem[18]
        setColor = ""
        if(cssColor == "")              :setColor = "card-outline-warning"
        elif(cssColor == "primary")     :setColor = "card-outline-primary"
        elif(cssColor == "secondary")   :setColor = "card-outline-secondary"
        elif(cssColor == "success")     :setColor = "card-outline-success"
        elif(cssColor == "danger")      :setColor = "card-outline-danger"
        elif(cssColor == "warning")     :setColor = "card-outline-warning"
        elif(cssColor == "yellow")      :setColor = "card-outline-yellow"
        elif(cssColor == "info")        :setColor = "card-outline-info"
        elif(cssColor == "lime")        :setColor = "card-outline-lime"
        elif(cssColor == "purple")      :setColor = "card-outline-purple"
        elif(cssColor == "light")       :setColor = "card-outline-light"
        elif(cssColor == "dark")        :setColor = "card-outline-dark"
        else                            :setColor = "card-outline-warning"

        if(childItem[0][0] == ""):title = ""
        else : title = """<p class="f-s-14 f-w-600">%s </p>""" % childItem[0][0]
        subTitle = """<p> %s</p>""" % childItem[13][0]
        note = """<footer class="f-s-12">%s<cite title="Source Title">Source Title</cite></footer>""" % childItem[16]

        item = baseItem % (setColor, title, note)
        result = html % (item)
        return result


    def COMP_card(self, childItem , childItemList):
        result = ""
        html = """

			<div class="row">


			    <div class="col-lg-12 col-md-12">
					
                    %s
					
			    </div>

			</div>


                """

        baseItem = """
					<div class="card card-inverse %s text-center">
						<div class="card-block">
							<blockquote class="card-blockquote">
								%s
								%s
							</blockquote>   
						</div>
					</div>
                """

        cssColor = childItem[18]
        setColor = ""
        if(cssColor == "")              :setColor = "bg-gradient-blue"
        elif(cssColor == "primary")     :setColor = "bg-gradient-blue"
        elif(cssColor == "secondary")   :setColor = "bg-gradient-blue"
        elif(cssColor == "success")     :setColor = "bg-gradient-blue"
        elif(cssColor == "danger")      :setColor = "bg-gradient-red"
        elif(cssColor == "warning")     :setColor = "bg-gradient-orange"
        elif(cssColor == "yellow")      :setColor = "bg-gradient-blue"
        elif(cssColor == "info")        :setColor = "bg-gradient-blue"
        elif(cssColor == "lime")        :setColor = "bg-gradient-green"
        elif(cssColor == "purple")      :setColor = "bg-gradient-purple"
        elif(cssColor == "light")       :setColor = "bg-gradient-blue"
        elif(cssColor == "dark")        :setColor = "bg-gradient-black"
        else                            :setColor = "bg-gradient-blue"


        title = """<p class="f-s-14 f-w-600">%s </p>"""  % childItem[0][0]
        subTitle = """<p> %s</p>""" % childItem[13][0]
        note = """<footer class="f-s-12">%s<cite title="Source Title">Source Title</cite></footer>""" % childItem[16]

        item = baseItem % ( setColor , title  , note )
        result = html % (item)
        return result

    def COMP_info(self, childItem , childItemList):
        html = ""
        html += """
			<div class="row">
			    <div class="col-lg-12 col-md-12">
					

					

					
					<div class="card card-outline-danger text-center bg-white">
						<div class="card-block">
							<blockquote class="card-blockquote">
								<p class="f-s-14 text-inverse f-w-600">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
								<footer class="f-s-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
							</blockquote>
						</div>
					</div>

					<div class="card card-outline-purple bg-gradient-green text-center bg-white">
						<div class="card-block">
							<blockquote class="card-blockquote">
								<p class="f-s-14 text-inverse f-w-600">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
								<footer class="f-s-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
							</blockquote>
						</div>
					</div>
			    </div>
			</div>

                """

        baseItem = """
					<div class="card card-outline-warning text-center bg-white">
						<div class="card-block">
							<blockquote class="card-blockquote">
								<p class="f-s-14 text-inverse f-w-600">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
								<footer class="f-s-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
							</blockquote>
						</div>
					</div>
        """

        return html



    def COMP_title(self, childItem , childItemList):
        html = """
            <ul class="result-list">
                <li>
                    <a href="#" class="result-image" style="background-image: url(../assets/img/gallery/gallery-51.jpg)"></a>
                    <div class="result-info">
                        <h4 class="title"><a href="javascript:;">  %s </a></h4>
                        <p class="location">  %s </p>
                        <p class="desc">
                            %s 
                        </p>
                        <div class="btn-row">
            
            
                        </div>
                    </div>
            
                </li>
            
            </ul>
            <br>
        """
        title = childItem[0][0]
        subTitle = childItem[13][0]
        note = childItem[16]

        return html % ( title ,  childItem[35] ,  note )


    def COMP_detail(self , childItem , childItemList):



        html = """
            <dl class="row">
                %s
            </dl>
        """


        uuid =  ("id_" + childItem[6])

        itemList = ""


        if (uuid in childItemList.keys()):
            getDATA = childItemList[uuid]


            for i in getDATA:

                title       = i[0][0]
                subTitle    = i[13][0]
                note        = i[16]

                itemList += """ <dt class="text-inverse text-right col-4 text-truncate">%s</dt> <dd class="col-8 text-truncate">%s</dd> """ % ( title ,  note)


        return html % (itemList)



    def COMP_detailA(self , childItem , childItemList):



        html = """
            <dl class="dl-horizontal">
                %s
            </dl>
        """


        uuid =  ("id_" + childItem[6])

        itemList = ""


        if (uuid in childItemList.keys()):
            getDATA = childItemList[uuid]


            for i in getDATA:

                title       = i[0][0]
                subTitle    = i[13][0]
                note        = i[16]

                itemList += """ <dt class="text-inverse">%s</dt> <dd> %s </dd> """ % ( title ,  note)


        return html % (itemList)

    def COMP_text(self , childItem):
        html = ""
        itemBody = """
            <blockquote>
              <p >%s</p>
              <small>
                %s <cite title="Source Title">%s</cite>
              </small>
            </blockquote>
        """
        title = childItem[0][0]
        subTitle = ""
        if(childItem[13][0] != ""):
            subTitle =  """ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - %s -  """  %childItem[13][0]
        note = childItem[16]

        return itemBody % (note , title , subTitle)



    #------------------------------------------------
    #------------------------------------------------
    # Layout
    #------------------------------------------------
    #------------------------------------------------
    def COMP_LAYOUT_grid(self, childItem , childItemList):
        html = ""
        aaa = """
        			<div class="col-md-3 col-sm-4 m-b-2">
        				<a href="https://www.youtube.com/watch?v=5lWkZ-JaEOc" data-lity>
        					<img src="https://img.youtube.com/vi/5lWkZ-JaEOc/mqdefault.jpg" class="width-full" />
        				</a>
        			</div>
        """

        html += """

        <div class="row">
        	<!-- begin col-6 -->
        	<div class="col-md-12">
        		<div class="m-b-10 f-s-10 m-t-5"><b class="text-inverse">%s</b></div>

        		<div class="row row-space-2">


        			
                    %s
                </div>
        	</div>

        </div>


                        """

        baseItem = """
        			<div class="col-md-3 col-sm-4 m-b-2">
        			    <h4> %s </h4>

        			</div>
        """

        uuid =  ("id_" + childItem[6])
        getDATA = childItemList[uuid]

        setItem = ""

        for i in getDATA:
            setItem += baseItem % (i[0][0])

        setTitle = str(childItem[0][0]) #str(childItemList)
        result = html % (setTitle, setItem)
        if(childItem[20] == "True"):result += "<hr>" + childItem[20]

        return result

    def COMP_LAYOUT_horizontal(self, childItem , childItemList):
        html = ""
        html += """
        <div class="row">
            <div class="col-md-12">
                <div class="m-b-10 f-s-10 m-t-5"><b class="text-inverse">%s</b></div>


                <div class="card-group">
                    %s
                </div>
            </div>
        </div>
                """

        baseItem = """
            <div class="card">

                <div class="card-block">
                    %s
                    <h4 class="card-title">%s</h4>
                    <p class="card-text"><small class="text-muted">%s</small></p>
                    <p class="card-text"> %s</p>
                </div>

            </div>
        """


        uuid =  ("id_" + childItem[6])
        getDATA = childItemList[uuid]

        setItem = ""

        for i in getDATA:
            setImage = ""
            if(i[22] != ""):

                imageBase = """  <img class="card-img-top" src="%s" alt="Card image cap" /> """
                imagePath = self.imagePath + r"/" + self.setDBName + r"_image/" + i[22]
                setImage = imageBase % (imagePath)
            setSubTitle = str(i[13][0])

            setItem += baseItem % (setImage , i[0][0] ,setSubTitle ,  str(i[16]) )

        setTitle = str(childItem[0][0]) #str(childItemList)
        result = html % (setTitle, setItem)

        if(childItem[20] == "True"):result += "<hr>" + childItem[20]



        return result


    def COMP_LAYOUT_tab(self, childItem , childItemList):
        html = ""
        tabMAIN = """
<div class="row">
	<div class="col-lg-12">

		<ul class="nav nav-pills">
		
            %s

		</ul>

		<div class="tab-content">
		
            %s
			
		</div>
	</div>
</div>

        """

        tabNavi = ""
        tabBody = "<hr>"


        uuid =  ("id_" + childItem[6])
        getDATA = childItemList[uuid]

        itemBaseNavi = """
			<li class="nav-items">
				<a href="#%s" data-toggle="tab" class="nav-link %s ">
					<span class="d-sm-none">%s</span>
					<span class="d-sm-block d-none">%s</span>
				</a>
			</li>
        """

        itemBaseBody = """
            
			<div class="tab-pane fade %s show" id="%s">
				%s
				<p>
                    %s
				</p>
			</div>
        """



        for index , i in enumerate(getDATA):
            setActive = ""
            if(index == 0):setActive = " active "

            tabNavi += itemBaseNavi % ( (uuid + "_" + str(index)) ,  setActive , i[0][0], i[0][0]   )

            if (i[10] == "Parameter1"):
                note = i[16]
                title = """<h4 class="m-t-10">%s</h4>""" % i[0][0]
            else:
                note =  self.COMP_LIST(i, childItemList)
                title = ""

            tabBody += itemBaseBody % ( setActive , (uuid + "_" + str(index)) , title , note   )


        html = tabMAIN % (tabNavi ,   tabBody)


        if(childItem[20] == "True"):html += "<hr>" + childItem[20]

        return html



    def COMP_LAYOUT_accordion(self, childItem , childItemList):
        html = ""

        accBody = """

        <div class="row">
            <div class="col-lg-12">
                <div id="%s" class="card-accordion">

                    %s

                </div>
            </div>
        </div>
        """

        baseItem = """
			<div class="card">
				<div class="card-header bg-black text-white pointer-cursor %s" 	data-toggle="collapse" data-target="#%s">
					%s
				</div>
				<div id="%s" class="collapse %s " data-parent="#%s">
					<div class="card-body">
                        %s
					</div>
				</div>
			</div>
                """
        tabItemList = ""

        accordionMainID = "ACCORDIN_MAIN_" + childItem[6]

        uuid = ("id_" + childItem[6])
        getDATA = childItemList[uuid]

        if(childItem[15] == "-1"):
            getDATA.reverse()

        for index, i in enumerate(getDATA):
            if (index == 0):
                setActive = "  "
                setShow = " show "
            else:
                setActive = " collapsed "
                setShow = ""

            setUUID = uuid + "_" + str(index)
            title = i[0][0]
            note =  "<h3>" + title + "</h3><hr>"
            note +=  self.COMP_LIST(i, childItemList)

            tabItemList += baseItem  % ( setActive , setUUID , title , setUUID , setShow, accordionMainID , note)

        return accBody % (accordionMainID , tabItemList)



    def COMP_table(self, item, type = "0"):
        html = ""

        baseItem = """
        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
            <div class="row">
                <div class="col-md-2">

                </div>
                <div class="col-md-8">
                    <h5 class="mb-8">%s</h5>
                    <p> %s </p>
                </div>
            </div>
        </div></div></div>
        """

        DATA_table = TABLE.HTML_TABLE_BODY(item[31], "1", "-1", "0")

        #html += item[0][0] + "<br>"
        table = ""
        table += (DATA_table[0])
        if (DATA_table[1] != ""):
            table += ("<br>" + DATA_table[1])

        if(  type == "0" ):
            result = table
        elif( type == "1"):
            result = baseItem % ( "" , table  )

        return result

    def COMP_LAYOUT_list(self, childItem , childItemList, mode = "0"):
        html = ""

        ListMain = """
            <ul>
                %s
            </ul>
        """

        list = ""
        uuid =  ("id_" + childItem[6])

        if (uuid in childItemList.keys()):
            getDATA = childItemList[uuid]

            for i in getDATA:
                childUuid = ("id_" + i[6])
                #list += """<li>%s</li>""" % (childUuid)

                if (childUuid in childItemList.keys()):

                    list += """<li>%s %s </li>"""  % ( i[0][0]  , self.COMP_LAYOUT_list(i , childItemList, 1) )
                else:
                    list += """<li>%s</li>"""  % (i[0][0])

        if(mode == "0"):
            html += """<h4  class=".text-purple-darker" >%s</h4>""" % childItem[0][0]
        html += ListMain  % (list)

        return html


    #------------------------------------------------
    #------------------------------------------------
    #
    #------------------------------------------------
    #------------------------------------------------

    def COMP_parameter1(self, item):




        html = """
        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
            <div class="row">
                <div class="col-md-2">
                </div>
                
                <div class="col-md-8">
                    <h6 class="mb-8">%s</h6>
                    <p> %s </p>
                </div>
            </div>
        </div></div></div>
        """
        if (item[20] == "True"):
            html += "<hr />"

        getString = item[16].split("\n")
        setString = ""
        for i in getString:
            setString += i + "<br>"

        #

        from xml.sax.saxutils import escape
        #import html

        title = str(item[0][0] )
        setMemo = escape(setString)

        return html % (title, setString)
        return html % (title, setString)

    def COMP_parameter2(self, item):
        html = """

        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">

            <div class="row">

                <div class="col-md-2">
                </div>

                <div class="col-md-8">
                    <h5 class="mb-8">%s</h5>
                    <p> %s </p>
                </div>

                        %s
            </div>
        </div></div></div>

        """

        setImage = ""
        if (item[22] != ""):
            imageHtml = """
                <div class="col-md-2">
                    <img src="%s" class="img-fluid" alt="company logo">
                </div>
            """
            setImage = imageHtml % (self.imagePath + r"/" + "FILENAME" + r"_image/" + item[22])
            #setImage =             self.imagePath + r"/" + self.setDBName + r"_image/" + item[22]

        if (item[20] == "True"):
            html += "<hr />"
        title = str(item[0][0] )

        return html % (title , item[16], setImage)

    def COMP_code(self, item):
        html = """

        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
            <div class="row">
                <div class="col-md-2">
                </div>

                <div class="col-md-8">
                    %s
                    <div class="alert %s mb-30"><!-- WARNING -->
                        %s
                        %s
                    </div>
                </div>
            </div>
        </div></div></div>
        """
        if (item[20] == "True"):
            html += "<hr />"

        setTitle = ""
        if (item[0][0] != ""):
            setTitle = """ <h5 class="mb-8">%s</h5> """ % item[0][0]

        setSubTitle = ""
        if (item[13][0] != ""):
            setSubTitle = """ <strong>%s</strong> <br><br> """ % item[13][0]

        getString = item[17].split("\n")
        setString = ""
        for i in getString:
            # setString += i + "<br>"
            setString += i.replace(" ", "&nbsp;&nbsp;") + "<br>"

        setAlertType = ""
        if(item[18] == ""):                 setAlertType = "alert-secondary"
        elif( item[18] == "primary" ):      setAlertType = "alert-primary"
        elif( item[18] == "secondary" ):    setAlertType = "alert-secondary"
        elif( item[18] == "success" ):      setAlertType = "alert-success"
        elif( item[18] == "danger" ):       setAlertType = "alert-danger"
        elif( item[18] == "warning" ):      setAlertType = "alert-warning"
        elif( item[18] == "yellow" ):       setAlertType = "alert-yellow"
        elif( item[18] == "info" ):         setAlertType = "alert-info"
        elif( item[18] == "lime" ):         setAlertType = "alert-lime"
        elif( item[18] == "purple" ):       setAlertType = "alert-purple"
        elif( item[18] == "light" ):        setAlertType = "alert-light"
        elif( item[18] == "dark" ):         setAlertType = "alert-dark"
        else:                               setAlertType = "alert-secondary"

        #setCode = "<pre>%s</pre>" % setString
        setCode = setString.encode("utf-8").decode("unicode-escape")

        from html import escape


        #----------------------------------
        # code number
        #----------------------------------
        setCode = item[17]
        setCode = escape(setCode)
        getCodeList = setCode.split("\n")
        allCode = ""
        base = """<a name="l1" style = "background-color:white" ><span class="ln">%s    </span></a>&nbsp;&nbsp;&nbsp;&nbsp;%s """
        for index , i in enumerate(getCodeList):
            item_i = i.replace(" ", "&nbsp;&nbsp;&nbsp;&nbsp;")
            item_i = item_i.replace(" ", "&nbsp;")
            allCode +=   base %  ( str(index+1) , item_i  ) + "<br>"
        setCode = allCode
        #----------------------------------
        # code number
        #----------------------------------
        setCode = item[17]
        setCode = escape(setCode)
        setCode = setCode.replace("\n", "<br>")
        setCode = setCode.replace(" ", "&nbsp;&nbsp;&nbsp;&nbsp;")
        setCode = setCode.replace(" ", "&nbsp;")

        #setCode = "<pre>%s</pre>" % setCode


        return html % (setTitle, setAlertType , setSubTitle, setCode)

        #setCode = "<pre>%s</pre>" % item[17]
        #return html % (setTitle, setSubTitle, setCode)


    def COMP_image(self, item):
        html = """
        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
            <div class="row">


                <div align="center" class="col-md-12">
                        <img src="%s" alt="image01"/>
                </div>

            </div>
        </div></div></div><br>
        """

        setImage  = self.imagePath + r"/" + self.setDBName + r"_image/"  + item[22]

        return html % (setImage)


    def COMP_imageToggle(self, item):
        html = """
        <div class="container"><div class="row"> <div class="col-md-12 col-sm-12">
            <div class="row">
                <div class="col-md-2">

                </div>

                <div class="col-md-8">
                        <img src="%s" alt="image01"/>
                </div>
            </div>
        </div></div></div><br>
        """

        setImage  = self.imagePath + r"/" + self.setDBName + r"_image/"  + item[19]

        return html % (setImage)



    def COMP_youtube(self, item):

        html = """
        <div class="row">
            <div class="col-md-12">
                <div class="container" align="center"><div class="row"> <div class="col-md-12 col-sm-12">
                    <iframe width="560" height="315" src="%s" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                </div> </div></div>
            </div>
        </div>
        

        
        """
        if (item[20] == "True"):
            html += "<hr />"

        return html % ( item[16])
