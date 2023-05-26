from django.contrib import admin
from .models import Instructor, PersonalizedWorkout, Trainer


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'image', 'description']  # Campos a mostrar en la lista de registros del administrador
    list_display_links = ['name']  # Campos que serán enlaces a la página de edición
    search_fields = ['name']  # Campos por los cuales se puede realizar búsqueda
    list_filter = ['title']  # Campos por los cuales se puede filtrar la lista
    # Otros ajustes del administrador, si es necesario

@admin.register(PersonalizedWorkout)
class PersonalizedWorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class PersonalizedWorkoutInline(admin.StackedInline):
    model = Trainer.personalized_workouts.through


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['name', 'experience_years']
    inlines = [PersonalizedWorkoutInline]