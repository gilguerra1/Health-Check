from django.shortcuts import render, redirect
from .models import Specialization, HealthProfessional
from django.contrib import messages
from django.contrib.auth.hashers import make_password



def cadastro_profissional_view(request):

    roles = Specialization.objects.all()

    if request.method == "POST":

        name = request.POST.get('name')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        birth_date = request.POST.get('birth_date')
        select_role = request.POST.get('role')
        registration_number = request.POST.get('registration_number')
        
        if password != confirm_password:

            messages.error(request, 'As senhas não coincidem!')
        
        elif HealthProfessional.objects.filter(cpf = cpf).exists():

            messages.error(request, 'Esses CPF já está cadastrado!')
        
        elif HealthProfessional.objects.filter(email = email).exists():

            messages.error(request, 'Esse e-mail já está cadastrado!')

        else :
             
            try:
                select_role = Specialization.objects.get(id = select_role)
                professional = HealthProfessional(
                    
                name = name,
                cpf = cpf,
                email = email,
                password = make_password(password),
                birth_date = birth_date,
                registration_number = registration_number,
                specialization = select_role

                )

                professional.save()
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('/home/')

            except Exception as e:

                messages.error(request, f'Erro ao criar o usuário{e}')
                 
    return render(request, 'cadastro_profissional.html', {'roles':roles})