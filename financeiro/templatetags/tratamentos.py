import locale
from django import template
from decimal import Decimal

register = template.Library()
locale.setlocale( locale.LC_MONETARY, 'pt_BR.UTF-8')

@register.filter
def currency(value):
    
    return locale.currency(value, grouping=True)

@register.filter
def none(value):
    if value == None:
        value = ''
    return (value)


# @register.filter(name='currency')    
# def currency(value):    
#     try:    
#         locale.setlocale(locale.LC_MONETARY,'pt_BR.UTF-8')    
#     except:    
#         locale.setlocale(locale.LC_MONETARY,'')    
#     value = Decimal(value)    
#     loc = locale.localeconv()    
#     return locale.currency(value, loc['currency_symbol'], grouping=True)