from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Subscriber_newsletter)

@admin.register(contact_us)
class contact_us_users(admin.ModelAdmin):
    list_display = ["name","email","address","phone"]