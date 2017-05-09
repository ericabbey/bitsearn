from django.contrib import admin
from .models import btcAddr, transaction, missed


class BtcAddrAdmin(admin.ModelAdmin):
    list_display = ('user', 'newAddr', 'oldAddr', 'updated', 'timestamp', )

class TransAdmin(admin.ModelAdmin):
    list_display = ('user', 'to', 'trans_id', 'amount', 'state', 'timestamp', )

class MissedAdmin(admin.ModelAdmin):
    list_display = ('user', 'was_to', 'missed_to', 'amount', 'trans_id', 'timestamp', )

admin.site.register(btcAddr, BtcAddrAdmin)
admin.site.register(transaction, TransAdmin)
admin.site.register(missed, MissedAdmin)
# Register your models here.
