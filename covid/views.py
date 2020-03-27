from django.http import HttpResponse
from django.shortcuts import render

from .main import *


def index(request):
	mn = covid_get_json()
	ht = covid_statewise_table(mn)

	dtst = covid_statewise_graph_active()['state']
	dtac = covid_statewise_graph_active()['active']
	dtcf = covid_statewise_graph_confirmed()['confirmed']
	dtdt = covid_statewise_graph_deaths()['deaths']
	dtrc = covid_statewise_graph_recovered()['recovered']

	date = covid_daily_dailyc()['date']
	ddc = covid_daily_dailyc()['dailyconfirmed']
	ddd = covid_daily_dailyd()['dailydeceased']
	ddr = covid_daily_dailyr()['dailyrecovered']
	dtc = covid_daily_totalc()['totalconfirmed']
	dtd = covid_daily_totald()['totaldeceased']
	dtr = covid_daily_totalr()['totalrecovered']

	return render(request, 'index.html', {
		'data_table': ht,
		'states': dtst,
		'active': dtac,
		'confirmed': dtcf,
		'deaths': dtdt,
		'recovered': dtrc,
		'date': date,
		'ddc': ddc, 'ddd': ddd, 'ddr': ddr,
		'dtc': dtc, 'dtd': dtd, 'dtr': dtr,
	})
