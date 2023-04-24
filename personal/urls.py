from django.urls import path
from .views import InstructorListView, InstructorDetailView, custom_workout

app_name = 'personal'

urlpatterns = [
    path('instructors/', InstructorListView.as_view(), name='instructor_list'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor_detail'),
    path('custom-workout/', custom_workout, name='custom_workout'),
]