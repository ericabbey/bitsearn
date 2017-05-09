from django.contrib import admin
from .models import tree, Descendant


class treeAdmin(admin.ModelAdmin):
    list_display = ['doner', 'p1', 'p2', 'p3', 'p4', 'ref_id']


class DescendantAdmin(admin.ModelAdmin):
    list_display = ['upliner', 'downliner',]

admin.site.register(tree, treeAdmin)
admin.site.register(Descendant, DescendantAdmin)
# Register your models here.
