from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def home(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title,user=request.user)
            return redirect("todo_app:home")
    
    tasks = Task.objects.filter(user=request.user)
    return render(request, "home.html", {"tasks": tasks})


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("todo_app:login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("todo_app:home")
