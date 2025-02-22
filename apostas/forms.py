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
        images = [f for f in os.listdir(profile_img_path) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', 'webp'))]
        return [(img, img) for img in images]
    return []  # Retorna uma lista vazia caso o diretório não exista

class CustomUserCreationForm(UserCreationForm):
    profile_image = forms.ChoiceField(
        choices=get_profile_images(),
        label="Imagem de Perfil",
        widget=ImageRadioSelect  # Certifique-se de que este widget está correto
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'seuemail@gmail.com'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ex: NeyLindo'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personalizando mensagens de erro
        self.fields['username'].error_messages = {
            'unique': 'Este nome de usuário já está em uso.',
            'max_lenght' : '',
        }

        self.fields['password1'].error_messages = {
            'required': 'A senha é obrigatória.',
            'min_length': 'A senha deve ter pelo menos 8 caracteres.',
            'password_too_common': 'Essa senha é muito comum.',
            'password_entirely_numeric': 'A senha não pode ser apenas números.',
        }

        self.fields['password2'].error_messages = {
            'required': 'Você precisa confirmar a senha.',
            'password_mismatch': 'As senhas não coincidem.',
        }
