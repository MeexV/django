from django.urls import path
from resultapp import views

app_name = 'resultapp'

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('vacancies/', views.VacanciesView.as_view(), name='vacancies'),
    path('result/', views.ResultView.as_view(), name='result'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),

]
