from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=35, min_length=2, required=True)
    description = serializers.CharField(max_length=100, min_length=2, required=True)
    # status = serializers.CharField()

    class Meta:
        model = Task
        fields = '__all__'
