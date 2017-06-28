from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from decimal import Decimal
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
	i_apps = Inward.objects.all()
	o_apps = Outward.objects.all()
	
	o_comm_months = list(OutwardData.objects.order_by('Date').values('Date').annotate(cAmt=Sum('commissionAmt')))
	o_amt_months = list(OutwardData.objects.order_by('Date').values('Date').annotate(amt=Sum('BeneficiaryAmountINR')))
	
	i_comm_months = list(InwardData.objects.order_by('Date').values('Date').annotate(cAmt=Sum('GLS_commission')))
	i_commex_months = list(InwardData.objects.order_by('Date').values('Date').annotate(cexAmt=Sum('Ex_commission')))
	i_amt_months = list(InwardData.objects.order_by('Date').values('Date').annotate(amt=Sum('amountINR')))
	
	for i in range(0,len(i_comm_months)-1):
		i_comm_months[i]['cAmt']=i_comm_months[i]['cAmt']+i_commex_months[i]['cexAmt']

	list_of_values = [o_comm_months[-1]['cAmt'],o_amt_months[-1]['amt'],i_comm_months[-1]['cAmt'],i_amt_months[-1]['amt']]

	if len(o_comm_months) >= 2:
		#<i class="green"><i class="fa fa-sort-asc"></i>3% </i> From last Month
		if (o_comm_months[-1]['cAmt']-o_comm_months[-2]['cAmt']) >= 0:
			list_of_values.append("<i class=\"green\"><i class=\"fa fa-sort-asc\"></i> "+str((abs((o_comm_months[-1]['cAmt']-o_comm_months[-2]['cAmt'])/o_comm_months[-2]['cAmt'])*100).quantize(Decimal('.01')))+"%</i> From last Month")
		else :
			list_of_values.append("<i class=\"red\"><i class=\"fa fa-sort-desc\"></i> "+str((abs((o_comm_months[-1]['cAmt']-o_comm_months[-2]['cAmt'])/o_comm_months[-2]['cAmt'])*100).quantize(Decimal('.01')))+"%</i> From last Month")

		if (o_amt_months[-1]['amt']-o_amt_months[-2]['amt']) >= 0:
			list_of_values.append("<i class=\"green\"><i class=\"fa fa-sort-asc\"></i> "+str((abs((o_amt_months[-1]['amt']-o_amt_months[-2]['amt'])/o_amt_months[-2]['amt'])*100).quantize(Decimal('.01')))+"%</i> From last Month")
		else :
			list_of_values.append("<i class=\"red\"><i class=\"fa fa-sort-desc\"></i> "+str((abs((o_amt_months[-1]['amt']-o_amt_months[-2]['amt'])/o_amt_months[-2]['amt'])*100).quantize(Decimal('.01')))+"%</i> From last Month")
	else :
		list_of_values.append("")
		list_of_values.append("")

	if len(i_comm_months) >= 2:
		if (i_comm_months[-1]['cAmt']-i_comm_months[-2]['cAmt']) >= 0:
			list_of_values.append("<i class=\"green\"><i class=\"fa fa-sort-asc\"></i> "+str((abs((i_comm_months[-1]['cAmt']-i_comm_months[-2]['cAmt'])/i_comm_months[-2]['cAmt'])*100).quantize(Decimal('.01')))+"%</i> From last Month")
		else :
			list_of_values.append("<i class=\"red\"><i class=\"fa fa-sort-desc\"></i> "+str((abs((i_comm_months[-1]['cAmt']-i_comm_months[-2]['cAmt'])/i_comm_months[-2]['cAmt'])*100).quantize(Decimal('.01')))+"%</i> From last Month")

		if (i_amt_months[-1]['amt']-i_amt_months[-2]['amt']) >= 0:
			list_of_values.append("<i class=\"green\"><i class=\"fa fa-sort-asc\"></i> "+str((abs((i_amt_months[-1]['amt']-i_amt_months[-2]['amt'])/i_amt_months[-2]['amt'])*100).quantize(Decimal('.01')))+"%</i> From last Month")
		else :
			list_of_values.append("<i class=\"red\"><i class=\"fa fa-sort-desc\"></i> "+str((abs((i_amt_months[-1]['amt']-i_amt_months[-2]['amt'])/i_amt_months[-2]['amt'])*100).quantize(Decimal('.01')))+"%</i> From last Month")
	else :
		list_of_values.append("")
		list_of_values.append("")

	if len(o_comm_months) > 7:
		o_comm_months=o_comm_months[-7:]
	if len(i_comm_months) > 7:
		i_comm_months=i_comm_months[-7:]
	
	return render(request,"dashB/index.html",{"list_of_values":list_of_values,"outward":o_apps,"inward":i_apps,"o_comm_months":o_comm_months,"i_comm_months":i_comm_months})

