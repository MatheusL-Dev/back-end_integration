#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django

def executar_script():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    django.setup()

    from backend.core.fake_dados import execute
    execute(20)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    if "runserver" in sys.argv and os.environ.get('RUN_MAIN') != 'true':
        executar_script()

    main()