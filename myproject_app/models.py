from django.db import models

class TableNumbers(models.Model):
    number = models.IntegerField(unique=True)
    order = models.IntegerField()
    price_dollar = models.FloatField()
    delivery_data = models.DateField()
    price_rub = models.FloatField()

