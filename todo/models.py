from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tasks(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    task_name = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name

    class Meta:
        ordering = ['date_of_creation']
        verbose_name_plural = "All the tasks"
