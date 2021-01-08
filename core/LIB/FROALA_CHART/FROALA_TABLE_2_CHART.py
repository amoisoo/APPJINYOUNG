
from bs4 import BeautifulSoup

JSON_SINGLE = """
{
        "chart": {
            "caption": "%s",
            "subCaption": "%s",
            "use3DLighting": "0",
            "showPercentValues": "1",
            "decimals": "1",
            "useDataPlotColorForLabels": "1",
            "exportEnabled": "1",
            "theme": "froala"
        },
        "data": [
                %s
        ]
}
"""

JSON_SINGLE_radar = """
{
        chart: {
    caption: "%s",
    subcaption: "%s",
    theme: "froala",
    showlegend: "0",
    showdivlinevalues: "0",
    showlimits: "0",
    showvalues: "1",
    plotfillalpha: "40",
            "exportEnabled": "1",

    plottooltext: "Harry's $label skill is rated as $value"
  },
  categories: [
    {
      category: [
                %s
      ]
    }
  ],
  dataset: [
    {
      seriesname: "User Ratings",
      color: "#ff0000",

      data: [
          %s
      ]
    }
  ]
}

"""

JSON_MATRIX_line = """
{
    "chart": {
    "caption": "%s",
    "subcaption": "%s",

    "yaxisname": "성장률  %s",
    "drawcrossline": "1",
    
    "numbersuffix": "%s",
    "plottooltext": "$seriesName 의  $label:  $dataValue ",
    "exportEnabled": "1",
    "theme": "froala"
  },

  "categories": [


    {

      "category": [
%s
      ]

    }
  ],


  "dataset": [

%s


  ]
}

"""

JSON_bar = """
{
            "chart": {
        "theme": "froala",
        "caption": "%s",
		"subCaption":"%s",
        "xAxisname": "분기",
        "yAxisName": "수익 (단위 : 달러)%s",
        "numberPrefix": "%s",
        "plotFillAlpha": "80",
        "divLineIsDashed": "1",
        "divLineDashLen": "1",
		"exportEnabled": "1",
        "divLineGapLen": "1"
      },
      "categories": [{
        "category": 
[
          %s
        ]

      }],

      "dataset": [

%s
      
      ],


      "trendlines": [
      {
      
      
        "line": [

        
        ]
        
        
      }
      ]
      
      
    }

"""


JSON_link = """
{
        chart: {
    caption: "%s",
    subcaption:
      "%s",
    theme: "froala",
    orientation: "horizontal",
    linkalpha: 30,
    linkhoveralpha: 60,
            "exportEnabled": "1",

    nodelabelposition: "start"
  },
  nodes: [

%s
  ],

  links: [


%s



  ]
}

"""



JSON_bubble = """
{ chart: {
    caption: "%s",
    subcaption: "%s",
    xaxisname: "변화",
    yaxisname: "가격",
    //numberprefix: "$",
    theme: "froala",
    "exportEnabled": "1",
    plottooltext: "$name : 환경 변화: $zvalue "
  },
  categories: [
    {
      verticallinealpha: "10",
      category: [
      
      
       // { label: "0", x: "0",  showverticalline: "1" },
       // { label: "100", x: "1500", showverticalline: "1" },

        
        %s
        
      ]
    }
  ],
  dataset: [
    {
      data: [
       // { x: "1", y: "1",  z: "1",  color: "#ff0000",  name: "Campaign 1" , },
       // { x: "10", y: "1",  z: "1",  color: "#ff0000",  name: "Campaign 1" , },
       // { x: "20", y: "1",  z: "1",  color: "#ff0000",  name: "Campaign 1" , },
       // { x: "30", y: "1",  z: "1",  color: "#ff0000",  name: "Campaign 1" , },
        


        %s
        
      ]
    } , 
    
    
    
    
  ]
}

"""

