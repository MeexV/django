from rest_framework import routers, serializers, viewsets
from .models import Requirements, Skills
from .serializers import RequirementsSerializer, SkillsSerializer
class RequirementsViewSet(viewsets.ModelViewSet):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializer

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer