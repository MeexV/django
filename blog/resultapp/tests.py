from django.test import TestCase
from mixer.backend.django import mixer
from .models import Skills, Requirements, Vacancies


class TestModels(TestCase):

    def setUp(self):
        self.skill = mixer.blend(Skills, skillname='Python')
        self.requirement = mixer.blend(Requirements, quantity=5, percentage=75.5, skills=self.skill)
        self.vacancy = mixer.blend(Vacancies,
                                   vacancyname='Developer',
                                   vacancyarea='Москва',
                                   totalvacancies=10,
                                   avgsalaryFrom=50000,
                                   avgsalaryTo=70000)
        self.vacancy.requirements.add(self.requirement)

    def test_skill_creation(self):
        self.assertEqual(str(self.skill), 'Python')

    def test_requirement_creation(self):
        self.assertEqual(str(self.requirement), 'Python')
        self.assertEqual(self.requirement.quantity, 5)
        self.assertEqual(self.requirement.percentage, 75.5)

    def test_vacancy_creation(self):
        self.assertEqual(str(self.vacancy), 'Developer')
        self.assertEqual(self.vacancy.vacancyarea, 'Москва')
        self.assertEqual(self.vacancy.totalvacancies, 10)
        self.assertEqual(self.vacancy.avgsalaryFrom, 50000)
        self.assertEqual(self.vacancy.avgsalaryTo, 70000)
        self.assertIn(self.requirement, self.vacancy.requirements.all())
