from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from alunos.models import Aluno
from disciplinas.models import Disciplina


class Avaliacao(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('RESPONDIDA', 'Respondida'),
    ]

    nota = models.PositiveSmallIntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    comentario = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDENTE')
    data_criacao = models.DateTimeField(auto_now_add=True)

    # A FK fica aqui porque um aluno pode fazer varias avaliacoes,
    # mas cada avaliacao pertence a um unico aluno (relacao 1:N).
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='avaliacoes')

    # A FK fica aqui porque uma disciplina recebe varias avaliacoes,
    # mas cada avaliacao e sobre uma unica disciplina (relacao 1:N).
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='avaliacoes')

    def __str__(self):
        return f"{self.aluno} -> {self.disciplina} ({self.status})"
