from django.contrib import admin
from .models import Category, ToDoList


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    fields = ['name']


class ToDoAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'due_date', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(ToDoList, ToDoAdmin)
