from rest_framework.exceptions import PermissionDenied, ValidationError
from .models import Application

def create_application(user, validated_data):
    if user.role != "JOB_SEEKER":
        raise PermissionDenied("Only job seekers can apply for jobs.")

    job = validated_data["job"]
    if job.status != "OPEN":
        raise ValidationError("Application cannot be submitted for a closed job.")

    if Application.objects.filter(
        job_seeker = user,
        job = job,
    ).exists():
        raise ValidationError("You have already applied for this job.")