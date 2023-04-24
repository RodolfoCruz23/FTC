from django.contrib import admin
from .models import Instructor, PersonalizedWorkout, Trainer


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'experience_years']


@admin.register(PersonalizedWorkout)
class PersonalizedWorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class PersonalizedWorkoutInline(admin.StackedInline):
    model = Trainer.personalized_workouts.through


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['name', 'experience_years']
    inlines = [PersonalizedWorkoutInline]