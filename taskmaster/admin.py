from django.contrib import admin
from taskmaster import models

"""Admin view enabled for task model"""
admin.site.register(models.TaskMaster)
