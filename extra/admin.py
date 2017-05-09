from django.contrib import admin

from .models import Action, Notif_Count

class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'verb', 'target', 'created')
    list_filter = ('created',)
    search_fields = ('verb',)

class NotifAdmin(admin.ModelAdmin):
    list_display = ('target', 'count')
    list_filter = ('target',)
    search_fields = ('target',)

admin.site.register(Action, ActionAdmin)
admin.site.register(Notif_Count, NotifAdmin)
