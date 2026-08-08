from rest_framework import serializers
from .models import Job , Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source = "company.name" , read_only = True)

    class Meta:
        model = Job
        fields = "__all__"
        read_only_fields = ["company"]