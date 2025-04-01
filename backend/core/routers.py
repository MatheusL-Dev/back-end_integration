from rest_framework.routers import SimpleRouter
from backend.core.views import TarefaViewSet

routes = SimpleRouter()

routes.register(r'task', TarefaViewSet, basename='task')

urlpatterns = [
    *routes.urls
]