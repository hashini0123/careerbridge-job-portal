from accounts.models import User
from django.db import models

class Company(models.Model):
    employer = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="company",
    ) 

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
