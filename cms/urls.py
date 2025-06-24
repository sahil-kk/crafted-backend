# backend/cms/urls.py

from django.urls import path
from .views import FacultyListCreateView

urlpatterns = [
    path('faculties/', FacultyListCreateView.as_view(), name='faculty-list-create'),
]