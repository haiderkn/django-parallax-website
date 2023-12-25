from django.contrib import admin
from .models import ContactModel

# Register your models here.
admin.site.register(ContactModel)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'ask')
    