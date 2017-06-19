from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
	studList = Students.objects.all()
	l=[]
	d={}
	for s in studList:
		d[s.name]=s.maths
	l.append(d)
	d={}
	for s in studList:
		d[s.name]=s.chem
	l.append(d)
	d={}
	for s in studList:
		d[s.name]=s.phy
	l.append(d)
	d={}
	for s in studList:
		d[s.name]=s.cs
	l.append(d)
	d={}
	for s in studList:
		d[s.name]=s.eng
	l.append(d)
	return render(request,'dashb/index.html',{'stud':studList,'l':l})

def chart(request,id):
	studList = Students.objects.all()
	student = Students.objects.get(id=id)
	return render(request,'dashb/charts.html',{'stud':studList,'student':student})