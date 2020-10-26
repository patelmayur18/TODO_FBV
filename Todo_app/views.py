from django.shortcuts import render,redirect
from . models import Todo
from . forms import TodoForm


# Create your views here.

def list_todos(request):
    todos = Todo.objects.all()
    context = {
        'todo_list':todos
    }
    return render(request,"list.html",context)

def detail_view(request,id):
    todo_detail = Todo.objects.get(id=id)
    context = {
        'todo_detail': todo_detail
    }
    return render(request,"detail.html",context)
    
def create_todo(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {
        'form':form
    }
    return render(request,"create.html",context)

def update_todo(request,id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None,instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form':form
    }
    return render(request,"update.html",context)

def delete_todo(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')

