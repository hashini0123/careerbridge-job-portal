from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from accounts.models import User
from companies.models import Company
from jobs.models import Job, Category


class ApplicationAPITest(APITestCase):

    def setUp(self):

        # Employer create
        self.employer = User.objects.create_user(
            username="employer1",
            email="employer1@gmail.com",
            password="Test@123",
            role="EMPLOYER"
        )

        # Job seeker create
        self.job_seeker = User.objects.create_user(
            username="jobseeker1",
            email="jobseeker1@gmail.com",
            password="Test@123",
            role="JOB_SEEKER"
        )

        # Company create
        self.company = Company.objects.create(
            employer=self.employer,
            name="Tech Company",
            location="Colombo"
        )

        # Category create
        self.category = Category.objects.create(
            name="Software Development"
        )

        # Open job create
        self.job = Job.objects.create(
            company=self.company,
            category=self.category,
            title="Software Engineer Intern",
            description="Internship position",
            location="Colombo",
            salary_min="30000.00",
            salary_max="50000.00",
            status="OPEN"
        )


    # 1. Job seeker can apply
    def test_job_seeker_can_apply(self):

        self.client.force_authenticate(
            user=self.job_seeker
        )

        data = {
            "job": self.job.id,
            "status": "APPLIED"
        }

        response = self.client.post(
            reverse("application-create"),
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


    # 2. Employer cannot apply
    def test_employer_cannot_apply(self):

        self.client.force_authenticate(
            user=self.employer
        )

        data = {
            "job": self.job.id,
            "status": "APPLIED"
        }

        response = self.client.post(
            reverse("application-create"),
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )


    # 3. Cannot apply for a closed job
    def test_cannot_apply_for_closed_job(self):

        self.job.status = "CLOSED"
        self.job.save()

        self.client.force_authenticate(
            user=self.job_seeker
        )

        data = {
            "job": self.job.id,
            "status": "APPLIED"
        }

        response = self.client.post(
            reverse("application-create"),
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


    # 4. Current user can view own applications
    def test_my_applications(self):

        self.client.force_authenticate(
            user=self.job_seeker
        )

        self.client.post(
            reverse("application-create"),
            {
                "job": self.job.id,
                "status": "APPLIED"
            },
            format="json"
        )

        response = self.client.get(
            reverse("my-applications")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )