from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True)
    position = models.CharField(max_length=250, null=True)
    dob = models.DateField(null=True)
    profile_image = CloudinaryField('profile_image', null=True, blank = True)
    qualification = models.CharField(max_length=250, null=True)
    status = models.CharField(max_length=250, null=True)
    desc = models.TextField(null=True)
    

    def __str__(self):
        return self.user.username



class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = CloudinaryField('about_us_image', null=True, blank=True)

    def __str__(self):
        return self.title

class OurWork(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = CloudinaryField('ourwork_image', null=True, blank=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('service_image', null=True, blank=True)

    def __str__(self):
        return self.title

class TrustedBy(models.Model):

    image = CloudinaryField('trustedby_image', null=True, blank=True)

class Reviews(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = CloudinaryField('Review_image', null=True, blank=True)

    def __str__(self):
        return self.title
    
class BackgroundImage(models.Model):

    image = CloudinaryField('backgroundimg_image', null=True, blank=True)

class Logo(models.Model):

    image = CloudinaryField('logo_image', null=True, blank=True)