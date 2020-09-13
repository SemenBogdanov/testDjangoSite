from django.views import generic
from .models import Category, ToDoList


class IndexPageView(generic.ListView):
    model = ToDoList
    template_name = 'index.html'
    queryset = ToDoList.objects.all()