JSON_scatter = """

{
            chart: {
    caption: "%s",
    subcaption: "%s",
    xaxisname: "평균 온도",
    yaxisname: "판매액",
    
    xaxisminvalue: "20",
    xaxismaxvalue: "100",
    ynumberprefix: "$",
    
    yaxisminvalue: "1200",
    xnumbersuffix: "°F",
    theme: "froala",
    showlegend: "0",
		"exportEnabled": "1",

    plottooltext:
      "$yDataValue worth $seriesNames were sold, when temperature was $xDataValue"
  },
  categories: [
    {
      verticallinedashed: "1",
      verticallinedashlen: "1",
      verticallinedashgap: "1",
      verticallinethickness: "1",
      verticallinecolor: "#000000",
      category: [
        { x: "20", label: "20°F",  showverticalline: "0"  },
        {  x: "40", label: "40°F" },
        {  x: "60", label: "60°F"  },
        {  x: "80",  label: "80°F" },
        {  x: "100", label: "100°F"  }
        
        %s
      ]
    }
  ],
  dataset: [
  
    {
      seriesname: "아이스크림",
      anchorbgcolor: "5D62B5",
      data: [
      
      
                %s

      ]
    } , 
    
   // {
   //   seriesname: "아이스크림",
   //   anchorbgcolor: "5D62B5",
   //   data: [
      
      
    //    {x: "221",y: "1450"},
    //    { x: "222", y: "1490" },
    //    {  x: "223", y: "1560" },


    //  ]
  //  } , 
    
    

    
    
  ]
}
"""


JSON_heatmap = """

{
        chart: {
    theme: "froala",
    caption: "%s",
    subcaption: "%s %s",
    xaxisname: "헤더",
    yaxisname: "종류",
    showvalues: "1",
    valuefontcolor: "#ffffff",
    "exportEnabled": "1",
"orientation": "horizontal",

    plottooltext: "$columnlabel 의 $rowlabel : $value/5"
  },
  colorrange: {
    mapbypercent: "0",

    gradient: "1",
    minvalue: "-50",
	code: "#00ffff",
    startlabel: "최소",
    endlabel: "최대"
  },

  dataset: [
    {
      data: [
%s
      ]
    }
  ],
  columns: {

    column: [
%s
    ]

  },
  rows: {
    row: [
%s
    ]
  }
}

"""

