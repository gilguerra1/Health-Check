from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Specialization(models.Model):

    id_specialization = models.AutoField(primary_key= True)
    name = models.CharField(max_length=40)  

    def __str__(self):

        return self.name
    
class HealthProfessional(models.Model):

    username = None
    id_health_professional = models.AutoField(primary_key= True)
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    birth_date = models.DateField()
    registration_number = models.CharField(max_length=50)  
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, related_name= 'professional_specialization') #N vai deletar o medico caso a especialização seja excluida
    

    def __str__(self):

        return self.name
    
    def set_password(self, raw_password):

        self.password = make_password(raw_password)

    def verify_password(self, raw_password):

        return check_password(raw_password, self.password)