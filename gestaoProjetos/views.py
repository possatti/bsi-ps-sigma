from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render
from gestaoProjetos.models import Projeto

def showcase(request):
    projetos = Projeto.objects.all()
    context = {'projetos': projetos}
    return render(request, 'showcase.html', context=context)
