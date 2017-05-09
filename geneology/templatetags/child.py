from django import template

register = template.Library()

@register.assignment_tag
def child(qs, **kwargs): #
    return qs.filter(**kwargs)\
        .select_related('doner__dashboard',)
