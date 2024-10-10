from django.db import models

# Create your models here.


# Define the Task model
class Task(models.Model):
    task_name = models.CharField(max_length=200)
    problem = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name

