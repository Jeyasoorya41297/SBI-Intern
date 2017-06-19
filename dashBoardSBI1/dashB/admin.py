from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Inward)
admin.site.register(InwardData)
admin.site.register(Outward)
admin.site.register(OutwardData)