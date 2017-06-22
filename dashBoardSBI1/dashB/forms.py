from django import forms
import datetime
from .models import *

class Ograph(forms.Form):
    ch_of_graph = forms.ChoiceField(choices=(('BeneficiaryAmount','Beneficiary Amount'),('BeneficiaryAmountINR','Beneficiary Amount in INR'),('commissionAmt','Commission'),('Service_tax','Service Tax')))

class Igraph(forms.Form):
	ch_of_graph = forms.ChoiceField(choices=(('amount','Amount'),('amountINR','Amount in INR'),('GLS_commission','GLS Commission'),('Ex_commission','Exchange Commission'),('Service_tax','Service Tax')))