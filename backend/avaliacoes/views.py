from django.http import JsonResponse
from django.db.models import Avg, Count
from .models import Avaliacao


def listar_avaliacoes(request):
    return JsonResponse(list(Avaliacao.objects.values()), safe=False)


def listar_pendentes(request):
    dados = Avaliacao.objects.filter(status='PENDENTE').values()
    return JsonResponse(list(dados), safe=False)


# Desafio 1: media e total de avaliacoes RESPONDIDAS por disciplina
def resumo(request):
    dados = (Avaliacao.objects.filter(status='RESPONDIDA')
             .values('disciplina__nome')
             .annotate(media=Avg('nota'), total=Count('id')))
    return JsonResponse(list(dados), safe=False)
