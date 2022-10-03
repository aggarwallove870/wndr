from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Subscriber_newsletter)

@admin.register(contact_us)
class contact_us_users(admin.ModelAdmin):
    list_display = ["name","email","address","phone"]


class VideoAdmin(admin.ModelAdmin):
    list_display=["desktop_top_video","mobile_top_video","desktop_bottom_video","mobile_bottom_video"]
    admin.site.register(DesktopMobileVideo)


