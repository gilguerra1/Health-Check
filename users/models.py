from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:

            raise ValueError('O email deve ser fornecido')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:

            raise ValueError('Superuser must have is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:

            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser, PermissionsMixin): #Superusuario

    username = None
    id_user = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 200)
    cpf = models.CharField(max_length= 11, unique= True)
    email = models.EmailField(max_length= 100, unique= True)
    password = models.CharField(max_length= 255)
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank= True, null= True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):

        return self.name

class Usuario(models.Model):

    username = None
    id_usuario = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 200)
    cpf = models.CharField(max_length= 11, unique= True)
    email = models.EmailField(max_length= 100, unique= True)
    password = models.CharField(max_length= 255)
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank= True, null= True)

    objects = UserManager()

    def __str__(self):

        return self.name
    
    def set_password(self, raw_password):

        self.password = make_password(raw_password)

    def verify_password(self, raw_password):

        return check_password(raw_password, self.password)

