from django import template

register = template.Library()


@register.simple_tag
def get_stars(value):
    return '★' * int(value)

