from django.shortcuts import render
from core.models import Comunicado, Categoria

def index(request):
    nivelPOST = request.POST.get('nivel', None)
    categoriaPOST= request.POST.get('categoria', None)
    comunicados = Comunicado.objects.order_by('-fecha_envio')
    categorias = Categoria.objects.all()

    if nivelPOST:
        comunicados = comunicados.filter(nivel=nivelPOST)
    
    if categoriaPOST:
        comunicados = comunicados.filter(categoria_id=categoriaPOST)
    
    data = {
        'comunicados': comunicados,
        'categorias': categorias
    }

    return render(request, 'core/index.html', data)

