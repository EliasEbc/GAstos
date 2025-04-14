from django.shortcuts import render, redirect
from .models import Gasto
from collections import defaultdict
import json
from django.utils import timezone

def dashboard(request):
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            gasto_id = request.POST.get('eliminar')
            Gasto.objects.filter(id=gasto_id).delete()
        else:
            nombre = request.POST.get('nombre')
            monto = request.POST.get('monto')
            Gasto.objects.create(nombre=nombre, monto=monto, categoria='General', fecha=timezone.now().date())
        return redirect('dashboard')

    gastos = Gasto.objects.order_by('-fecha', '-id')
    por_categoria = defaultdict(float)
    for g in gastos:
        por_categoria[g.categoria] += float(g.monto)

    labels = list(por_categoria.keys())
    datos = list(por_categoria.values())

    return render(request, 'dashboard.html', {
        'gastos': gastos,
        'labels': json.dumps(labels),
        'datos': json.dumps(datos)
    })