class IO:

    def __init__(self, url = "" ):
        self.DATA       = BeautifulSoup(url, 'html.parser')
        self.getHEADER  = self.DATA.table.thead.tr
        self.getTABLEBODY    = self.DATA.table.tbody.children


    def getTableHEADER(self):
        HEADER = self.getHEADER
        result = []
        for index, i in enumerate(HEADER):
            if (i.name != "th"): continue
            result.append( i.string )

        return result

    def getTableBODY(self):
        BODY = self.getTABLEBODY
        result = []
        for index, i in enumerate( BODY ):
            if ( i.name != "tr" ) : continue
            try:
                column = []
                for j in i.children :
                    if(j.name == "td"):
                        #print(j.name, j.string)
                        column.append( j.string )
                result.append( column )
            except:pass

        return result

    def get_RAW(self):
        result = []
        try:
            result.append( self.getTableHEADER() )
        except:
            result.append( [] )

        result.append( self.getTableBODY()  )
        return result


    def get_DATA(self , data ):
        result = None
        print("DATA, table", data)

        if( data.context == "pie" ):result = self.CHART_SINGLE(data)
        elif( data.context == "doughnut" ):result = self.CHART_SINGLE(data)
        elif( data.context == "pyramid" ):result = self.CHART_SINGLE(data)
        elif( data.context == "funnel" ):result = self.CHART_SINGLE(data)
        elif( data.context == "radar" ):result = self.CHART_SINGLE_radar(data)

        elif( data.context == "line" ):result = self.CHART_SINGLE_line(data)
        elif( data.context == "area" ):result = self.CHART_SINGLE_line(data)

        elif( data.context == "angulargauge" ):result = self.CHART_SINGLE(data)

        elif( data.context == "bar" ):  result = self.CHART_BAR(data)
        elif( data.context == "column" ): result = self.CHART_BAR(data)

        elif( data.context == "stackedarea" ):result = self.CHART_BAR(data)
        elif( data.context == "stackedbar" ):result = self.CHART_BAR(data)
        elif( data.context == "stackedcolumn" ):result = self.CHART_BAR(data)


        elif( data.context == "chord" ):result = self.CHART_LINK(data)
        elif( data.context == "sankey" ):result = self.CHART_LINK(data)

        elif( data.context == "bubble" ):result = self.CHART_BUBBLE(data)
        elif( data.context == "scatter" ):result = self.CHART_SCATTER(data)

        elif( data.context == "heatmap" ):result = self.CHART_HEATMAP(data)


        elif( data.context == "combination" ):result = self.CHART_SINGLE(data)

        elif( data.context == "timeseries" ):result = self.CHART_SINGLE(data)
        else: result = self.CHART_SINGLE(data)

        return result

    def CHART_HEATMAP(self, DATA):


        getDATA  = self.get_RAW()
        #--------------------------------------------------------------
        baseLabel_X = """  { id: "rows_%s", label: "%s"},  """
        baseLabel_Y = """  { id: "cols_%s", label: "%s"},  """
        dataListLabel_X = ""
        dataListLabel_Y = ""

        for index, i in enumerate(getDATA[1]):
            dataListLabel_Y += baseLabel_Y % (  str(index +1 ) ,  i[0]  )

        for index, i in enumerate(getDATA[0]):
            if( index == 0) : continue
            dataListLabel_X += baseLabel_X % (  str(index  ) ,  i[0]  )


        #--------------------------------------------------------------

        baseValueSet = """  {  rowid: "cols_%s", columnid: "rows_%s",  value: "%s"  },  \n"""

        setDATAset = ""

        for index_x, i in enumerate(getDATA[1]):

            for index_y , j in enumerate( i  ):
                if(index_y == 0): continue
                setDATAset += baseValueSet %  (  index_x + 1, index_y , j  )
                #print( index_x + 1, index_y , j   )

        unit = "%"

        #return JSON_bar % (DATA.title, DATA.subtitle, unit,unit, dataListLabel, setDATAset)
        print(DATA.title, DATA.subtitle , ""  , setDATAset , dataListLabel_X , dataListLabel_Y )

        return JSON_heatmap % (DATA.title, DATA.subtitle , ""  , setDATAset , dataListLabel_X , dataListLabel_Y )



    def CHART_SCATTER(self, DATA):
        getDATA  = self.get_RAW()
        baseLabel = """  {label: "%s"},  """
        dataListLabel = ""

        for index, i in enumerate(getDATA[1]):
            dataListLabel += baseLabel % ( i[0]  )


        baseValueSet = """   {x: "%s",y: "%s"},  \n"""


        baseValue = """  {value: "%s"},   """

        setDATAset = ""
        for index, i in enumerate(getDATA[1]):

            setDATAset +=  baseValueSet % ( i[1] , i[2] )

        unit = "%"

        print(setDATAset)
        #return JSON_bar % (DATA.title, DATA.subtitle, unit,unit, dataListLabel, setDATAset)
        return JSON_scatter % (DATA.title, DATA.subtitle , "" , setDATAset)


    def CHART_BUBBLE(self, DATA):

        getDATA  = self.get_RAW()
        baseLabel = """  {label: "%s"},  """
        dataListLabel = ""

        for index, i in enumerate(getDATA[1]):
            dataListLabel += baseLabel % ( i[0]  )


        baseValueSet = """ { name: "%s", x: "%s", y: "%s",   z: "%s",   }, \n"""


        baseValue = """  {value: "%s"},   """

        setDATAset = ""
        for index, i in enumerate(getDATA[1]):

            setDATAset +=  baseValueSet % ( i[0]  ,  i[1] , i[2], i[3] )

        unit = "%"

        print(setDATAset)
        #return JSON_bar % (DATA.title, DATA.subtitle, unit,unit, dataListLabel, setDATAset)
        return JSON_bubble % (DATA.title, DATA.subtitle , "" , setDATAset)



    def CHART_LINK(self, DATA):

        getDATA  = self.get_RAW()
        baseLabel = """  {label: "%s"},  """
        dataListLabel = ""

        for index, i in enumerate(getDATA[1]):
            dataListLabel += baseLabel % ( i[0]  )


        baseValueSet = """{ from: "%s", to: "%s", value: %s}, \n"""

        baseValue = """  {value: "%s"},   """

        setDATAset = ""
        for index, i in enumerate(getDATA[1]):

            setDATAset +=  baseValueSet % ( i[0]  ,  i[1] , i[2])

        unit = "%"

        print(setDATAset)
        #return JSON_bar % (DATA.title, DATA.subtitle, unit,unit, dataListLabel, setDATAset)
        return JSON_link % (DATA.title, DATA.subtitle , dataListLabel , setDATAset)



    def CHART_BAR(self, DATA):


        if(DATA.layout == "INVERSE"):

            getDATA = self.get_RAW()
            baseLabel = """  {label: "%s"},  """
            dataListLabel = ""

            for index, i in enumerate(getDATA[0]):
                if (index == 0): continue
                dataListLabel += baseLabel % (i)

            baseValueSet = """
                {
                  "seriesname": "%s",
                  "data": [  %s ]
                },
            """

            baseValue = """  {value: "%s"},   """

            setDATAset = ""
            for index, i in enumerate(getDATA[1]):
                dataListValue = ""
                for indexj, j in enumerate(i):
                    if (indexj == 0): continue
                    dataListValue += baseValue % (j)

                setDATAset += baseValueSet % (i[0], dataListValue)
        else:

            getDATA  = self.get_RAW()
            print(getDATA)
            baseLabel = """  {label: "%s"},  """
            dataListLabel = ""

            for index, i in enumerate(getDATA[1]):
                dataListLabel += baseLabel % ( i[0]  )


            baseValueSet = """
                {
                  "seriesname": "%s",
                  "data": [  %s ]
                },
            """

            baseValue = """  {value: "%s"},   """

            setDATAset = ""
            for index, i in enumerate(getDATA[0]):
                if (index == 0): continue

                dataListValue = ""
                for j in getDATA[1]:
                    dataListValue += baseValue % ( j[index]  )

                setDATAset +=  baseValueSet % ( getDATA[0][index]  ,  dataListValue)

        unit = "%"
        return JSON_bar % (DATA.title, DATA.subtitle, unit,unit, dataListLabel, setDATAset)







    def CHART_SINGLE(self, DATA):
        getDATA  = self.get_RAW()
        base = """  { "label": "%s", "value": "%s",},  """
        dataList = ""
        for index, i in enumerate(getDATA[1]):
            dataList += base % ( i[0] , i[1]  )

        return JSON_SINGLE % (DATA.title , DATA.subtitle,  dataList )

        getDATA  = self.get_RAW()
        result = []
        for index, i in enumerate(getDATA[1]):
            result.append(  [  i[0], i[1] ] )
            print(i[0], i[1])
        return result


    def CHART_SINGLE_radar(self, DATA):
        getDATA  = self.get_RAW()
        baseLabel = """  {label: "%s"},  """
        baseValue = """  {value: "%s"},   """
        dataListLabel = ""
        dataListValue = ""
        for index, i in enumerate(getDATA[1]):
            dataListLabel += baseLabel % ( i[0]  )
            dataListValue += baseValue % ( i[1]  )

        return JSON_SINGLE_radar % (DATA.title , DATA.subtitle,  dataListLabel , dataListValue )





    def CHART_SINGLE_line(self, DATA):

        if(DATA.layout == "INVERSE"):

            getDATA = self.get_RAW()
            baseLabel = """  {label: "%s"},  """
            dataListLabel = ""

            for index, i in enumerate(getDATA[0]):
                if (index == 0): continue
                dataListLabel += baseLabel % (i)

            baseValueSet = """
                {
                  "seriesname": "%s",
                  "data": [  %s ]
                },
            """

            baseValue = """  {value: "%s"},   """

            setDATAset = ""
            for index, i in enumerate(getDATA[1]):
                dataListValue = ""
                for indexj, j in enumerate(i):
                    if (indexj == 0): continue
                    dataListValue += baseValue % (j)

                setDATAset += baseValueSet % (i[0], dataListValue)
        else:

            getDATA  = self.get_RAW()
            print(getDATA)
            baseLabel = """  {label: "%s"},  """
            dataListLabel = ""

            for index, i in enumerate(getDATA[1]):
                dataListLabel += baseLabel % ( i[0]  )


            baseValueSet = """
                {
                  "seriesname": "%s",
                  "data": [  %s ]
                },
            """

            baseValue = """  {value: "%s"},   """

            setDATAset = ""
            for index, i in enumerate(getDATA[0]):
                if (index == 0): continue

                dataListValue = ""
                for j in getDATA[1]:
                    dataListValue += baseValue % ( j[index]  )

                setDATAset +=  baseValueSet % ( getDATA[0][index]  ,  dataListValue)

        unit = "%"
        return JSON_MATRIX_line % (DATA.title, DATA.subtitle, unit,unit, dataListLabel, setDATAset)



    def CHART_MATRIX(self):
        getDATA  = self.get_RAW()

        for index, i in enumerate(getDATA[0]):
            print(i)
            print( getDATA[1][index] )































