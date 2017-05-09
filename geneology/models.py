from django.db import models
from django.contrib.auth.models import User


class tree(models.Model):
    doner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="downliner",
                              )
    p1 = models.ForeignKey(User, on_delete=models.CASCADE,
                           related_name="parent1",
                           )
    p2 = models.ForeignKey(User, on_delete=models.CASCADE,
                           related_name="parent2",
                           )
    p3 = models.ForeignKey(User, on_delete=models.CASCADE,
                           related_name="parent3",
                           )
    p4 = models.ForeignKey(User,
                           related_name="parent4",
                           )
    ref_id = models.CharField(max_length=10)


class Descendant(models.Model):
    upliner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="upliner")
    downliner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="child")
