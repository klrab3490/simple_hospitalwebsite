from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm,Feedbackform
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'feedback.html')
    form = Feedbackform()
    form_dict = {
        'form' : form
    }
    return render(request, 'contact.html',form_dict)

def doctors(request):
    doc_dict = {
        'doctors' : Doctors.objects.all()
    }
    return render(request, 'doctors.html',doc_dict)

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    form_dict = {
        'form' : form
    }
    return render(request, 'booking.html', form_dict)

def department(request):
    dept_dict ={
        'dept' : Departments.objects.all()
    }
    return render(request, 'department.html',dept_dict)
