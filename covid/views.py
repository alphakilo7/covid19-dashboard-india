from django.http import HttpResponse
from django.shortcuts import render
from .main import covid_get_json, covid_national, covid_statewise, covid_statewise_table, covid_statewise_graph


def index(request):
	mn = covid_get_json()
	ht = covid_statewise_table(mn)
	dt = covid_statewise_graph()
	print(dt)

	return render(request, 'index.html', {
		'data_table': ht,
		'plot_data': dt,
	})
