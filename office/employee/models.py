from django.db import models

class employeedetail(models.Model):
    empNo = models.IntegerField()
    empName = models.CharField(max_length=20)
    empSalary = models.IntegerField()
    empAddress = models.CharField(max_length=100)
    empPhoto = models.ImageField(upload_to='office/image/')
    #def __str__(self):
       # return 'Employee details are shared' + self.empName
    def __str__(self):
        return self.empName
