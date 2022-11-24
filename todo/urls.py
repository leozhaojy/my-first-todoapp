
from django.urls import path, include
#from todo import views as todo_views
from rest_framework import routers
from todo.views import *

router = routers.DefaultRouter()
router.register(r'categories', CategoryView, basename='Categories')
router.register(r'todos', TodoView, basename='Todos')

urlpatterns = [
    path('', index, name="TodoList"),
    path(r'api/', include(router.urls)),
]
