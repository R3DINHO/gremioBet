from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Partida, CustomUser

# Registrar o modelo Partida
admin.site.register(Partida)

# Personalizar a interface de administração para CustomUser
class CustomUserAdmin(UserAdmin):
    # Campos exibidos na lista de usuários
    list_display = ('username', 'email', 'gremio_coins', 'imagem_perfil')

    # Campos exibidos no formulário de edição de usuário
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('imagem_perfil', 'gremio_coins')}),  # Exibir o campo imagem_perfil
    )

    # Campos exibidos no formulário de criação de usuário
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('imagem_perfil', 'gremio_coins')}),  # Exibir o campo imagem_perfil
    )

    # Método para exibir a imagem no painel de administração
    def imagem_perfil(self, obj):
        if obj.imagem_perfil:
            return f'<img src="{obj.get_imagem_perfil_url()}" width="50" height="50" />'
        return 'Sem imagem'

    imagem_perfil.allow_tags = True
    imagem_perfil.short_description = 'Imagem de Perfil'

# Registrar o modelo CustomUser com a classe CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
