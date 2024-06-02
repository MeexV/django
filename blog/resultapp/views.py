from django.shortcuts import render
from django import forms
# Create your views here.


class VacanciesForm(forms.Form):
    vacancy_name = forms.CharField(label='Название вакансии')
    vacancy_area = forms.CharField(label='Город')

def main_view(request):
    return render(request, 'resultapp/index.html')

def vacancies_view(request):
    if request.method == 'POST':
        form = VacanciesForm(request.POST)
        if form.is_valid():
            vacancy_name = form.cleaned_data['vacancy_name']
            vacancy_area = form.cleaned_data['vacancy_area']
            pass
        else:
            return render(request, 'resultapp/vacancies.html', context={'form': form})
    else:
        form = VacanciesForm()
        return render(request, 'resultapp/vacancies.html', context={'form': form})

def result_view(request):
    return render(request, 'resultapp/result.html')

def contacts_view(request):
    context = {'email': 'HHParser@gmail.ru',
               'number': '+7 (654) 651-51-88',
               'adres': 'г. Москва, 2-й Кожевнический переулок, 11'}
    return render(request, 'resultapp/contacts.html', context={'context': context})
