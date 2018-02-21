import pandas as pd
import numpy as np
import matplotlib
%matplotlib inline
#new_list = []
df = pd.DataFrame()
print(df)

df['name'] = ['Bilbo','Frodo','Samwise']

df
df.assign(height=[0.5,0.4,0.6])
import os
os.chdir('week-03')
df = pd.read_csv('data/skyhook_2017-07.csv', sep=',')
df.head()
df.shape[1]
df.columns
df['cat_name'].unique()
one_fifty_eight = df[df['hour']==158]
one_fifty_eight.shape
df[(df['hour']==158) & (df['count']>50)].shape

bastille = df[df['date']=='2017-07-14']
bastille.head()
lovers_of_bastille = bastille[(bastille['count'] > bastille['count'].mean())]

lovers_of_bastille['count'].describe()

df.groupby('date')['count'].sum().plot()
df.groupby('date')['count'].describe()

jul_sec = df[df['date']=='2017-07-02']
jul_sec.groupby('hour')['count'].sum().plot()
df['date_new']=pd.to_datetime(df['date'], format='%Y-%m-%d')
# Return weekday that corresponds to our hours (which is Sunday-Saturday; .weekday() is Monday-Sunday)
# Without adding 1, weekday 0 refers to Monday and hour 0 is in Sunday, so we'll have to manually replace that
df['weekday'] = df['date_new'].apply(lambda x: x.weekday() + 1)
df['weekday'].replace(7,0, inplace=True)

# Drop values that are on the wrong day
## Hours recorded at GMT, so EST is 5 hours before
for i in range(0, 168, 24):
  j = range(0,168,1)[i - 5]
  if (j > i):
    df.drop(df[
    (df['weekday'] == (i/24)) &
    (
    ( (df['hour'] < j) & (df['hour'] > i + 18) ) |
    ( (df['hour'] > i + 18 ) & (df['hour'] < j) )
    )
    ].index, inplace = True)
  else:
    df.drop(df[
    (df['weekday'] == (i/24)) &
    (
    (df['hour'] < j) | (df['hour'] > i + 18 )
    )
    ].index, inplace = True)
