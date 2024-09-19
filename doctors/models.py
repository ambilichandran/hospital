from django.db import models
class Department(models.Model):
    departmentname=models.CharField(max_length=30,blank=None)
    description=models.TextField(max_length=500,blank=None)

    def __str__(self):
        return self.departmentname


class Doctor(models.Model):
    doc_name=models.CharField(max_length=20,blank=False)
    doc_spe=models.CharField(max_length=100,blank=True)
    doc_dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.CharField(max_length=500,blank=False)
    def __str__(self):
        return self.doc_name
    
class Booking(models.Model):
        name=models.CharField(max_length=30,blank=False)
        email=models.EmailField(max_length=40,blank=False)
        phone=models.IntegerField(blank=False)
        date=models.DateField()
        doc_name=models.TextField(max_length=30,blank=False)
        department=models.ForeignKey(Department,on_delete=models.CASCADE)
        message=models.TextField(max_length=500,blank=False)
        def __str__(self):
            return self.name