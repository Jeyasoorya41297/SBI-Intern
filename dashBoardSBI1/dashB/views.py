from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Sum
# Create your views here.

def index(request):
	i_apps = Inward.objects.all()
	o_apps = Outward.objects.all().order_by('-id')
	o_comm_months = list(OutwardData.objects.order_by('Date').values('Date').annotate(cAmt=Sum('commissionAmt')))
	o_amt_months = list(OutwardData.objects.order_by('Date').values('Date').annotate(amt=Sum('BeneficiaryAmountINR')))
	i_comm_months = list(InwardData.objects.order_by('Date').values('Date').annotate(cAmt=Sum('GLS_commission')))
	i_commex_months = list(InwardData.objects.order_by('Date').values('Date').annotate(cexAmt=Sum('Ex_commission')))
	i_amt_months = list(InwardData.objects.order_by('Date').values('Date').annotate(amt=Sum('amountINR')))
	for i in range(0,len(i_comm_months)-1):
		i_comm_months[i]['cAmt']=i_comm_months[i]['cAmt']+i_commex_months[i]['cexAmt']
	o_comm = o_comm_months[len(o_comm_months)-1]['cAmt']
	i_comm = i_comm_months[len(i_comm_months)-1]['cAmt']
	o_amt = o_amt_months[len(o_amt_months)-1]['amt']
	i_amt = i_amt_months[len(i_amt_months)-1]['amt']
	return render(request,"dashB/index.html",{"outward":o_apps,"inward":i_apps,"o_comm":o_comm,"i_comm":i_comm,"o_comm_months":o_comm_months,"o_amt":o_amt,"i_comm_months":i_comm_months,"i_amt":i_amt})

def outward_view(request,id):
	# i_apps = Inward.objects.all()
	i_apps = Inward.objects.all().order_by('-id')
	o_apps = Outward.objects.all().order_by('-id')
	o_data = OutwardData.objects.filter(curr__pk=id)

	return render(request,"dashB/outward.html",{"outward":o_apps,"inward":i_apps,"outwardData":o_data})

def inward_view(request,id):
	i_apps = Inward.objects.all()
	o_apps = Outward.objects.all().order_by('-id')
	return render(request,"dashB/inward.html",{"outward":o_apps,"inward":i_apps})