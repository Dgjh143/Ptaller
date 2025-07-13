from django.contrib import admin
from django.urls import path
from core_admin import view  # ← corregido
from django.shortcuts import redirect

urlpatterns = [
    path('login/', view.login_view, name='login'),
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login/')),  # ← redirección al login
    path('funcionario/', view.funcionario_inicio, name='funcionario_inicio'),
    path('soporte-tecnico/', view.soporte_tecnico, name='soporte_tecnico'),
    path('soporte-sistema/', view.soporte_sistema, name='soporte_sistema'),
    path('ingeniero/', view.ingeniero_inicio, name='ingeniero_inicio'),
    path('ingeniero-jefe/', view.ingeniero_jefe_inicio, name='ingeniero_jefe_inicio'),
    path('comprobante/', view.comprobante_finalizacion, name='comprobante_finalizacion'),
]
