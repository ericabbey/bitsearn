import datetime
from django.db import models
from django.contrib.auth.models import User


class dashboard(models.Model):
    ACCOUNT_TYPES = (
    ('u', 'ultimate'),
    ('d', 'dynamo'),
    ('p', 'prime'),
    ('n', 'normal'),
)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='dashboard')
    name = models.CharField(max_length=200)
    sponsor = models.ForeignKey(User, related_name='sponsor', blank=True,
                                null=True, on_delete=models.CASCADE)
    securityQ = models.CharField(max_length=200, blank=True, null=True)
    securityA = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200)
    phoneNum = models.CharField(max_length=200)
    ip_addr = models.GenericIPAddressField(blank=True, null=True)
    ref_id = models.CharField(max_length=10, default="1ae8f991ce")
    level = models.IntegerField(default=0)
    acc_type = models.CharField(max_length=1, choices=ACCOUNT_TYPES, default='n')
    date_joined = models.DateTimeField(auto_now_add=True)
    expire = models.DateField(auto_now_add=False, auto_now=False, blank=False, null=False)
    last_login = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def daysleft(self):
        now = datetime.date.today()
        future = self.expire
        delta = future-now
        return delta.days

    def total_ref(self):
        acc_type = self.user.dashboard.acc_type
        if acc_type == 'n':
            ref = 3
        elif acc_type == 'p':
            ref = 10
        elif acc_type == 'd':
            ref = 100
        elif acc_type == 'u':
            ref = 10000
        return ref

    def level_ref(self, lev=None):
        if lev:
            level = lev
        else:
            level = self.user.dashboard.level
        ref = self.total_ref()
        max_ref = ref * (3**(level-1))
        return max_ref


    def ref_made(self, lev=None):
        if lev:
            level = lev
        else:
            level = self.user.dashboard.level
        if level == 0:
            done = 0
        if level == 1:
            done = self.user.parent1.count()
        elif level == 2:
            done = self.user.parent2.count()
        elif level == 3:
            done = self.user.parent3.count()
        elif level == 4:
            done = self.user.parent4.count()

        return done


    def ref_left(self):
        left = self.level_ref() - self.ref_made()
        if left == 1.0:
            left = 0
        return left


class user_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='info')
    user_image = models.FileField(upload_to='user/',
                                  default='/user/default.jpg')
    fb_link = models.CharField(max_length=200, blank=True, null=True)
    twi_link = models.CharField(max_length=200, blank=True, null=True)
    lin_link = models.CharField(max_length=200, blank=True, null=True)
    gm_link = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


class option(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='option')
    show_soc = models.BooleanField(default=True)
    autosave = models.BooleanField(default=False)
    allowemail = models.BooleanField(default=True)
    show_pp = models.BooleanField(default=True)
    show_num = models.BooleanField(default=True)
    dsd = models.BooleanField(default=False)
    dsi = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Testiment(models.Model):
    user = models.ForeignKey(User,related_name="testimonies")
    msg = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ('-timestamp',)
