from rest_framework import generics
from .models import Faculty
from .serializers import FacultySerializer

class FacultyListCreateView(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer