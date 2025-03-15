from django.shortcuts import render
import datetime
from calendar import monthrange
from datetime import date

# 🔹 New helper function that only returns context


def get_calendar_context(request):
    # Get year and month from URL parameters, or use the current date
    year = int(request.GET.get('year', datetime.datetime.today().year))
    month = int(request.GET.get('month', datetime.datetime.today().month))
    today = date.today()

    # Get total days in the selected month
    days_in_month = monthrange(year, month)[1]

    # Get month name
    month_name = datetime.date(year, month, 1).strftime("%B")

    # Generate lists of months and years
    months_list = [
        {"number": i, "name": datetime.date(2000, i, 1).strftime("%B")}
        for i in range(1, 13)
    ]
    # Year range: past 5 to next 5 years
    years_list = list(range(year - 5, year + 6))

    return {
        "year": year,
        "month": month,
        "month_name": month_name,
        "today": today,
        "days": list(range(1, days_in_month + 1)),  # Days of the month
        "months_list": months_list,
        "years_list": years_list,  # List of years for dropdown
    }

# 🔹 The view function now calls the helper function


def mycalendar(request):
    context = get_calendar_context(request)
    return render(request, "calendar.html", context)


def index(request):
    return render(request, "index.html")
