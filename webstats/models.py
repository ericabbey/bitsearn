from django.contrib.auth.models import User
from django.db import models

class Support(models.Model):
    PRIORITY = (
        ('L', 'low'),
        ('M', 'medium'),
        ('H', 'high'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    priority = models.CharField(max_length=1,choices=PRIORITY, default="L")
    subj = models.CharField(max_length=200)
    msg = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
