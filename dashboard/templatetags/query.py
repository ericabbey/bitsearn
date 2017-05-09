from django import template

register = template.Library()

@register.assignment_tag
def query(qs, **kwargs): # Only one argument
    return qs.filter(**kwargs)
