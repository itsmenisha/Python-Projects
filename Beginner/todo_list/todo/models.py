from django.db import models
import datetime  # Import datetime module


class Task(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, null=True, default="")
    due_date = models.DateField(
        null=False, blank=False, default=datetime.date.today)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
