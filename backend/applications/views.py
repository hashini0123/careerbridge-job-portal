from rest_framework import generics, permissions
from .models import Application
from .serializers import ApplicationSerializer
from .services import create_application


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        create_application(user=self.request.user, validated_data=serializer.validated_data)


class MyApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(job_seeker=self.request.user)