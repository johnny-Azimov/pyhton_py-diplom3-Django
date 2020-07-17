from django import template

register = template.Library()


@register.filter
def text_short(value, arg=100):
    return value[:arg] + '...'

