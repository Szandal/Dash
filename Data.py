import dash
import flask
#from flask_caching import Cache
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np


Global_D = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
Global_C = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
Global_R = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
Global_Countrys = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')

Global_Countrys.columns = map(str.lower, Global_Countrys)
Global_D.columns = map(str.lower, Global_D)
Global_C.columns = map(str.lower, Global_C)
Global_R.columns = map(str.lower, Global_R)

Global_D = Global_D.rename(columns = {'province/state' : 'state','country/region':'country'})
Global_C = Global_C.rename(columns = {'province/state' : 'state','country/region':'country'})
Global_R = Global_R.rename(columns = {'province/state' : 'state','country/region':'country'})
Global_Countrys = Global_Countrys.rename(columns = {'country_region':'country'})
