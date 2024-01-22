import os
import time
import pandas as pd
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()
qry="SELECT * FROM `erudite-gate-405305.BQ_sample.Sample_table` LIMIT 2"

qry_job=client.query(qry)

while qry_job.state !='DONE':
    qry_job.reload()
    time.sleep(3)
    #print('waiting')

#qry_job.to_dataframe()

if qry_job.state =='DONE':
    df=pd.DataFrame(qry_job)
    df.to_csv('bq.csv')
    df.T.to_json('bq1.json')
else:
    print(qry_job.result())
print(df)