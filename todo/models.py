from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Task(models.Model):
    # Define Status Choices
    class TaskStatus(models.TextChoices):
        TODO = 'todo', _('Todo')
        IN_PROGRESS = 'in_progress', _('In Progess')
        CLOSED = 'closed', _('Closed')

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Define Table Name
        db_table = 'task'