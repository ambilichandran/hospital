from django.contrib import admin
from .models import Department, Doctor, Booking
class BookingAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','date','doc_name','department','message']
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Booking,BookingAdmin)
