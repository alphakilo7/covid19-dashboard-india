from django.http import HttpResponse
from django.shortcuts import render
from .main import covid_get_json, covid_national, covid_statewise, covid_statewise_table


def index(request):
	mn = covid_get_json()
	ht = covid_statewise_table(mn)

	return render(request, 'index.html', {
		'data_table': ht,
	})
