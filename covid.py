import pandas as pd
import requests
from urllib.request import urlretrieve as retrieve
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv"
retrieve (url, "covid.csv")
# r = requests.get(url)
covid19_data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv' , usecols=['Last Update','Country/Region', 'Confirmed','Deaths','Recovered'])
covid_list = covid19_data.groupby('Country/Region').max().sort_values(by = 'Confirmed', ascending=False)[1:20]
pd.set_option('display.max_column', None)
print(covid_list)