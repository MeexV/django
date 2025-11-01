from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy

from resultapp.parser import parser_vacancies
from django.views.generic import TemplateView, FormView, ListView
from .models import Vacancies, Requirements, Skills
from django.shortcuts import redirect
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class VacanciesForm(forms.Form):
    vacancy_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Введите название вакансии', 'class': 'form-control'}))
    vacancy_area = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Введите название города', 'class': 'form-control'}))

class MainView(TemplateView):
    template_name = 'resultapp/index.html'

class VacanciesView(LoginRequiredMixin, FormView):
    template_name = 'resultapp/vacancies.html'
    form_class = VacanciesForm
    def form_valid(self, form):
        vacancy_name = form.cleaned_data['vacancy_name']
        vacancy_area = form.cleaned_data['vacancy_area']

        # Запускаем парсер
        result = parser_vacancies(vacancy_name, vacancy_area)

        # Сохраняем результаты парсера в базу данных
        vacancies = Vacancies.objects.create(
            vacancyname=vacancy_name,
            vacancyarea=vacancy_area,
            totalvacancies=result['Всего вакансий'],
            avgsalaryFrom=result['Средняя зарплата до'],
            avgsalaryTo=result['Средняя зарплата от']
        )

        requirements = [x for x in result['Требования']]
        for requirement in requirements:
            skill_name = requirement.get('Навыки')
            quantity = requirement.get('Количество')
            percentage = requirement.get('Процент')

            skill, created = Skills.objects.get_or_create(skillname=skill_name)

            requirementss = Requirements.objects.create(
                quantity=quantity,
                percentage=percentage,
                skills=skill
            )
            vacancies.requirements.add(requirementss)
        vacancies.save()

        return redirect('resultapp:result')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class ResultView(LoginRequiredMixin, TemplateView):
    template_name = 'resultapp/result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancy'] = Vacancies.objects.last()
        if context['vacancy']:
            context['requirements'] = context['vacancy'].requirements.select_related('skills').all()
        else:
            context['requirements'] = []
        return context


class ContactsView(ListView):
    template_name = 'resultapp/contacts.html'
    paginate_by = 1
    context_object_name = 'context'

    def get_queryset(self):
        context = [
            ['HHParser@gmail.ru', '+7 (654) 651-51-88','г. Москва, 2-й Кожевнический переулок,11'],
            ['HHPar@gmail.ru','+7 (654) 651-51-22', 'г. Омск, Комсомольский проспект,22']
        ]
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['email'] = 'HHParser@gmail.ru'
    #     context['number'] = '+7 (654) 651-51-88'
    #     context['adres'] = 'г. Москва, 2-й Кожевнический переулок,11'
    #     return context