@csrf_exempt
def outward_view(request,name):
	i_apps = Inward.objects.all()
	o_apps = Outward.objects.all()
	selected_curr = Outward.objects.get(Currency=name)
	if request.method == 'POST':
		form = Ograph(request.POST)
		if form.is_valid():
			sel_field = request.POST['ch_of_graph']
			in_date=request.POST['in_date']
			fi_date=request.POST['fi_date']

			x_data = list(OutwardData.objects.filter(curr__Currency=name,Date__gte=in_date,Date__lte=fi_date).order_by("Date").values("Date",request.POST['ch_of_graph']))
			print(x_data)
		else :
			form = Ograph()
			sel_field='BeneficiaryAmount'
			x_data = list(OutwardData.objects.filter(curr__Currency=name).order_by("Date").values("Date",'BeneficiaryAmount'))
			if len(x_data) > 10:
				x_data = x_data[-10:]
	else :
		form = Ograph()
		sel_field='BeneficiaryAmount'
		x_data = list(OutwardData.objects.filter(curr__Currency=name).order_by("Date").values("Date",'BeneficiaryAmount'))
		if len(x_data)>10 :
			x_data = x_data[-10:]
	
	return render(request,"dashB/outward.html",{"outward":o_apps,"inward":i_apps,"data":x_data,"form":form,"curr":selected_curr,"sel_field":sel_field})

@csrf_exempt
def inward_view(request,name):
	i_apps = Inward.objects.all()
	o_apps = Outward.objects.all()
	selected_app = Inward.objects.get(App_name=name)
	if request.method == 'POST':
		form = Igraph(request.POST)
		if form.is_valid():
			sel_field = request.POST['ch_of_graph']
			in_date=request.POST['in_date']
			fi_date=request.POST['fi_date']
			x_data = list(InwardData.objects.filter(App__App_name=name,Date__gte=in_date,Date__lte=fi_date).order_by("Date").values("Date",request.POST['ch_of_graph']))
			print(x_data)
		else :
			form = Igraph()
			sel_field='amountINR'
			x_data = list(InwardData.objects.filter(App__App_name=name).order_by("Date").values("Date",'amountINR'))
			if len(x_data) > 10:
				x_data = x_data[-10:]

	else :
		form = Igraph()
		sel_field='amountINR'
		x_data = list(InwardData.objects.filter(App__App_name=name).order_by("Date").values("Date",'amountINR'))
		if len(x_data) > 10:
			x_data = x_data[-10:]

	return render(request,"dashB/inward.html",{"outward":o_apps,"inward":i_apps,"data":x_data,"form":form,"app":selected_app,"sel_field":sel_field})

@csrf_exempt
def compOut_view(request) :
	i_apps = Inward.objects.all()
	o_apps = Outward.objects.all()
	if request.method=='POST':
		form = compout(request.POST)
		if form.is_valid():
			sel_field = request.POST['ch_of_graph']
			in_date=request.POST['in_date']
			fi_date=request.POST['fi_date']
			x_data = list(OutwardData.objects.filter(Date__gte=in_date,Date__lte=fi_date).values('curr__Currency').annotate(x_val=Sum(sel_field)))
		else:
			form = compout()
			sel_field = 'BeneficiaryAmountINR'
			x_data = list(OutwardData.objects.values('curr__Currency').annotate(x_val=Sum(sel_field)))
			if len(x_data) > 10:
				x_data = x_data[-10:]
	else:
		form = compout()
		sel_field = 'BeneficiaryAmountINR'
		x_data = list(OutwardData.objects.values('curr__Currency').annotate(x_val=Sum(sel_field)))
		if len(x_data) > 10:
			x_data = x_data[-10:]
	return render(request,"dashB/compout.html",{"outward":o_apps,"inward":i_apps,"sel_field":sel_field,"x_data":x_data})

@csrf_exempt
def compIn_view(request) :
	i_apps = Inward.objects.all()
	o_apps = Outward.objects.all()
	if request.method=='POST':
		form = compin(request.POST)
		if form.is_valid():
			sel_field = request.POST['ch_of_graph']
			in_date=request.POST['in_date']
			fi_date=request.POST['fi_date']
			x_data = list(InwardData.objects.filter(Date__gte=in_date,Date__lte=fi_date).values('App__App_name').annotate(x_val=Sum(sel_field)))
		else:
			form = compin()
			sel_field = 'amountINR'
			x_data = list(InwardData.objects.values('App__App_name').annotate(x_val=Sum(sel_field)))
			if len(x_data) > 10:
				x_data = x_data[-10:]

	else:
		form = compin()
		sel_field = 'amountINR'
		x_data = list(InwardData.objects.values('App__App_name').annotate(x_val=Sum(sel_field)))
		if len(x_data) > 10 :
			x_data = x_data[-10:]

	return render(request,"dashB/compin.html",{"outward":o_apps,"inward":i_apps,"sel_field":sel_field,"x_data":x_data})

def view_data(request):
	i_apps = Inward.objects.all()
	o_apps = Outward.objects.all()
	outward_data = OutwardData.objects.all().order_by('-Date')
	inward_data = InwardData.objects.all().order_by('-Date')
	return render(request,"dashB/viewData.html",{"outward":o_apps,"inward":i_apps,"outward_data":outward_data,"inward_data":inward_data})
