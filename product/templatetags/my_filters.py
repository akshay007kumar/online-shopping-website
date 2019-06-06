from django import template

register = template.Library()


@register.filter()
def discount(value, disc):
    return value - (value*disc)/100


@register.filter()
def short_desc(value):
    return value[0:60] + '.....'


@register.filter()
def short_name(value):
    return value[0:40] + '..'
