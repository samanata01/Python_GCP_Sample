import datetime, time
import pandas as pd
from google.cloud import storage

ticker= 'TSLA'
period1=int(time.mktime(datetime.datetime(2027,7,1,23,59).timetuple()))
period2=int(time.mktime(datetime.datetime(2027,7,31,23,59).timetuple()))
interval ='1d' # 1wk, 1m
query= f'https://query1.finance.yahoo.com/v7/finance/download/TSLA?peri'
df=pd.read_csv(query)
print(df)

client= storage.Client()
exportbuck=client.get_bucket('gcs_api_demo_01')
df.to_csv()

exportbuck.blob('tsla{0}.csv'.format(datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S'))).upload_from_string(df.to_csv(),'text/csv')