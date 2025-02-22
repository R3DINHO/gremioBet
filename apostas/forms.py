import os
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .widgets import ImageRadioSelect

# Função para listar as imagens disponíveis na pasta 'fotosPerfil'
def get_profile_images():
    profile_img_path = os.path.join(settings.BASE_DIR, 'apostas', 'static', 'img', 'fotosPerfil')
    if os.path.exists(profile_img_path):  # Verifica se o diretório existe
        images = [f for f in os.listdir(profile_img_path) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        return [(img, img) for img in images]
    return []  # Retorna uma lista vazia caso o diretório não exista

class CustomUserCreationForm(UserCreationForm):
    profile_image = forms.ChoiceField(
        choices=get_profile_images(),
        label="Imagem de Perfil",
        widget=ImageRadioSelect  # Certifique-se de que este widget está correto
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


