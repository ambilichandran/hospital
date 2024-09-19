from django.shortcuts import render, redirect
from .models import Department, Doctor
from .forms import BookingForm
def index (request):
    data=Department.objects.all()
    doc=Doctor.objects.all()
    form=BookingForm()
    
    context = {
        "data":data,
        "doc":doc, 
        "form":form
    }
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("/")
    return render(request,"index.html",context)
