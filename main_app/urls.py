from django.urls import path

# Import the views from the views file
from .views import Home
from .views import ExerciseList, ExerciseDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('exercise/', ExerciseList.as_view(), name='exercise'),
    path('exercise/<int:id>/', ExerciseDetail.as_view(), name='exercise'),
]

