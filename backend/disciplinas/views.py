from django.http import JsonResponse
from .models import Disciplina


def listar_disciplinas(request):
    return JsonResponse(list(Disciplina.objects.values()), safe=False)
