# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.
class TodoListAdmin(admin.ModelAdmin):
    	list_display = ("title", "created", "due_date")

class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name",)

admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Category, CategoryAdmin)