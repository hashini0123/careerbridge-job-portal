from rest_framework.exceptions import PermissionDenied , ValidationError
from .models import Company

def create_function(user, validated_data):
    if user.role != "EMPLOYER":
        raise PermissionDenied("Only employer users can create a company.")

    if Company.objects.filter(employer= user).exists():
        raise ValidationError("This employer already has a error.")

    company = Company.objects.create(
        empolyer = user,
        **validated_data,
    )

    return company
    