from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.project_name
