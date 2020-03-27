from django.http import HttpResponse
from django.shortcuts import render

from .main import *

"""
Functions in `main.py`
@ covid_get_json
@ covid_national_total
@ covid_national_today
@ covid_statewise
@ covid_statewise_table
@ covid_plot_to_b64
@ covid_daily
@ covid_daily_daily
@ covid_daily_total
@ covid_daily_dailyc
@ covid_daily_dailyd
@ covid_daily_dailyr
@ covid_daily_totalc
@ covid_daily_totald
@ covid_daily_totalr
@ covid_statewise_graph
@ covid_statewise_graph_active
@ covid_statewise_graph_confirmed
@ covid_statewise_graph_recovered
@ covid_statewise_graph_deaths
"""

def index(request):
	mn = covid_get_json()
	ht = covid_statewise_table(mn)

	dtst = covid_statewise_graph_active()['state']
	dtac = covid_statewise_graph_active()['active']
	dtcf = covid_statewise_graph_confirmed()['confirmed']
	dtdt = covid_statewise_graph_deaths()['deaths']
	dtrc = covid_statewise_graph_recovered()['recovered']

	date = covid_daily_dailyc()['date']
	ddc = covid_daily_dailyc()['dailyconfirmed'][:-1]
	ddd = covid_daily_dailyd()['dailydeceased'][:-1]
	ddr = covid_daily_dailyr()['dailyrecovered'][:-1]
	dtc = covid_daily_totalc()['totalconfirmed'][:-1]
	dtd = covid_daily_totald()['totaldeceased'][:-1]
	dtr = covid_daily_totalr()['totalrecovered'][:-1]

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
