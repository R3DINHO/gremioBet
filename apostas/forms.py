import os
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .widgets import ImageRadioSelect
from django.core.exceptions import ValidationError
import re

def get_profile_images():
    profile_img_path = os.path.join(settings.BASE_DIR, 'apostas', 'static', 'img', 'fotosPerfil')
    if os.path.exists(profile_img_path):  
        images = [f for f in os.listdir(profile_img_path) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', 'webp'))]
        return [(img, img) for img in images]
    return [] 

class CustomUserCreationForm(UserCreationForm):
    profile_image = forms.ChoiceField(
        choices=get_profile_images(),
        label="Imagem de Perfil",
        widget=ImageRadioSelect  
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

        self.fields['username'].error_messages = {
            'unique': 'Este nome de usuário já está em uso.',
            'max_length': 'O nome de usuário deve ter no máximo 20 caracteres.',
            'min_length': 'O nome de usuário deve ter pelo menos 4 caracteres.',
        }

        self.fields['password1'].error_messages = {
            'min_length': 'A senha deve ter pelo menos 8 caracteres.',
            'password_too_common': 'Essa senha é muito comum.',
            'password_entirely_numeric': 'A senha não pode ser apenas números.',
        }

        self.fields['password2'].error_messages = {
            'required': 'Você precisa confirmar a senha.',
            'password_mismatch': 'As senhas não coincidem.',
        }
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username and (len(username) < 4 or len(username) > 20):
            raise ValidationError("O nome de usuário deve ter entre 4 e 20 caracteres.")
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if username and len(username) < 4:
            self.add_error("username", "O nome de usuário deve ter pelo menos 4 caracteres.")
        return cleaned_data
    
    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if password:
            if len(password) < 8:
                raise ValidationError("A senha deve ter pelo menos 8 caracteres.")
            if not re.search(r"[A-Za-z]", password):
                raise ValidationError("A senha deve conter pelo menos uma letra.")
            if not re.search(r"\d", password):
                raise ValidationError("A senha deve conter pelo menos um número.")
        return password

from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

    error_messages = {
        'invalid_login': "Nome de usuário ou senha incorretos. Verifique e tente novamente.",
        'inactive': "Esta conta está inativa.",
    }

from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):
    password = None  

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_image']


from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class EditarPerfilForm(UserChangeForm):
    password = None  

    profile_image = forms.ChoiceField(
        choices=get_profile_images(),  
        label="Imagem de Perfil",
        widget=ImageRadioSelect, 
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['username'].error_messages = {
            'max_length': 'O nome de usuário deve ter no máximo 20 caracteres.',
            'min_lenght': 'O nome de usuário deve ter no mínimo 4 caracteres.',
            'unique': 'Este nome de usuário já está em uso.',
        }
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username and (len(username) < 4 or len(username) > 20):
            raise ValidationError("O nome de usuário deve ter entre 4 e 20 caracteres.")
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if username and len(username) < 4:
            self.add_error("username", "O nome de usuário deve ter pelo menos 4 caracteres.")
        return cleaned_data
    

from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
import re

class AtualizarSenhaForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['old_password'].error_messages = {
            'required': 'A senha atual é obrigatória.',
            'password_incorrect': 'Senha incorreta. Tente novamente.',
        }

        self.fields['new_password1'].error_messages = {
            'required': 'A nova senha é obrigatória.',
            'min_length': 'A nova senha deve ter pelo menos 8 caracteres.',
            'password_too_common': 'Essa senha é muito comum.',
            'password_entirely_numeric': 'A senha não pode ser apenas números.',
        }

    def clean_new_password2(self):
        senha1 = self.cleaned_data.get("new_password1")
        senha2 = self.cleaned_data.get("new_password2")

        if senha1 and senha2:
            if senha1 != senha2:
                raise ValidationError("As senhas não coincidem.")
            
            return senha2
        
    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        

        if not self.user.check_password(old_password):
            raise ValidationError("Senha incorreta. Tente novamente.")
        
        return old_password
       

