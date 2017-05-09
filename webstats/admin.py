from django.contrib import admin

from .models import Support

class SupportAdmin(admin.ModelAdmin):
    list_display = ('user', 'priority', 'subj', 'msg')

admin.site.register(Support, SupportAdmin)
