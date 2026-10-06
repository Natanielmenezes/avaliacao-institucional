from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alunos/', include('alunos.urls')),
    path('api/disciplinas/', include('disciplinas.urls')),
    path('api/avaliacoes/', include('avaliacoes.urls')),
]
