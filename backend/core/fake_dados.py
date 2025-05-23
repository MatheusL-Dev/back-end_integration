import random
from faker import Faker
from backend.core.models import Tarefa
from datetime import date, timedelta
from django.db.utils import OperationalError

fake = Faker()
def generate_random_date():
    start_date = date(2025, 1, 1)
    end_date = date(2025, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date

status_choices = ['pendente', 'em_andamento', 'concluida', 'cancelada']
def generate_random_tasks(num_tasks=10):

    for _ in range(num_tasks):
        nome = fake.word().capitalize()
        descricao = fake.sentence()
        status = random.choice(status_choices)
        data_criacao = generate_random_date()
        tarefa = Tarefa(
            nome=nome,
            descricao=descricao,
            status=status,
            data_criacao=data_criacao,
            data_atualizacao=data_criacao
        )
        tarefa.save()
        print(f"Tarefa '{nome}' criada com status '{status}' e data de criação '{data_criacao}'.")

def execute(num_tasks=10):

    try:
        if not Tarefa.objects.all().exists():
            print("Nenhum tarefa encontrada, gerando automaticamente dados...")
            generate_random_tasks(num_tasks)

    except OperationalError:
        from django.core.management import call_command
        call_command("makemigrations", interactive=False)
        call_command("migrate", interactive=False)
        generate_random_tasks(num_tasks) 

    except Exception as err:
        print("Ocorreu um error...", err)