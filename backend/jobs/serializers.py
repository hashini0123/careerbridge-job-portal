from rest_framework import serializers
from .models import Job , Category

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = "__all__"

class JobSerializers(serializers.ModelSerializer):
    company_name = serializers.CharField(source = "Company.name" , read_only = True)

    class Meta:
        model = Job
        field = "__all__"
        read_only_field = ["company"]