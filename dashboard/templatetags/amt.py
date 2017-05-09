from django import template
from .lev import lev
register = template.Library()

@register.assignment_tag
def amt(args, l=None, a=None):
    total = lev(args, l) * a
    return total
