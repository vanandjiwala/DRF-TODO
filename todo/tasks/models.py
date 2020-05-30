from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=250, blank=True, null=True)
    completed  = models.BooleanField(blank=False,null=False)
    owner = models.ForeignKey('auth.User', related_name='task', on_delete=models.CASCADE)

