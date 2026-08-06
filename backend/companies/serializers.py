from rest_framework import serializers
from .models import Company

class ComapanySerializers(serializers.ModelsSerializer):
    class Meta:
        model = Company
        field = "__all__"
        read_only_field = ["employer"]