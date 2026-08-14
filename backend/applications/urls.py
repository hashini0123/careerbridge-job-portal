from django.urls import path
from .views import ApplicationCreateView, MyApplicationsView

urlpatterns = [
    path("", ApplicationCreateView.as_view(), name="application-create"),
    path("mine/", MyApplicationsView.as_view(), name="my-applications"),
]