from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import localdate
from datetime import datetime, timedelta
from mycalendar.views import get_calendar_context
from .models import Task
from .forms import TaskForm


def todo(request):
    """Render a page to ask for the user's name if not already provided."""
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            request.session["name"] = name  # Save the name in session
            return redirect("index")
    return render(request, "todo_list.html")  # Template to collect name


def task_list(request, name=None):
    # Check if the name is stored in the session and is not empty.
    user_name = request.session.get("name", "").strip()
    if not user_name:
        return redirect("name")

    context = get_calendar_context(request)
    today = localdate()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)

    # Get selected date from query parameters (default to today)
    date_str = request.GET.get("date", today.strftime("%Y-%m-%d"))
    try:
        selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        selected_date = today

    # Fetch tasks for the selected date
    tasks = Task.objects.filter(due_date=selected_date)
    # Get all task due dates (for calendar highlighting)
    task_dates = list(Task.objects.values_list("due_date", flat=True))

    if request.method == "POST":
        # Create new task
        if "create_task" in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(request.path + f"?date={selected_date}")
        # Update existing task
        elif "update_task" in request.POST:
            task_id = request.POST.get("task_id")
            task = get_object_or_404(Task, id=task_id)
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect(request.path + f"?date={selected_date}")
        # Delete task
        elif "delete_task" in request.POST:
            task_id = request.POST.get("task_id")
            task = get_object_or_404(Task, id=task_id)
            task.delete()
            return redirect(request.path + f"?date={selected_date}")

    context.update({
        "tasks": tasks,
        "selected_date": selected_date,
        "form": TaskForm(),
        "task_dates": task_dates,
        "today": today,
        "yesterday": yesterday,
        "tomorrow": tomorrow,
        "name": user_name,
    })

    return render(request, "index.html", context)


def calander(request):
    return render(request, "calendar.html")


def clear_name(request):
    if "name" in request.session:
        del request.session["name"]
    return redirect("name")
