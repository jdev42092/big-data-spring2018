import pandas as pd
import requests
import io

datelist = pd.date_range('07-01-2017', periods=31, freq='D')

df = pd.DataFrame()

for date in datelist:
    url = f'https://s3.amazonaws.com/skyhook-metro-extracts/metro_extracts/boston_massachusetts_{date.date()}.csv'
    data = requests.get(url)

    df_new = pd.read_csv(io.StringIO(data.text))
    df_new['date'] = date
    df = pd.concat([df, df_new])
    # print(df.head())

df.to_csv('week-03/data/skyhook_2017-07.csv')
