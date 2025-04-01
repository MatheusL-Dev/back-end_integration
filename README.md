# Ativar o Projeto

## Configurando o Ambiente Virtual

### Para Linux/macOS:
```sh
python -m venv venv
source venv/bin/activate
```

### Para Windows:
```sh
python -m venv venv
venv\Scripts\activate
```

## Instalando Dependências

### Se já existir um arquivo `requirements.txt`:
```sh
pip install -r requirements.txt
```

## Executando o Servidor de Desenvolvimento
```sh
python manage.py runserver
```

## Desativando o Ambiente Virtual

### Para Linux/macOS e Windows:
```sh
deactivate
```
