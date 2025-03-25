from .forms import TaskForm
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, CustomUser


# View for all tasks 
def all_tasks_view(request):
    tasks = Task.objects.all()
    users = CustomUser.objects.all()  # Fetch all users for the dropdown
    return render(request, 'tasks/all_tasks.html', {'tasks': tasks, 'users': users})


# View for tasks assigned to a specific user
def user_tasks_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    tasks = user.tasks.all()
    return render(request, 'tasks/user_tasks.html', {'tasks': tasks, 'user': user})

# View for assigning tasks via a Web Form, used to assign tasks directly via dropdown also
def assign_task_form_view(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        user_id = request.POST.get("user_id")

        task = get_object_or_404(Task, id=task_id)
        user = get_object_or_404(CustomUser, id=user_id)

        task.assigned_users.add(user)
        return redirect("all-tasks")  # Redirect after assigning

    tasks = Task.objects.all()
    users = CustomUser.objects.all()
    return render(request, "tasks/assign_task.html", {"tasks": tasks, "users": users})

# View for creating a new task by filling the details through a form
def create_task_form_view(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the task
            return redirect("all-tasks")
    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form": form})

# View for the detailed view of each task, including status, creation and completion time and assigned users etc
def task_detail_view(request, task_name):
    task = get_object_or_404(Task, name = task_name)
    return render(request, 'tasks/task_detail.html', {'task':task})