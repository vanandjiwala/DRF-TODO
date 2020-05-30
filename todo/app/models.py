from django.db import models

class App(models.Model):
    task = models.CharField(max_length=250, blank=True, null=True)
    completed  = models.BooleanField(blank=False,null=False)
