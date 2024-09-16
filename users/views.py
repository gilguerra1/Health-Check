from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password

def home_view(request):

    return render(request, 'tela_inicio.html')


def login_view(request):

    return render(request, 'login.html')

def cadastro_usuario_view(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        birth_date = request.POST.get('birth_date')

        if password != confirm_password:

            messages.error(request, 'As senhas não coincidem!')
        
        elif User.objects.filter(cpf = cpf).exists():

            messages.error(request, 'Esses CPF já está cadastrado!')
        
        elif User.objects.filter(email = email).exists():

            messages.error(request, 'Esse e-mail já está cadastrado!')

        else :

            try: 

                user = User(

                    name = name,
                    cpf = cpf,
                    email = email,
                    password = make_password(password),
                    birth_date = birth_date

                )
                
                
                user.save()
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('/home/')
        
            except Exception as e:

                messages.error(request, f'Erro ao criar usuário{e}')

    return render(request, 'cadastro_usuario.html')

