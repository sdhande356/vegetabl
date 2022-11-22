
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import Billing
from . forms import BillingForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout




#1.First Function-Intro
def index(request):
    return render(request,"app1/index.html")

#2.Second Function-Sign-up
def signup(request):
  if request.method == "POST":
    fm = SignUpForm(request.POST)
    if fm.is_valid():
      fm.save()
      return HttpResponseRedirect('/login/')
    # return render(request, 'app1/login.html')
  else: 
    fm = SignUpForm() #First time user sees blank form
  return render(request, 'app1/signup.html', {'form':fm})
 
#3.Third function Login

def login_up (request): 
  if not request.user.is_authenticated:#if userr entered data in login
    if request.method == "POST":#heis submitting on bitton
      fm1 = AuthenticationForm(request=request, data=request.POST) #here data inserted by user will come in authentication forms format,it is saved in fm
      if fm1.is_valid(): #if the details are valid
        username = fm1.cleaned_data['username'] #details entered by user stored in local varibales
        password = fm1.cleaned_data['password']
        user = authenticate(username=username, password=password) # compairing details entered by user vs previous details entered during ragistration
        if user is not None:
          login(request,user)
          return HttpResponseRedirect('/first/')
    else: 
      fm1 = AuthenticationForm()
    return render(request, 'app1/login.html', {'form3':fm1})
  else:
    return HttpResponseRedirect('/login/')

#Fourth Function

# Logout
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/')

#Fifth function:
def first(request):
    if request.method=="POST":
        form1=BillingForm(request.POST)
        if form1.is_valid(): #### make all data cleaned
          
          dt=form1.cleaned_data['address']
          it=form1.cleaned_data['item']
          qt=form1.cleaned_data['qty']
          pay=int(it)*int(qt)
          bill=Billing(Payable_amt=pay,item=it,qty=qt,address=dt) #multiplication of qty withhrates
          bill.save()      
    else:
      form1=BillingForm() #Blank Form
    Key2=Billing.objects.all()
    return render(request,"app1/first.html",{"key2":Key2,"form1":form1})

#6TH Function
#Following method will execute when user will click on delete button ,then its id will be fetched in url and it will pass it here
def delete(request, id):#note:here taken requested action and id as parameter
    if request.method =="POST": #if this is true
        di=Billing.objects.get(pk=id) #get method will store the value from databse table into this variable
        di.delete()#and it will delete it.
        return HttpResponseRedirect("/first/")
#7th function
def update(request, id): #note:here taken requested action and id as parameter
    if request.method=="POST": #if its true\print(id)
        pi=Billing.objects.get(pk=id)#pi will store the new values entered by the user in that id
        fm=BillingForm(request.POST,instance=pi)#replacing old values by new values
        if fm.is_valid(): ##if the information given by user is valid 
         
          dt=fm.cleaned_data['address']
          it=fm.cleaned_data['item']
          qt=fm.cleaned_data['qty']
          pay=int(it)*int(qt)
          bill=Billing(id=id,Payable_amt=pay,item=it,qty=qt,address=dt) #multiplication of qty withhrates
          bill.save()   #save the records into database
        return HttpResponseRedirect("/first/") #stay on the same page
    else:
        pi=Billing.objects.get(pk=id)#get method is used to get the values from database table using id which is passed from urls,py,stored in a variable
        fm=BillingForm(instance=pi) #if we dont give instance it wil give blank form ,so we passed instance pi into our blank form(passing old values)
    return render(request,"app1/show.html",{"form":fm}) #with this it will fo show.html


  

    
