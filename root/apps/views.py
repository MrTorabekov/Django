from .models import Task

from django.views.generic import ListView, DeleteView, CreateView


class TodoView(ListView):
    template_name = 'todo.html'
    model = Task
    context_object_name = "dataset"
    success_url = "/"


class TodoCreate(CreateView):
    template_name = "todo_form.html"
    model = Task
    success_url = "/"
    fields = "__all__"


class TodoDelete(DeleteView):
    model = Task
    pk_url_kwarg = 'pk'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)