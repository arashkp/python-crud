from django.shortcuts import render
from .models import Task
from .forms import TaskForm
# from .forms import TaskForm
# Create your views here.


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/task_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'myapp/task_detail.html', {'task': task})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
