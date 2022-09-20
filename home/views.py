from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def doctor(request):
    return render(request, 'doctor.html')
def contact(request):
    return render(request, 'contact.html')
def doctor(request):
    return render(request, 'doctor.html')
def booking(request):
    return render(request, 'booking.html')