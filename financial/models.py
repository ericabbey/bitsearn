import qrcode
import io

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

class btcAddr(models.Model):

    def qrcode_location(instance, filename):
        return '%s/qr_codes/%s/' %(instance.user.username, filename)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bitcoin')
    newAddr = models.CharField(max_length=34, blank=True, null=True)
    oldAddr = models.CharField(max_length=34, blank=True, null=True)
    qrcode = models.ImageField(upload_to='qr_code', blank=True, null=True)
    changeCount = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # def save(self, *args, **kwargs):
    #     print('saving_begun')
    #     self.generate_qr()
    #     super(btcAddr, self).save(*args, **kwargs)
    #
    # def generate_qr(self):
    #     print('encoding begun')
    #     qr = qrcode.QRCode(
    #     version=1,
    #     error_corrections=qrcode.constants.ERROR_CORRECT_L,
    #     box_size=10,
    #     border=4
    #     )
    #     qr.add_data(self.newAddr)
    #     qr.make(fit=True)
    #
    #     img = qr.make_image()
    #     buffer = io.StringIO
    #     img.save(buffer)
    #
    #     filename = '%s_qrcode_%i.png' %(self.user.username, changeCount)
    #
    #     filebuffer = InMemoryUploadedFile(buffer, None, filename, 'image/png', buffer.len, None)
    #     self.qrcode.save(filename, filebuffer)

    #
    # def generateQr(self):
    #     qr = qrcode.QRCode(
    #     version=1,
    #     error_corrections=qrcode.constants.ERROR_CORRECT_L,
    #     box_size=10,
    #     border=4
    #     )
    #     qr.add_data(self.newAddr)
    #     qr.make(fit=True)
    #
    #     filename = '%s_qrcode_%i.png' %(self.user.username, changeCount)
    #     img = qr.make_image()
    #     img.save('media_cdn/'+ qrcode_location(self, filename))


class transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction')
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    trans_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=4, decimal_places=3)
    level = models.IntegerField(default=0)
    state = models.CharField(max_length=10, default="pending")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


class missed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='missed')
    was_to =models.ForeignKey(User, on_delete=models.CASCADE, related_name='was_to_user')
    missed_to = models.CharField(max_length=30)
    trans_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=4, decimal_places=3)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
