from django.db import models

# Create your models here.


class Students(models.Model):
	name = models.CharField(max_length=20)
	maths = models.IntegerField()
	chem = models.IntegerField()
	phy = models.IntegerField()
	cs = models.IntegerField()
	eng = models.IntegerField()
	def __str__(self):
		return self.name