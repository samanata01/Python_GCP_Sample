import os
import pandas as pd
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()

qry="""
SELECT _name_ FROM `erudite-gate-405305.BQ_sample.Sample_table` where rank<10
"""
query_job=client.query(qry,location='US',job_config=bigquery.QueryJobConfig(maximum_bytes_billed=50000000),
job_id_prefix='job_post',
)
print(query_job)

#retrieve records
for i in query_job.result():
    print(i._name_)
    print(i)

#retrieve records as dataframe
df=pd.DataFrame(query_job)
#df=query_job.to_dataframe()
print(df)


