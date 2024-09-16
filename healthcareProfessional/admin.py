from django.contrib import admin
from .models import HealthProfessional, Specialization

class HealthProfessionalAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'birth_date', 'registration_number', 'specialization', )
    search_fields = ('name', 'registration_number')

admin.site.register(HealthProfessional, HealthProfessionalAdmin)

class SpecializationAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Specialization, SpecializationAdmin)
