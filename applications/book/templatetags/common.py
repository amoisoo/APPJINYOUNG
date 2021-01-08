from django import template
from django.conf import settings
from django.utils.html import mark_safe
from django.template.defaultfilters import stringfilter
import locale

register = template.Library()
locale.setlocale(locale.LC_ALL, '')
register = template.Library()

# settings value
@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")



#-----------------------------------------------------
# List
#-----------------------------------------------------

@register.filter
def getlist(list, num):
    try:
        return list[num]
    except:
        return []


#-----------------------------------------------------
# Dictional
#-----------------------------------------------------

@register.filter
def hash(dict_data, key):
    try:
        return dict_data[str(key)]
    except:
        return []

#-----------------------------------------------------

@register.filter
def sum(dict_data, key):
    try:
        getList = dict_data[str(key)]
        result = 0
        for i in getList:
            result += int(i.subtitle)
        return result
    except:
        return " -1 (Error)"

#-----------------------------------------------------

@register.filter()
def currency(value):
    try:
        setValue  = int(value)
        return ( locale.currency(setValue, symbol=False ,  grouping=True ))
    except:
        return 0
#https://www.djangosnippets.org/snippets/552/
#-----------------------------------------------------


@register.filter
def code_space(data):


    getList = data.split('\n')

    result = ""
    for i in getList:
        result += mark_safe(i ) + mark_safe( "<br/><br/>"  )

    return result
    return mark_safe(result)




@register.filter('setDicValue')
def setDicValue(dict_data, key):
    """
    usage example {{ your_dict|setDicValue:your_key }}
    """
    if key:
        return dict_data.get(key)


#-----------------------------------------------------

@register.filter
def ftable_2_tchart(table, data):
    try:
        print("CHART OK")

        from core.LIB.FROALA_CHART import FROALA_TABLE_2_CHART
        DATA = FROALA_TABLE_2_CHART.IO(table)
        result = DATA.get_DATA( data  )
        return result
    except:
        print("CHART ERROR")
        return None




#-----------------------------------------------------

@register.filter
def m2m_list(data):
    try:
        return data.all()
    except:
        return []




