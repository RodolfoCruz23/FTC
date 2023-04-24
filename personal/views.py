from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Instructor

class InstructorListView(ListView):
    model = Instructor
    template_name = 'personal/instructor_list.html'
    context_object_name = 'instructors'

class InstructorDetailView(DetailView):
    model = Instructor
    template_name = 'personal/instructor_detail.html'
    context_object_name = 'instructor'

def custom_workout(request):
    # logic for creating custom workout
    return render(request, 'personal/custom_workout.html')