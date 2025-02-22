

# urls.py
from django.urls import path
from .views import index, register, user_login
from .views import logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path("registro/", register, name="registro"),
    path("login/", user_login, name="login"),
    path('logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)