from django.http import HttpResponse
from django.shortcuts import render
from .main import *


def index(request):
	mn = covid_get_json()
	ht = covid_statewise_table(mn)
	dt = covid_statewise_graph_active()
	dtst = dt['state']
	dtac = dt['active']
	print(dtst)
	print(dtac)

	return render(request, 'index.html', {
		'data_table': ht,
		'states': dtst,
		'active': dtac,
	})
