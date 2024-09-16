from django.db import models



class Specialization(models.Model):

    name = models.CharField(max_length=40)  

    def __str__(self):

        return self.name
    
class HealthProfessional(models.Model):

    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    birth_date = models.DateField()
    registration_number = models.CharField(max_length=50)  
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, related_name= 'professional_specialization') #N vai deletar o medico caso a especialização seja excluida


    def __str__(self):

        return self.name


   

