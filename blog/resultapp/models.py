from django.db import models
from usersapp.models import ParsUser

# Create your models here.

class Skills(models.Model):
    skillname = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.skillname
class Requirements(models.Model):
    quantity = models.IntegerField(null=True)
    percentage = models.FloatField(null=True)
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)

    def __str__(self):
        return self.skills.__str__()

class Vacancies(models.Model):
    vacancyname = models.CharField(max_length=32)
    vacancyarea = models.CharField(max_length=32)
    totalvacancies = models.IntegerField(null=True)
    avgsalaryFrom = models.FloatField(null=True, default=0)
    avgsalaryTo = models.FloatField(null=True, default=0)
    requirements = models.ManyToManyField(Requirements, related_name='vacancies')
    #user = models.ManyToManyField(ParsUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.vacancyname