from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from healthcareProfessional.models import HealthProfessional
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'tela_inicio.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Tenta autenticar o usuário usando o modelo de usuário padrão
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            print("Usuário autenticado:", user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('/home/')
        else:
            print("Autenticação falhou")
            try:
                # Tenta obter o profissional de saúde
                health_professional = HealthProfessional.objects.get(email=email)
                # Verifica a senha do profissional de saúde
                if check_password(password, health_professional.password):
                    # Autentica e faz login do profissional de saúde
                    user = health_professional.user  # Certifique-se de que esse campo exista
                    login(request, user)
                    messages.success(request, "Login realizado com sucesso!")
                    return redirect('/home/')
                else:
                    messages.error(request, "Credenciais inválidas")
            except HealthProfessional.DoesNotExist:
                messages.error(request, "Credenciais inválidas")

    return render(request, 'Tela_Login.html')

def cadastro_usuario_view(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        birth_date = request.POST.get('birth_date')

        if not all([name, cpf, email, password, confirm_password, birth_date]):

            messages.error(request, 'Todos os campos são obrigatórios!')
            
        if password != confirm_password:

            messages.error(request, 'As senhas não coincidem!')
        
        elif Usuario.objects.filter(cpf = cpf).exists():

            messages.error(request, 'Esses CPF já está cadastrado!')
        
        elif Usuario.objects.filter(email = email).exists():

            messages.error(request, 'Esse e-mail já está cadastrado!')

        else :

            try: 

                user = Usuario(

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

