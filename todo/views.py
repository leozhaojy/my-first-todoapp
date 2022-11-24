# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from rest_framework import viewsets
from .serializers import TodoSerializer, CategorySerializer
from .models import TodoList, Category
import datetime

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TodoView(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

def index(request): # index view
	todos = TodoList.objects.all() # query all todos with object manager
	categories = Category.objects.all() # get all categories with object manager
	if request.method == "POST": # check if request method is POST
		if "taskAdd" in request.POST: # check if request is to add a todo item
			title = request.POST["description"] # title
			date = str(request.POST["date"]) # date
			category = request.POST["category_select"] # category
			content = title + " -- " + date + " " + category # content
			Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
			Todo.save() # save todo item 
			return redirect("/") # reload page
		
		if "taskDelete" in request.POST: # check if request is to delete a todo
			checkedlist = request.POST["checkedbox"] # checked todos to be deleted
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id)) # get todo id
				todo.delete() # delete todo

	return render(request, "index.html", {"todos": todos, "categories":categories})