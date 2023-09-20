from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Service, AboutUs, Staff, TrustedBy, Reviews, BackgroundImage, Logo


from django.shortcuts import render
from .models import Staff, Service, AboutUs, OurWork

def index(request):
    staff = Staff.objects.all()
    services = Service.objects.all()
    trustedby = TrustedBy.objects.all()
    reviews = Reviews.objects.all()
    about_us = AboutUs.objects.first()
    backgroundimage = BackgroundImage.objects.first()
    logo = Logo.objects.first()
    works = OurWork.objects.all()

    context = {
        'staff': staff,
        'services': services, 
        'about_us': about_us,
        'trustedby': trustedby,
        'reviews':reviews,
        'backgroundimage':backgroundimage,
        "logo":logo,
        "works":works
        }
    
    return render(request, 'geospatial_app/index.html', context = context)



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

