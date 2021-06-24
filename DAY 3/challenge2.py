# import requests
# import csv

# response = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')
# print(response)

# csv_file = csv.DictReader(response)

# for row in csv_file:
#     print(dict(row))

import pandas as pd

covid_data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv', usecols = ['Deaths', 'Confirmed', 'Recovered', 'Country/Region'])
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths']
# print(covid_data)

filtered_data = covid_data.groupby(['Country/Region'])['Deaths', 'Recovered', 'Active'].sum().reset_index()
filtered_data =filtered_data.sort_values(by='Deaths')
filtered_data = filtered_data[filtered_data['Deaths']>200]
print(filtered_data)