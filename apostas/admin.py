from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Partida


class CustomUserAdmin(UserAdmin):
    # Campos exibidos na lista de usuários
    list_display = ('username', 'email', 'gremio_coins', 'profile_image_display')

    # Campos exibidos no formulário de edição de usuário
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_image', 'gremio_coins')}),  # Exibir o campo profile_image
    )

    # Campos exibidos no formulário de criação de usuário
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('profile_image', 'gremio_coins')}),  # Exibir o campo profile_image
    )

    # Método para exibir a imagem no painel de administração
    def profile_image_display(self, obj):
        if obj.profile_image:
            return f'<img src="{obj.get_imagem_perfil_url()}" />'
        return 'Sem imagem'

    profile_image_display.allow_tags = True
    profile_image_display.short_description = 'Imagem de Perfil'

# Registrar o modelo CustomUser com a classe CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from .models import Partida

admin.site.register(Partida)