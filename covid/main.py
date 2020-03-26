import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import io
import json
import urllib
import base64
import urllib3 as ulib


def covid_get_json():
	"""Fetch CoViD-19 JSON Data from given URL"""

	URL = "https://api.covid19india.org/data.json"
	http = ulib.PoolManager()
	ncp_data = http.request('GET', URL)
	data = json.loads(ncp_data.data.decode("utf-8"))

	return data


def covid_national(data_dict):
	nat = data_dict['statewise'][0]
	print(nat)


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


def covid_statewise_graph(out='dict'):
	mf = covid_get_json()
	sf = covid_statewise(mf)
	sf = pd.DataFrame(sf)
	xf = sf.drop([0], axis=0)
	xf = xf[xf.active != '0']
	xf = xf[['state', 'active', 'confirmed', 'deaths', 'recovered']]
	if out == 'dict':
		return xf.to_dict('list')
	elif out == 'df':
		return xf


def covid_statewise_graph_active():
	sna = covid_statewise_graph('df')
<<<<<<< HEAD
	sna = sna[['state', 'active']]
	plt.bar(sna.state, sna.active)
	plt.xticks(rotation=45)

	return covid_plot_to_b64(plt)
=======
	sna = sna[['state', 'active']].to_dict('list')

	return sna
>>>>>>> d242950f7cac6f9f25ed390869d69af6254d8410


def covid_statewise_graph_confirmed():
	snc = covid_statewise_graph('df')
	snc = snc[['state', 'confirmed']].to_dict('list')

	return snc


def covid_statewise_graph_deaths():
	snd = covid_statewise_graph('df')
	snd = snd[['state', 'deaths']].to_dict('list')

	return snd


def covid_statewise_graph_recovered():
	snr = covid_statewise_graph('df')
<<<<<<< HEAD
	snr = snr[['state', 'recovered']]
=======
	snr = snr[['state', 'recovered']].to_dict('list')
>>>>>>> d242950f7cac6f9f25ed390869d69af6254d8410

	return snr


def run():
	"""Script Runner"""
	print(covid_statewise_graph_active())


if __name__ == "__main__":
	run()
