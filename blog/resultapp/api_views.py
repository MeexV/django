from rest_framework import routers, serializers, viewsets
from .models import Requirements, Skills
from .serializers import RequirementsSerializer, SkillsSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import ReadOnly
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication


class RequirementsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializer

class SkillsViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer