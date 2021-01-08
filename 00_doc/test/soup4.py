

table = """

<table align="center" class="table mb-0 table-bordered table-sm table-width-80">
	<thead>
		<tr>
			<th style="width: 19.9197%;">label</th>
			<th style="width: 19.881%;">한국</th>
			<th style="width: 19.8809%;">중국</th>
			<th style="width: 20.0803%;">일본</th>
			<th style="width: 20.0000%;">인도</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="width: 19.9197%;">10대</td>
			<td style="width: 19.881%;">11</td>
			<td style="width: 19.8809%;">21</td>
			<td style="width: 20.0803%;">31</td>
			<td style="width: 20.0000%;">41</td>
		</tr>
		<tr>
			<td style="width: 19.9197%;">20대</td>
			<td style="width: 19.881%;">12</td>
			<td style="width: 19.8809%;">22</td>
			<td style="width: 20.0803%;">32</td>
			<td style="width: 20.0000%;">42</td>
		</tr>
		<tr>
			<td style="width: 19.9197%;">30대</td>
			<td style="width: 19.881%;">13</td>
			<td style="width: 19.8809%;">23</td>
			<td style="width: 20.0803%;">33</td>
			<td style="width: 20.0000%;">43</td>
		</tr>
		<tr>
			<td style="width: 19.9197%;">40대</td>
			<td style="width: 19.881%;">14</td>
			<td style="width: 19.8809%;">24</td>
			<td style="width: 20.0803%;">34</td>
			<td style="width: 20.0000%;">44</td>
		</tr>
		<tr>
			<td style="width: 19.9197%;">50대</td>
			<td style="width: 19.881%;">15</td>
			<td style="width: 19.8809%;">25</td>
			<td style="width: 20.0803%;">35</td>
			<td style="width: 20.0000%;">45</td>
		</tr>
	</tbody>
</table>
<br>

"""
from bs4 import BeautifulSoup




class TABLE:

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
        result.append( self.getTableHEADER() )
        result.append( self.getTableBODY()  )
        return result

    def CHART_SINGLE(self):
        getDATA  = self.get_RAW()
        result = []
        for index, i in enumerate(getDATA[1]):
            result.append(  [  i[0], i[1] ] )
            print(i[0], i[1])
        return result

    def CHART_PIE(self):
        getDATA  = self.get_RAW()

        for index, i in enumerate(getDATA[0]):
            print(i)
            print( getDATA[1][index] )
DATA = TABLE(table)

getList = DATA.CHART_SINGLE()


