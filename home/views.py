from django.shortcuts import render,HttpResponse
from home.models import Department
from home.models import Doctor
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def depp(request):
    depdict={
        'dep':Department.objects.all()
            }
    print(depdict.values())
    return render(request, 'departments.html',depdict)


def doc(request):
    docv={
        'doc':Doctor.objects.all()
         }
    print(docv.values())
    return render(request,'doctor.html',docv)


def contact(request):
    return render(request, 'contact.html')
def doctor(request):
    return render(request, 'doctor.html')


def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form=BookingForm()
    dform={
        'form':form
    }

    return render(request, 'booking.html',dform)