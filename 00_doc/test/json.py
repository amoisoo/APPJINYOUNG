import json


#https://rfriend.tistory.com/474

SET_DATA = {
        "chart": {
            "caption": "AAA",
            "subCaption": "bbb",
            "use3DLighting": "0",
            "showPercentValues": "1",
            "decimals": "1",
            "useDataPlotColorForLabels": "1",
            "exportEnabled": "1",
            "theme": "froala"
        },
        "data": [
            {
                "label": "10대",
                "color": "#ff00ff",
                "value": "1250400"
            },
            {
                "label": "중년3",
                "value": "2050700"
            },
            {
                "label": "중년3",
                "value": "205070"
            },
            {
                "label": "노인",
                "value": "491000"
            }
        ]
}

DATA_STRING = """
{
        "chart": {
            "caption": "AAA",
            "subCaption": "bbb",
            "use3DLighting": "0",
            "showPercentValues": "1",
            "decimals": "1",
            "useDataPlotColorForLabels": "1",
            "exportEnabled": "1",
            "theme": "froala"
        },
        "data": [
            {
                "label": "10대",
                "color": "#ff00ff",
                "value": "1250400"
            },
            {
                "label": "중년3",
                "value": "2050700"
            },
            {
                "label": "중년3",
                "value": "205070"
            },
            {
                "label": "노인",
                "value": "491000"
            }
        ]
}
"""

data = {'team': 'Brazil', 'position': 1, 'host': True, 'lastGame': 'Win'}
dictToJson = json.dumps(data)