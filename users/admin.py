from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'name', 'cpf', 'email', 'birth_date', 'is_active', 'is_staff')
    search_fields = ('name', 'email', 'cpf')

admin.site.register(User, UserAdmin)
