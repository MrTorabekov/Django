from django.urls import path
from .views import TodoView, TodoDelete, TodoCreate

urlpatterns = [
    path('', TodoView.as_view(), name="view"),
    path('delete/<int:pk>', TodoDelete.as_view(), name="delete"),
    path('create', TodoCreate.as_view(), name="create"),
]