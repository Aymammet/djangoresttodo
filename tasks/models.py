from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, validators=[MinLengthValidator(2)])
    description = models.TextField(max_length=1000, validators=[MinLengthValidator(2)], null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class status(models.TextChoices):
        SCHEDULED = 'Scheduled',
        INPROGRESS = 'In Progress',
        COMPLETED = 'Completed',
    status = models.CharField(max_length=15, choices=status.choices, default=status.SCHEDULED)
    
    class priority(models.TextChoices):
        HIGH = 'High',
        MEDIUM = 'Medium',
        LOW = 'Low',

    priority = models.CharField(max_length=7, choices=priority.choices, default=priority.MEDIUM)

    def __str__(self):
        return self.title