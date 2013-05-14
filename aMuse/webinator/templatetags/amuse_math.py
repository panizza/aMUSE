from django import template
register = template.Library()


@register.filter()
def mult(value, arg):
    return float(value) * float(arg)

@register.filter()
def module(value, arg):
    return float(value) % float(arg)
