from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import TaskForm
# Create your views here.


def index(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            print('form validated')
            form.save()
        else:
            print('cant validate')
        return redirect('tasks/')

    tasks = Task.objects.all()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/tasks_list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/tasks')

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/tasks')

    context = {'task': task}
    return render(request, 'tasks/delete.html', context)

