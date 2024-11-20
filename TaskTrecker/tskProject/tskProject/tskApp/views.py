from django.shortcuts import render, redirect

# Create your views here.
from .forms import TaskForms
from .models import Task


def home_view(request):
    return render(request, 'tskApp/home.html')

def task_create_view(request):
    form = TaskForms()
    if request.method == 'POST':
        form = TaskForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request, 'tskApp/task_form.html', {'form':form})


def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'tskApp/task_list.html', {'tasks':tasks})


def task_update_view(request, id):
    task = Task.objects.get(id = id)
    form = TaskForms(instance=task)
    if request.method == 'POST':
        form = TaskForms(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request, 'tskApp/task_list.html', {'form':form})


def task_delete_view(request, id):
    task = Task.objects.get(id = id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tskApp/task_confirm_delete.html', {'task':task})