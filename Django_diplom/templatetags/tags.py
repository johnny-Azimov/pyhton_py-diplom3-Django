from django import template

register = template.Library()

@register.simple_tag
def view_act(name_tmp, name_view):
    if name_tmp == name_view:
        name_act = 'active'
    else:
        name_act = 'not active'
    return name_act

