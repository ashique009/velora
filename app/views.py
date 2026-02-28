from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        duration = request.POST.get("duration")   # 👈 change
        rules = request.POST.get("rules")

        Task.objects.create(
            title=title,
            duration=duration,   # 👈 change
            rules=rules
        )

        return redirect('home')

    return render(request, 'index.html', {'tasks': tasks})


def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('home')