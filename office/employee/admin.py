from django.contrib import admin
from django.contrib.admin import ModelAdmin
from employee.models import employeedetail
from employee import models
from employee.models import employeedetail


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    emp_list = ['empNo', 'empName', 'empSalary', 'empAddress', 'empDesignation']

admin.site.register(employeedetail, EmployeeAdmin)

