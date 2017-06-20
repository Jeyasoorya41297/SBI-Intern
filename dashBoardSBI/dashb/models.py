from django.db import models

# Create your models here.


class Inward(models.Model):
	App_name = models.CharField(max_length=20)
	amount = models.DecimalField(max_digits=15, decimal_places=2)
	amountINR = models.DecimalField(max_digits=15, decimal_places=2)
	GLS_commission = models.DecimalField(max_digits=15, decimal_places=2)
	Ex_commission = models.DecimalField(max_digits=15, decimal_places=2)
	Service_tax = models.DecimalField(max_digits=15, decimal_places=2)
	Date = models.Date.Field() 
	def __str__(self):
		return self.App_name

class Inward(models.Model):
	App_name = models.CharField(max_length=20)
	Currency = models.CharField(max_length=10)
	amountForeign = models.DecimalField(max_digits=15, decimal_places=2)
	amountINR = models.DecimalField(max_digits=15, decimal_places=2)
	GLS_commission = models.DecimalField(max_digits=15, decimal_places=2)
	Service_tax = models.DecimalField(max_digits=15, decimal_places=2)
	Date = models.Date.Field() 
	def __str__(self):
		return self.App_name