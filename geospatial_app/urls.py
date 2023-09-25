from django.urls import path
from . import views

from .views import StaffDetail, ServicesDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about_us/', views.about_us, name='about_us'),
    path('staff/', views.staff, name='staff'),
    path('staffdetail/<int:pk>/', StaffDetail.as_view(), name='staffdetail'),
    path('servicesdetail/<int:pk>/', ServicesDetail.as_view(), name='servicesdetail'),
]
