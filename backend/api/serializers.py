from rest_framework import serializers
from .models import JobPost
from rest_framework.renderers import JSONRenderer



class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'

