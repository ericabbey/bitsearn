from django import template

register = template.Library()

@register.assignment_tag
def lev(args, l=None):
    if l:
        level = l
    else:
        level = args.user.dashboard.level
    ref = args.total_ref()
    max_ref = ref * (3**(level-1))
    return max_ref
