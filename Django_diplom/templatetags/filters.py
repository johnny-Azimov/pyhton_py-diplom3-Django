from django import template
register = template.Library()

@register.filter
def cell_paint(value, row):
    index = row.index(value)

    if(index == 13):
        return 'gray'

    if (value == '---' or index == 0 or (float(value) > 0.0 and float(value) < 1.0)):
        return 'white'

    if (float(value) < 0.0):
        return 'green'

    if (float(value) > 1.0 and float(value) < 2.0 ):
        return 'pink'

    if (float(value) >= 2.0 and float(value) < 5.0 ):
        return 'crimson'

    if (float(value) >= 5.0):
        return 'red'