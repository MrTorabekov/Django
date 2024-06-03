from django.db import models


class Task(models.Model):
    fullname = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname