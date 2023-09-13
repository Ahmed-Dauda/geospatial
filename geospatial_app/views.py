from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Service, AboutUs, Staff


from django.shortcuts import render
from .models import Staff, Service, AboutUs, OurWork

def index(request):
    staff = Staff.objects.all()
    services = Service.objects.all()
    about_us = AboutUs.objects.first()
    return render(request, 'geospatial_app/index.html', {'staff': staff, 'services': services, 'about_us': about_us})



def services(request):
    services_list = Service.objects.all()
    ourwork_list = OurWork.objects.all()
    return render(request, 'geospatial_app/services.html', {'services_list': services_list})

def about_us(request):
    about_us = AboutUs.objects.all()

    return render(request, 'geospatial_app/about_us.html', {'about_us': about_us})


def staff(request):
    staff_list = Staff.objects.all()
    return render(request, 'geospatial_app/staff.html', {'staff_list': staff_list})

