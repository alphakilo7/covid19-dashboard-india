import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import io
import json
import urllib
import base64
import urllib3 as ulib

"""
Functions' List
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

def covid_get_json():
	"""Fetch CoViD-19 JSON Data from given URL"""

	URL = "https://api.covid19india.org/data.json"
	http = ulib.PoolManager()
	ncp_data = http.request('GET', URL)
	data = json.loads(ncp_data.data.decode("utf-8"))

	return data


def covid_national_total(data_dict):
	data_dict = data_dict['statewise'][0]
	return dict((k, data_dict[k]) for k in ['active', 'confirmed', 'deaths', 'recovered'] if k in data_dict.keys())


def covid_national_today(data_dict):
	return data_dict['statewise'][0]['delta']


def covid_statewise(data_dict):
	"""Extract Indian Statewise Date from `data_dict`"""

	swise = data_dict['statewise']
	return swise


def covid_statewise_table(data_dict):
	d = covid_statewise(data_dict)
	html = """<table class="tableu">
	<tr class="tableu-head">
		<th>State</th>
		<th>Active</th>
		<th>Confirmed</th>
		<th>Deceased</th>
		<th>Recovered</th>
	</tr>\n"""
	for s in range(1, len(d)):
		html += "\t<tr>\n"
		html += """\t\t<td class="states">{st}</td>\n\t\t<td class="nums">{ac}</td>\n\t\t<td class="nums">{cf}</td>\n\t\t<td class="nums">{dt}</td>\n\t\t<td class="nums">{rc}</td>\n""".format(st=d[s]['state'],
														ac=d[s]['active'],
														cf=d[s]['confirmed'],
														dt=d[s]['deaths'],
														rc=d[s]['recovered'])
		html += "\t</tr>\n"
	html += "</table>\n"

	return html


def covid_plot_to_b64(plt_fig):
	fig = plt_fig.gcf()
	buf = io.BytesIO()
	fig.savefig(buf, format='png')
	buf.seek(0)
	ustr = base64.b64encode(buf.read())
	uri = urllib.parse.quote(ustr)

	return "data:image/png;base64," + uri


def covid_daily():
	djson = covid_get_json()
	daily = djson["cases_time_series"]

	return daily


def covid_daily_daily(out='dict'):
	ddaily = pd.DataFrame(covid_daily())
	ddaily = ddaily[['date', 'dailyconfirmed', 'dailydeceased', 'dailyrecovered']]

	if out == 'df':
		return ddaily
	elif out == 'dict':
		return ddaily.to_dict('list')


def covid_daily_total(out='dict'):
	dtotal = pd.DataFrame(covid_daily())
	dtotal = dtotal[['date', 'totalconfirmed', 'totaldeceased', 'totalrecovered']]

	if out == 'df':
		return dtotal
	elif out == 'dict':
		return dtotal.to_dict('list')


def covid_daily_dailyc():
	return covid_daily_daily('df')[['date', 'dailyconfirmed']].to_dict('list')


def covid_daily_dailyd():
        return covid_daily_daily('df')[['date', 'dailydeceased']].to_dict('list')


def covid_daily_dailyr():
        return covid_daily_daily('df')[['date', 'dailyrecovered']].to_dict('list')


def covid_daily_totalc():
	return covid_daily_total('df')[['date', 'totalconfirmed']].to_dict('list')


def covid_daily_totald():
        return covid_daily_total('df')[['date', 'totaldeceased']].to_dict('list')



def covid_daily_totalr():
        return covid_daily_total('df')[['date', 'totalrecovered']].to_dict('list')


def covid_statewise_graph(out='dict'):
	mf = covid_get_json()
	sf = covid_statewise(mf)
	sf = pd.DataFrame(sf)
	xf = sf.drop([0], axis=0)
	xf = xf[xf.active != '0']
	xf = xf[['state', 'active', 'confirmed', 'deaths', 'recovered']]
	xf['state'][:] = [x[:10] + "." if len(x) > 12 else x for x in xf['state']]
	if out == 'dict':
		return xf.to_dict('list')
	elif out == 'df':
		return xf


def covid_statewise_graph_active():
	sna = covid_statewise_graph('df')
	sna = sna[['state', 'active']].to_dict('list')
	sna['state'] = list(reversed(sna['state']))
	sna['active'] = list(reversed(sna['active']))

	return sna


def covid_statewise_graph_confirmed():
	snc = covid_statewise_graph('df')
	snc = snc[['state', 'confirmed']].to_dict('list')
	snc['state'] = list(reversed(snc['state']))
	snc['confirmed'] = list(reversed(snc['confirmed']))

	return snc


def covid_statewise_graph_deaths():
	snd = covid_statewise_graph('df')
	snd = snd[['state', 'deaths']].to_dict('list')
	snd['state'] = list(reversed(snd['state']))
	snd['deaths'] = list(reversed(snd['deaths']))

	return snd


def covid_statewise_graph_recovered():
	snr = covid_statewise_graph('df')
	snr = snr[['state', 'recovered']].to_dict('list')
	snr['state'] = list(reversed(snr['state']))
	snr['recovered'] = list(reversed(snr['recovered']))

	return snr


def covid_get_districtwise(get='states'):
	URL = "https://api.covid19india.org/state_district_wise.json"
	http = ulib.PoolManager()
	distw = http.request('GET', URL)
	data = json.loads(distw.data.decode('utf-8'))

	return data


def covid_district_data(state):
	disd = covid_get_districtwise()
	df = disd[state]['districtData']

	dist = dict()
	for ds in df.keys():
		dist[ds] = df[ds]['confirmed']

	return dist

def covid_get_states():
	return list(covid_get_districtwise().keys())

def covid_statewise_district():
	data = dict()
	for state in covid_get_states():
		data[state] = covid_district_data(state)

	return data


def run():
	"""Test Script Runner"""
	print(covid_statewise_district())


if __name__ == "__main__":
	run()
