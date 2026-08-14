from django.db import models
from companies.models import Company

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Job(models.Model): 
    STATUS_CHOICES = [
        ("OPEN" , "open"),
        ("CLOSED" , "closed"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="jobs",
    )

    category = models.ForeignKey(
        Category,
        on_delete= models.SET_NULL,
        null= True,
        related_name="jobs",
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary_min = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    salary_max = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="OPEN",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title