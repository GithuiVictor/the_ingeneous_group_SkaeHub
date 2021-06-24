import pandas as pd

dataset_path   = pd.read_csv ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv")
dataset_path['Active'] = dataset_path['Confirmed'] - dataset_path['Deaths'] - dataset_path['Recovered']
full_grouped = dataset_path.groupby([ 'Country/Region'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
print(full_grouped)