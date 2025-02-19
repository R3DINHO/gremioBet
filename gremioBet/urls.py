from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apostas.urls")),  # Inclui as URLs do app 'apostas'
]
