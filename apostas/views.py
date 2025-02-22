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


from django.shortcuts import redirect
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('index') 