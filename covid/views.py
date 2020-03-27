from django.http import HttpResponse
from django.shortcuts import render

from .main import *


def index(request):
	mn = covid_get_json()
	ht = covid_statewise_table(mn)
	dt = covid_statewise_graph_active()
	du = covid_statewise_graph_confirmed()
	dd = covid_statewise_graph_deaths()
	dr = covid_statewise_graph_recovered()
	dtst = dt['state']
	dtac = dt['active']
	dtcf = du['confirmed']
	dtdt = dd['deaths']
	dtrc = dr['recovered']

	return render(request, 'index.html', {
		'data_table': ht,
		'states': dtst,
		'active': dtac,
		'confirmed': dtcf,
		'deaths': dtdt,
		'recovered': dtrc,
	})
