from django.db import models
from django.shortcuts import render, redirect, reverse


class Position(models.Model):

    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, related_name="payment_types")
    company_name = models.CharField(max_length=25)
    contact_name = models.CharField(max_length=25)
    date_applied =  models.DateField(auto_now=False, auto_now_add=True)
    responded = models.BooleanField(default=False)
    phone_interview = models.BooleanField(default=False)
    technical_challenge = models.BooleanField(default=False)
    tech_challenge_date =  models.DateField(auto_now=False, auto_now_add=True)
    second_interview = models.BooleanField(default=False)
    hired = models.BooleanField(default=False)
    # *** FKs ***
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("position")
        verbose_name_plural = ("positions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("position_detail", kwargs={"pk": self.pk})
