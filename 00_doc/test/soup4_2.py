

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

from core.LIB.FROALA_CHART import FROALA_TABLE_2_CHART


DATA = FROALA_TABLE_2_CHART.IO( table )



DATA.CHART_SINGLE()


