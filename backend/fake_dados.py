import random
from faker import Faker
from backend.core.models import Tarefa
from datetime import datetime, timedelta

fake = Faker()
def generate_random_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2025, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date

status_choices = ['Pendente', 'Em andamento', 'Concluída', 'Cancelada']
def generate_random_tasks(num_tasks=100):
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

generate_random_tasks(20)