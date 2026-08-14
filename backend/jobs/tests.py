from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from accounts.models import User
from companies.models import Company
from jobs.models import Category


class JobAPITest(APITestCase):

    def setUp(self):
        self.employer = User.objects.create_user(
            username="employer1",
            email="employer1@gmail.com",
            password="Test@123",
            role="EMPLOYER"
        )

        self.job_seeker = User.objects.create_user(
            username="jobseeker1",
            email="jobseeker1@gmail.com",
            password="Test@123",
            role="JOB_SEEKER"
        )

        self.company = Company.objects.create(
            employer=self.employer,
            name="Tech Company",
            location="Colombo"
        )

        self.category = Category.objects.create(
            name="Software Development"
        )


    def test_employer_can_create_job(self):
        self.client.force_authenticate(user=self.employer)

        data = {
            "title": "Software Engineer Intern",
            "description": "Internship position",
            "location": "Colombo",
            "salary_min": "30000.00",
            "salary_max": "50000.00",
            "status": "OPEN",
            "category": self.category.id
        }

        response = self.client.post(
            reverse("job-list-create"),
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


    def test_job_seeker_cannot_create_job(self):
        self.client.force_authenticate(user=self.job_seeker)

        data = {
            "title": "Software Engineer Intern",
            "description": "Internship position",
            "location": "Colombo",
            "salary_min": "30000.00",
            "salary_max": "50000.00",
            "status": "OPEN",
            "category": self.category.id
        }

        response = self.client.post(
            reverse("job-list-create"),
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )


    def test_salary_validation(self):
        self.client.force_authenticate(user=self.employer)

        data = {
            "title": "Software Engineer Intern",
            "description": "Internship position",
            "location": "Colombo",
            "salary_min": "80000.00",
            "salary_max": "40000.00",
            "status": "OPEN",
            "category": self.category.id
        }

        response = self.client.post(
            reverse("job-list-create"),
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )