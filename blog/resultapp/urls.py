from django.urls import path
from resultapp import views

app_name = 'resultapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('vacancies/', views.vacancies_view, name='vacancies'),
    path('result/', views.result_view, name='result'),
    path('contacts/', views.contacts_view, name='contacts'),

]
