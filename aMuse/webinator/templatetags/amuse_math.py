from django import template
register = template.Library()


@register.filter()
def mult(value, arg):
    return float(value) * float(arg)

@register.filter()
def module(value, arg):
    return float(value) % float(arg)

@register.filter()
def get_uidb36( value ):
    return  value.split('-')[0]

@register.filter()
def get_token( value ):
    return  value.split('-')[1]
