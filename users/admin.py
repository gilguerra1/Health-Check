from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):

        list_display = ('id', 'name', 'cpf', 'email', 'birth_date',)
        search_fields = ('name', )

admin.site.register(User, UserAdmin)