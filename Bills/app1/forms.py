from django import forms
from  . models import Billing
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email',]
  labels = {'email': 'Email'}
  widgets={
        'username': forms.TextInput(attrs={"class":"form-control"}),
        'first_name': forms.TextInput(attrs={"class":"form-control"}),
        'last_name': forms.TextInput(attrs={"class":"form-control"}),
        'email': forms.TextInput(attrs={"class":"form-control"}),
        'password': forms.TextInput(attrs={"class":"form-control"}),
        '(confirm_password_again)': forms.TextInput(attrs={"class":"form-control"}),
        }


            
class BillingForm(forms.ModelForm):
    
    # item =forms.ChoiceField(choices=Item_CHOICES,required=True,widget=forms.Select(attrs={'class':'form-select'}))
    class Meta:    
        model=Billing
        fields=("address","item","qty")
        widgets={                                                         #for giving styles to attributes of forms since in we cant access each field individually in html.
        'address': forms.TextInput(attrs={"class":"form-control"}),
        
        'qty': forms.TextInput(attrs={"class":"form-control"}),
}