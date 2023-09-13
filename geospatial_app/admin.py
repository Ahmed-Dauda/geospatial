from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget
from django.db import models
from .models import Staff
from .models import Staff, Service, AboutUs, OurWork

# Register your models here.



class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'position')
    formfield_overrides = {
        models.DateField: {'widget': AdminDateWidget(attrs={'style': 'width: 10em;'})},
    }


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)

class OurWorkAdmin(admin.ModelAdmin):
    list_display = ('title',)



admin.site.register(Service, ServiceAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(OurWork, OurWorkAdmin)

admin.site.register(Staff, StaffAdmin)
