from django.shortcuts import render
from django.http import HttpResponse
from .models import DataStore

# Create your views here.

def home(request):
    return render(request,'app/register.html')
def register(request):
    firstname=request.POST['fname']
    lastname=request.POST['lname']
    quali=request.POST['quali']
    dob=request.POST['dob']
    age=request.POST['age']
    language=request.POST.getlist("language[]")
    
    # print('my name is :',firstname)
    # return render(request.mathod)
    
    DataStore.objects.create(
       First_Name=firstname,
       Last_Name=lastname,
       Age=age,
       Qualification=quali,
       DOB=dob,
       Language=language
    )
    return render(request,'app/login.html')

def data(request):
    all_stu =DataStore.objects.all()
    # print(all_stu)
    students =all_stu.values()
    # print(student)
    return render(request,'app/all_data.html',{'data':students})


# ------------------------login---------

def home(request):
    return render(request,'app/register.html')
def login(request):
    firstname=request.POST['fname']
    lastname=request.POST['lname']
    
    user = DataStore.objects.filter(First_Name=firstname)
    print(user)
    if user:
        if user.First_Name == lastname:
            return render(request,'app/login.html')  
        else:
            msg='user cerieat'
    else:
        msg="Fast_Fname not register"        
    
            
    