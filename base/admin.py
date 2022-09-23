from django.contrib import admin

from.models import Appoinment, Doctor, Patient

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appoinment)