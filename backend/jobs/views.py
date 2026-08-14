from rest_framework import generics, permissions
from .models import Job, Category
from .serializers import JobSerializer, CategorySerializer
from .services import create_job


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.filter(status="OPEN")
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        create_job(user=self.request.user, validated_data=serializer.validated_data)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]