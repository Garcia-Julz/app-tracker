from django.db import models
from django.contrib.auth.models import User

class Applicant(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    graduated = models.CharField(max_length=15)

    class Meta:
        verbose_name = ('applicant')
        verbose_name_plural = ('applicants')