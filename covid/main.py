import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import urllib3 as ulib
import json


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


def run():
	"""Script Runner"""
	# Keys
	#	:state:
	#	:cofirmed:
	#	:deaths:
	#	:recovered:
	#	:active:

	md = covid_get_json()
	sd = covid_statewise(md)
	print(sd)
#	ht = covid_statewise_table(sd)
#	print(ht)


if __name__ == "__main__":
	run()
