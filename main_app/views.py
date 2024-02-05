from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Exercise
from .serializer import ExerciseSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the gym-exercise-collector api home route!'}
    return Response(content)

# Define the exercise view
class ExerciseList(ListCreateAPIView):
  queryset = Exercise.objects.all()
  serializer_class = ExerciseSerializer

# Define the exercise detail view
class ExerciseDetail(RetrieveUpdateDestroyAPIView):
  queryset = Exercise.objects.all()
  serializer_class = ExerciseSerializer
  lookup_field = 'id'

