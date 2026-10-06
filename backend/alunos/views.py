from django.http import JsonResponse
from .models import Aluno


def listar_alunos(request):
    return JsonResponse(list(Aluno.objects.values()), safe=False)
