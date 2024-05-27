from django.core.management.base import BaseCommand
from resultapp.models import Skills, Vacancies, Requirements
from resultapp.parser import parser_vacancies
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.loading_data()
    def loading_data(self):
        vacancy_name = "python"
        vacancy_area = "Москва"
        result = parser_vacancies(vacancy_name, vacancy_area)

        vacancy = Vacancies.objects.create(vacancyname=result['Вакансия'],
                                 vacancyarea=result['Город'],
                                 totalvacancies=result['Всего вакансий'],
                                 avgsalaryFrom=result['Средняя зарплата от'],
                                 avgsalaryTo=result['Средняя зарплата до'])


        requirements = [x for x in result['Требования']]
        for requirement in requirements:
            skill, quantity, percentage = requirement.values()

            skill, created = Skills.objects.get_or_create(skillname=skill)
            req = Requirements.objects.create(quantity=quantity,
                                              percentage=percentage,
                                              skills=skill)
            vacancy.requirements.add(req)
