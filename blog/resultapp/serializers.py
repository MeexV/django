from django.urls import path, include
from .models import Requirements, Skills
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class RequirementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'

class SkillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'