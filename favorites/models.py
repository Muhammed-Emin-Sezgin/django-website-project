from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from isIlan.models import Ilan


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    job = models.ForeignKey(Ilan, on_delete=models.SET_NULL, null=True)

    def jobPublisher(self):
        return self.job

    def jobName(self):
        return self.job.ilanBaslik
