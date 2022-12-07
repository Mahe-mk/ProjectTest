from django.shortcuts import render
from employee.models import employeedetail
from django.http import HttpResponse
from django.db import models
# Create your views here.

def empDetails(request):
    name='Mahesh.V'
    emp_data = employeedetail.objects.all()
    emp_dict = {'emp_list': emp_data}
   # context.update({'emp_list': emp_data})
    return render(request, 'employee/empdetail.html', context=emp_dict)
    #return render(request,'employee/empdetail.html', {'employee':emp_data})

def index(request):
    return HttpResponse("Hi welcome to index page")

def testing(request):
    return render(request, 'employee/test.html')