from django.contrib.auth.models import User
from django.db import models


class Jacket(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(default='No description.')
    location = models.CharField(max_length=300)
    image = models.FileField(default='generic/img/series-placeholder.png')
    added_by = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)
    lost_found = models.CharField(default='found', max_length=5)
