from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget
from django.db import models
from .models import Staff
from .models import Staff, Service, AboutUs, OurWork, TrustedBy, Reviews, BackgroundImage, Logo

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

class TrustedByAdmin(admin.ModelAdmin):
    list_display = ('image',)

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('title','desc')

class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ('image',)

class LogoAdmin(admin.ModelAdmin):
    list_display = ('image',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(OurWork, OurWorkAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(TrustedBy, TrustedByAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(BackgroundImage, BackgroundImageAdmin)
admin.site.register(Logo, LogoAdmin)