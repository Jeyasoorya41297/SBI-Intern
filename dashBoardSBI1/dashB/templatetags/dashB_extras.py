from django import template

register = template.Library()

@register.filter
def return_item(l, i):
    try:
        return l[i]
    except:
        return None

@register.filter
def return_index(l,i):
	print(l)
	print(i)
	try:
		return l[i-1]['cAmt']
	except:
		return None