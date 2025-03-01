# apostas/views.py
from django.shortcuts import render
from .models import Partida

def index(request):
    partidas = Partida.objects.order_by('data')  # Busca todas as partidas no banco
    return render(request, "apostas/index.html", {"partidas": partidas})


# apostas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Removemos request.FILES
        if form.is_valid():
            user = form.save(commit=False)
            user.profile_image = form.cleaned_data['profile_image']  # Salva a escolha da imagem
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'apostas/registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Mensagem de erro
            pass
    return render(request, 'apostas/login.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            print("Formulário inválido:", form.errors)  # Log de erros do formulário
    else:
        form = CustomAuthenticationForm()
    
    print("Formulário passado para o template:", form)  # Log do formulário
    return render(request, 'apostas/login.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import EditarPerfilForm


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import EditarPerfilForm, AtualizarSenhaForm

@login_required
def editar_perfil(request):
    perfil_form = EditarPerfilForm(instance=request.user)
    senha_form = AtualizarSenhaForm(request.user)
    

    if request.method == 'POST':
        print("POST recebido!")  # Verificar se o POST está sendo capturado

        if 'perfil_submit' in request.POST:
            print("Formulário de perfil enviado!")
            perfil_form = EditarPerfilForm(request.POST, instance=request.user)
            if perfil_form.is_valid():
                perfil_form.save()
                messages.success(request, 'Perfil atualizado com sucesso!')
                return redirect('editar_perfil')
            

        elif 'senha_submit' in request.POST:
            print("Formulário de senha enviado!")  # Verificar se o formulário correto está sendo enviado
            senha_form = AtualizarSenhaForm(request.user, request.POST)
            if senha_form.is_valid():
                user = senha_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Senha atualizada com sucesso!')
                return redirect('editar_perfil')
            else:
                print("Erros do formulário de senha:", senha_form.errors)  # Verificar quais erros estão aparecendo
                messages.error(request, 'Erro ao atualizar a senha. Verifique os campos e tente novamente.')


            
        if perfil_form.is_valid():
            user = perfil_form.save(commit=False)
            if 'profile_image' in perfil_form.cleaned_data and perfil_form.cleaned_data['profile_image']:
                user.profile_image = perfil_form.cleaned_data['profile_image']
            user.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('editar_perfil')
        else:
            perfil_form = EditarPerfilForm(instance=request.user)

    return render(request, 'apostas/editarPerfil.html', {
        'perfil_form': perfil_form,
        'senha_form': senha_form,
    })



from django.shortcuts import redirect
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('index') 