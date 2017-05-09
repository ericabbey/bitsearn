import datetime
from django import template

register = template.Library()

@register.simple_tag
def daysleft(future): #
    now = datetime.date.today()
    return future - now
