from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

class TaskMaster(models.Model):
    """Task master table containing task related information"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True) #Should be updated when changing the completed state
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
    project = models.ForeignKey(Project,on_delete=models.CASCADE,default=2,related_name='project')


    # """
    # Here, we are conditionally setting the completed time of the task only when completed is marked as True by
    # overriding the save method
    # Ref: https://docs.djangoproject.com/en/3.0/topics/db/models/#overriding-model-methods
    # This breaks task post method.
    # This may not be the correct way to do it. Handled in the views.py file.
    # Keeping this for learning and future reference.
    # """
    # def save(self, *args, **kwargs):
    #     if self.completed == True:
    #         self.completed_at = timezone.now()
    #     else:
    #         self.completed_at = None
    #     super(TaskMaster, self).save(*args, *kwargs)



    class Meta:
        verbose_name = 'task master'
        verbose_name_plural = 'tasks master'

    def __str__(self):
        """String representation of taskmaster"""
        return self.title

