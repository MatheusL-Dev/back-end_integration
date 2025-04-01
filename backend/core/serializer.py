from rest_framework import serializers
from backend.core.models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarefa
        fields = '__all__'