from django.db import models

# Create your models here.
class Subscriber_newsletter(models.Model):
    email=models.CharField(max_length=100)
    class Meta:
         verbose_name = "Subscriber"

    def __str__(self):
        return self.email

class contact_us(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    review=models.CharField(max_length=500)

    class Meta:
        verbose_name = "Contact u"

class DesktopMobileVideo(models.Model):
    desktop_top_video= models.CharField(max_length=200)
    mobile_top_video=models.CharField(max_length=200)
    desktop_bottom_video=models.CharField(max_length=300)
    mobile_bottom_video=models.CharField(max_length=200)





