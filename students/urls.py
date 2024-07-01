from django.urls import path
from .views import get_students, create_student

urlpatterns = [
    path("students/", get_students),
    path("students/create/", create_student)
]
