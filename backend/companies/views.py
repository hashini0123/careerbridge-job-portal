from rest_framework import generics, permissions
from .models import Company
from .serializers import CompanySerializer
from .services import create_company


class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        create_company(user=self.request.user, validated_data=serializer.validated_data)


class CompanyDetailView(generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]