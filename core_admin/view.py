from django.shortcuts import render

def login_view(request):
    return render(request, 'Soporte/login.html')

def funcionario_inicio(request):
    return render(request, 'Soporte/funcionario_inicio.html')

def soporte_tecnico(request):
    return render(request, 'Soporte/soporte_tecnico.html')

def soporte_sistema(request):
    return render(request, 'Soporte/soporte_sistema.html')

def ingeniero_inicio(request):
    return render(request, 'Soporte/ingeniero_inicio.html')

def ingeniero_jefe_inicio(request):
    return render(request, 'Soporte/ingeniero_jefe_inicio.html')

def comprobante_finalizacion(request):
    return render(request, 'Soporte/comprobante_finalizacion.html')