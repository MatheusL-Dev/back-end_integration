import traceback
from datetime import datetime
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from django.db.models import Count
from django.db.models.functions import TruncMonth

from backend.core.models import Tarefa
from backend.core.serializer import TarefaSerializer


class TarefaViewSet(viewsets.ViewSet):   
    permission_classes = [AllowAny,]

    def list(self, request):
        """
            Retorna todas as tarefas criadas
        """

        try:
            tasks = Tarefa.objects.all()
            serializer = TarefaSerializer(tasks, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except Exception as err:
            print(traceback.format_exc())
            print("Ocorreu um erro", err)
            return Response(data={'message': f'ocorreu um erro na solicitação: {str(err)}'}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        """
            Retorna os detalhes de uma tarefa específica
        """

        try:
            task = Tarefa.objects.get(pk=pk)
            serializer = TarefaSerializer(task) 
            return Response(data=serializer.data, status=status.HTTP_200_OK) 

        except Tarefa.DoesNotExist:
            return Response(data={'message': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)  
        
        except Exception as err:
            print(traceback.format_exc()) 
            print("Ocorreu um erro", err)
            return Response(data={'message': f'ocorreu um erro na solicitação: {str(err)}'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """
            Cria uma nova tarefa
        """

        try:
            data = request.data
            data['data_criacao'] = datetime.now().date()
            data['data_atualizacao'] = datetime.now().date()

            serializer = TarefaSerializer(data=data) 

            if serializer.is_valid(): 
                serializer.save() 
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            print(traceback.format_exc())
            print("Ocorreu um erro", err)
            return Response(data={'message': f'ocorreu um erro na solicitação: {str(err)}'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
            Atualiza uma tarefa existente
        """

        try:
            task = Tarefa.objects.get(pk=pk)
            data = request.data
            data['data_atualizacao'] = datetime.now().date()
            serializer = TarefaSerializer(task, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        except Tarefa.DoesNotExist:
            return Response(data={'message': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as err:
            print(traceback.format_exc()) 
            print("Ocorreu um erro", err)
            return Response(data={'message': f'ocorreu um erro na solicitação: {str(err)}'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
            Deleta uma tarefa existente
        """

        try:
            task = Tarefa.objects.get(pk=pk) 
            task.delete() 
            return Response(data={'message': 'Tarefa deletada com sucesso'}, status=status.HTTP_204_NO_CONTENT) 

        except Tarefa.DoesNotExist:
            return Response(data={'message': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as err:
            print(traceback.format_exc()) 
            print("Ocorreu um erro", err)
            return Response(data={'message': f'ocorreu um erro na solicitação: {str(err)}'}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'], url_path='etl')
    def get_etl(self, request):

        try:
            status_data = Tarefa.objects.values('status') \
                .annotate(qtd=Count('id')) \
                .order_by('status')

            status_result = [{'status': item['status'], 'qtd': item['qtd']} for item in status_data]

            month_data = Tarefa.objects.annotate(month=TruncMonth('data_criacao')) \
                .values('month') \
                .annotate(qtd=Count('id')) \
                .order_by('month')

            month_result = [{'mes': item['month'].month, 'qtd': item['qtd']} for item in month_data]

            return Response(data={'status': status_result, 'mes': month_result}, status=status.HTTP_200_OK)
        
        except Exception as err:
            return Response(data={'message': f'ocorreu um erro na solicitação: {str(err)}'}, status=status.HTTP_400_BAD_REQUEST)