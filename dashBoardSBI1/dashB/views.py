from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
	i_apps = Inward.objects.all()
	o_no_apps = len(list(Outward.objects.all()))
	o_comm_list = list(OutwardData.objects.all().order_by('-Date').values_list('commissionAmt'))[0:o_no_apps-1]
	o_amt_list = list(OutwardData.objects.all().order_by('-Date').values_list('BeneficiaryAmountINR'))[0:o_no_apps-1]
	o_comm = 0
	for out in o_comm_list:
		o_comm = o_comm+out[0]
	o_amt = 0
	for out in o_amt_list:
		o_amt = o_amt+out[0]
	i_no_apps = len(list(i_apps))
	i_comm_list = list(InwardData.objects.all().order_by('-Date').values_list('GLS_commission'))[0:i_no_apps-1]
	i_commex_list = list(InwardData.objects.all().order_by('-Date').values_list('Ex_commission'))[0:i_no_apps-1]
	i_amt_list = list(InwardData.objects.all().order_by('-Date').values_list('amountINR'))[0:i_no_apps-1]
	i_comm_gls = 0
	for i in i_comm_list:
		i_comm_gls = i_comm_gls+i[0]
	i_comm_ex = 0
	for i in i_commex_list:
		i_comm_ex = i_comm_ex+i[0]
	i_comm = i_comm_ex+i_comm_gls
	i_amt = 0
	for i in i_amt_list:
		i_amt = i_amt+i[0]
	return render(request,"dashB/index.html",{"inward":i_apps,"o_comm":o_comm,"o_amt":o_amt,"i_comm":i_comm,"i_amt":i_amt})