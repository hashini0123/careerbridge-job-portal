from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class RegisterAPITest(APITestCase):

    def test_register_user_success(self):
        url = reverse("register")

        data = {
            "username": "testuser",
            "email": "testuser@gmail.com",
            "password": "Test@123",
            "role": "JOB_SEEKER"
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.data["username"],
            "testuser"
        )


    def test_login_user_success(self):
        self.client.post(
            reverse("register"),
            {
                "username": "testuser",
                "email": "testuser@gmail.com",
                "password": "Test@123",
                "role": "JOB_SEEKER"
            },
            format="json"
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "testuser",
                "password": "Test@123"
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)


    def test_login_with_wrong_password(self):
        self.client.post(
            reverse("register"),
            {
                "username": "testuser",
                "email": "testuser@gmail.com",
                "password": "Test@123",
                "role": "JOB_SEEKER"
            },
            format="json"
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "testuser",
                "password": "WrongPassword"
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )


    def test_profile_without_token(self):
        response = self.client.get(
            reverse("profile")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )