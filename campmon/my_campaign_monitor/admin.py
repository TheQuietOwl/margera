from django.contrib import admin

# Register your models here.
from .models import subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display=('email','name')


admin.site.register(subscriber)