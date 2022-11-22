from django.contrib import admin
from . models import Billing

# Register your models here.
@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display= ("id","address","Payable_amt","item",'qty')
