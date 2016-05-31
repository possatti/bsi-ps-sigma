from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render
from gestaoProjetos.models import Projeto

def showcase(request):
    projetos = Projeto.objects.all()
    context = {'projetos': projetos}
    return render(request, 'showcase.html', context=context)

def detalhes_projeto(request, projeto_id):
    print(type(projeto_id))
    projeto = Projeto.objects.get(id=int(projeto_id))
    context = {'projeto': projeto}
    return render(request, 'detalhes_projeto.html', context=context)
