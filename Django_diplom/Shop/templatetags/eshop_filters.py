from django import template

register = template.Library()


@register.filter
def mul(val_1, val_2):
    return int(val_1) * int(val_2)


@register.filter
def get_items(value, arg=''):
    result = ''
    if isinstance(value, dict):
        result = value.get(arg, '')
    return result

