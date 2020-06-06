from rest_framework import serializers
from taskmaster import models
from projects.models import Project


class TaskMasterSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.TaskMaster
        fields = ['id','title','description','completed','created_at','completed_at','owner','project']
        """completed_at is marked read only so it can be altered at updated time by system."""
        extra_kwargs = {
            'completed_at': {
                'read_only': True
            },
            'id': {
                'read_only': True
            },
            'owner': {
                'read_only': True
            }
        }


