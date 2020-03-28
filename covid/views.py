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
@ covid_get_districtwise
@ covid_district_data
@ covid_get_states
@ covid_statewise_district
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

	nat_t = covid_national_total(mn)
	nat_ta = nat_t['active']
	nat_tc = nat_t['confirmed']
	nat_td = nat_t['deaths']
	nat_tr = nat_t['recovered']
	nat_d = covid_national_today(mn)
	nat_da = nat_d['active']
	nat_dc = nat_d['confirmed']
	nat_dd = nat_d['deaths']
	nat_dr = nat_d['recovered']

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
		'nta': nat_ta, 'ntc': nat_tc, 'ntd': nat_td, 'ntr': nat_tr,
		'nda': nat_da, 'ndc': nat_dc, 'ndd': nat_dd, 'ndr': nat_dr,
	})
