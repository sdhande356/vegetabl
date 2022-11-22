from django.db import models
from datetime import *
Item_CHOICES = (
        ("0",'---select item----'),
        ("10",'Potates'),
        ("20",'Tomotoes'),
        ("30",'Onion'),
        ("40",'Cabbage'),
        ("50",'Apple'),
    )
# Create your models here.
class Billing(models.Model): #this is class for craetaing table in database
    #Attributes:
    
    
    
    address=models.CharField(max_length=50,default='dd')
    Payable_amt=models.IntegerField(max_length=50)
    item=models.CharField(max_length=50,choices=Item_CHOICES, default='0')
    qty=models.IntegerField(max_length=50)
   
   

