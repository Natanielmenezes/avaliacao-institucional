# Avaliação Institucional

API em Django onde alunos avaliam disciplinas.

## Como rodar

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

## Rotas

- /api/alunos/
- /api/disciplinas/
- /api/avaliacoes/
- /api/avaliacoes/pendentes/
- /api/avaliacoes/resumo/

## Perguntas

### 1. Por que usamos um ambiente virtual em cada projeto?
Cada projeto pode usar versões diferentes das bibliotecas. Com o venv, elas ficam separadas e não bagunçam o Python do computador.

### 2. Por que dividimos o sistema em 3 apps em vez de um só?
Cada app cuida de um assunto. Assim fica mais organizado e dá para mexer em um sem quebrar os outros.

### 3. Para que servem makemigrations e migrate, e por que nessa ordem?
O makemigrations lê os models e cria o "plano" das mudanças. O migrate aplica esse plano no banco. Por isso a ordem é essa: primeiro cria o plano, depois aplica.

