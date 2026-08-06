from rest_framework import serializers
from .models import Application

class ApplicationSerializers(serializers.ModelSerializer):
    job_title = serializers.CharField(source = "job_title" , read_only = "True")

    class Meta:
        model = Application
        field = "__all__"
        read_only_field = ["job_seeker"]
         