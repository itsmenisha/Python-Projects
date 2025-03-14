from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import localdate
from datetime import timedelta
from mycalendar.views import get_calendar_context
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse


def task_list(request):
    context = get_calendar_context(request)

    today = localdate()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)

    tasks_today = Task.objects.filter(due_date=today)
    tasks_yesterday = Task.objects.filter(due_date=yesterday)
    tasks_tomorrow = Task.objects.filter(due_date=tomorrow)

    # Get all task dates in the current month
    task_dates = list(Task.objects.values_list("due_date", flat=True))

    if request.method == "POST":
        if "create_task" in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("index")

        elif "update_task" in request.POST:
            task_id = request.POST.get("task_id")
            task = get_object_or_404(Task, id=task_id)
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("index")

        elif "delete_task" in request.POST:
            task_id = request.POST.get("task_id")
            task = get_object_or_404(Task, id=task_id)
            task.delete()
            return redirect("index")

    context.update({
        "tasks_today": tasks_today,
        "tasks_yesterday": tasks_yesterday,
        "tasks_tomorrow": tasks_tomorrow,
        "form": TaskForm(),
        "task_dates": task_dates,
    })

    return render(request, "index.html", context)


def calendar(request):
    return render(request, "calendar.html")


def get_tasks_for_day(request, date):
    # Parse the date string from the URL (e.g., "2025-03-15")
    tasks = Task.objects.filter(due_date=date)
    task_list = [{"title": task.title, "description": task.description,
                  "due_date": task.due_date} for task in tasks]

    # Return the tasks as a JSON response
    return JsonResponse({"tasks": task_list})
