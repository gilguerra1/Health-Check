from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class Specialization(models.Model):

    id_specialization = models.AutoField(primary_key= True)
    name = models.CharField(max_length=40)  

    def __str__(self):

        return self.name
    
class HealthProfessional(AbstractBaseUser, PermissionsMixin):

    username = None
    id_health_professional = models.AutoField(primary_key= True)
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    birth_date = models.DateField()
    registration_number = models.CharField(max_length=50)  
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, related_name= 'professional_specialization') #N vai deletar o medico caso a especialização seja excluida
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'cpf', 'birth_date', 'registration_number', 'specialization']

    def __str__(self):

        return self.name
    
    def set_password(self, raw_password):

        self.password = make_password(raw_password)

    def verify_password(self, raw_password):

        return check_password(raw_password, self.password)