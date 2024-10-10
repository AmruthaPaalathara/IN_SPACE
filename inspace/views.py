from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Task


# Create your views here.


from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()  # Fetch all tasks to display in the table
    return render(request, 'user/home.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('project_name')
        problem = request.POST.get('problem')

        # Save the new task to the database
        if task_name and problem:
            Task.objects.create(task_name=task_name, problem=problem)
            return redirect('home')  # Redirect to the home page after saving

    return render(request, 'user/create_task.html')


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.task_name = request.POST.get('project_name')
        task.problem = request.POST.get('problem')
        task.save()
        return redirect('home')  # Redirect to the home page after updating

    return render(request, 'user/update_task.html', {'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')
