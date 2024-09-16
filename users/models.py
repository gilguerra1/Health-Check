from django.db import models

class User(models.Model):

    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 200)
    cpf = models.CharField(max_length= 11, unique= True)
    email = models.EmailField(max_length= 100, unique= True)
    password = models.CharField(max_length= 255)
    birth_date = models.DateField()

    def __str__(self):

        return self.name


