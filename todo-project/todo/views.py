from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Task
from .forms import TaskForm


# Membuat view untuk halaamat daftar task
def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks':tasks
    }

    return render(request, 'index.html', context)

# Membuat view untuk halaman detail task
def detail_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        context = {
            'task': task
        }

    except Task.DoesNotExist:
        raise HttpResponse("Task tidak ditemukan")
    
    return render(request, 'detail.html', context)

def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = TaskForm(request.POST)
            new_task.save()
            messages.success(request, 'Sukses Menambahkan Task')
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'form.html', {'form': form})

def update_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise HttpResponse("Task tidak ditemukan")
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Mengubah Task')
            return redirect('index')
    else:
        form = TaskForm(instance=task)

    return render(request, 'form.html', {'form': form})

def delete_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
        messages.success(request, 'Sukses Menghapus Task')
        return redirect('index')
    
    except Task.DoesNotExist:
        raise HttpResponse("Task tidak ditemukan")