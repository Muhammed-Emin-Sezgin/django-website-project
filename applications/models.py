from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from isIlan.models import Ilan


class Applications(models.Model):
    STATUS = (
        ('True', 'True'),
        ('Pending', 'Pending'),
        ('False', 'False'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    job = models.ForeignKey(Ilan, on_delete=models.SET_NULL, null=True)
    applicationDate = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='Pending')

    def jobPublisher(self):
        return self.job

    def jobName(self):
        return self.job.ilanBaslik
