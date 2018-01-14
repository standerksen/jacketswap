from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Jacket(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=300)
    image = models.FileField(default='generic/img/series-placeholder.png')
    added_by = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)
    lost_found = models.CharField(default='found', max_length=5)

    def get_absolute_url(self):
        return reverse('jacket:details', kwargs={'pk': self.pk})

    def __str__(self):
        return '"' + self.title + '" in "' + self.location + '"'
