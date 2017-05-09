from django.contrib import admin
from dashboard.models import dashboard, user_info, option, Testiment


class dashAdmin(admin.ModelAdmin):
    list_display = ('user', 'sponsor', 'country', 'ip_addr', 'phoneNum', )


class user_infoAdmin(admin.ModelAdmin):
    list_display = ('user', 'fb_link', 'twi_link', 'gm_link', 'lin_link')


class optionAdmin(admin.ModelAdmin):
    list_display = ('user', 'show_soc', 'autosave', 'allowemail', 'show_pp', 'show_num')


class testimentAdmin(admin.ModelAdmin):
    list_display = ('user', 'msg', 'timestamp',)

admin.site.register(dashboard, dashAdmin)
admin.site.register(user_info, user_infoAdmin)
admin.site.register(option, optionAdmin)
admin.site.register(Testiment, testimentAdmin)
