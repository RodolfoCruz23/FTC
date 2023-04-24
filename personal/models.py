from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    certifications = models.TextField()
    experience_years = models.IntegerField()

    def __str__(self):
        return self.name


class PersonalizedWorkout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    certifications = models.TextField()
    experience_years = models.IntegerField()
    personalized_workouts = models.ManyToManyField(PersonalizedWorkout)

    def __str__(self):
        return self.name