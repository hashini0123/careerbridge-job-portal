from rest_framework.exceptions import PermissionDenied, ValidationError
from .models import Job 
from companies.models import Company

def create_job(user, validated_data):
    if user.role != "EMPLOYER":
        raise PermissionDenied("Only employers can create jobs.")

    try:
        company = user.company
    except Company.DoesNotExist():
        raise ValidationError("Create a company profile before posting a job.")

    salary_min = validated_data.get("salary_min")
    salary_max = validated_data.get("salary_max")

    if (
        salary_min is not None
        and salary_max is not None
        and salary_min > salary_max
    ):
        raise ValidationError("Minimum salary cannot be greater than maximum salary.")

    job = Job.objects.create(
        company = company,
        ** validated_data,
    )

    return job