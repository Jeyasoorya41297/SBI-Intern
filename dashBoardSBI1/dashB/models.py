from django.db import models

# Create your models here.
class Inward(models.Model):
	App_name = models.CharField(max_length=20)
	def __str__(self):
		return self.App_name

class InwardData(models.Model):
	amount = models.DecimalField(max_digits=15, decimal_places=2)
	amountINR = models.DecimalField(max_digits=15, decimal_places=2)
	GLS_commission = models.DecimalField(max_digits=15, decimal_places=2)
	Ex_commission = models.DecimalField(max_digits=15, decimal_places=2)
	Service_tax = models.DecimalField(max_digits=15, decimal_places=2)
	Date = models.DateField() 
	App = models.ForeignKey(Inward, on_delete=models.CASCADE)
	def __str__(self):
		return self.App.App_name+" "+str(self.Date)

class Outward(models.Model):
	Currency = models.CharField(max_length=10)
	def __str__(self):
		return self.Currency

class OutwardData(models.Model):
	BeneficiaryAmount = models.DecimalField(max_digits=15, decimal_places=2)
	BeneficiaryAmountINR = models.DecimalField(max_digits=15, decimal_places=2)
	commissionAmt = models.DecimalField(max_digits=15, decimal_places=2)
	Service_tax = models.DecimalField(max_digits=15, decimal_places=2)
	Date = models.DateField()
	curr = models.ForeignKey(Outward, on_delete=models.CASCADE) 
	def __str__(self):
		return self.curr.Currency+" "+str(self.Date)