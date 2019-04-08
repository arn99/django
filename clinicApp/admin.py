from django.contrib import admin
from .models import Contact,About,New,Appointment,Appreciation,Service,Categorie
# Register your models here.

admin.site.register(Contact)
admin.site.register(About)
admin.site.register(New)
admin.site.register(Service)
admin.site.register(Categorie)
admin.site.register(Appointment)
admin.site.register(Appreciation)