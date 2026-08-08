from django.db import models
from accounts.models import User
from jobs.models import Job

class Application(models.Model):
    STATUS_CHOICES = [
        ("APPLIED" , "applied"),
        ("REVIEWED" , "reviewed"),
        ("REJECTED" , "rejected"),
        ("ACCEPTED" , "accepted"),
    ]

    job_seeker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="application",
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="application",
    )

    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="APPLIED")
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("job_seeker" , "job")

    def __str__(self):
        return f"{self.job_seeker.username} -> {self.job.title} "








