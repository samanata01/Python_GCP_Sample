import os
import time,datetime
from google.cloud import bigquery
import pandas as pd
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()

sql_query ="""
SELECT _name_ FROM `erudite-gate-405305.BQ_sample.Sample_table` whererank<20 
"""
 # _name_ like %g% AND  
# Example 1: Query a scalar value
query_parameters = [
#bigquery.ScalarqueryParameter("_name_", "STRING", "%la%"),
bigquery.ScalarQueryParameter("rank", "INT64", 20),
]
job_config = bigquery.QueryJobConfig(
query_parameters=query_parameters
)
qry_job=client.query(sql_query,job_config=job_config)


#date range
sql_query ="""
SELECT _name_,created_utc FROM `erudite-gate-405305.BQ_sample.Sample_table` where createdutc= @created
"""
query_parameters=[
    bigquery.ScalarQueryParameter("created", "DATETIME",datetime.datetime(2023,12,18)),
]
job_config=bigquery.QueryJobConfig(
    query_parameters=query_parameters
)
qry_job=client.query(sql_query,job_config=job_config)

# Example 3: Positional parameters
sql_query ="""
SELECT _name_,created_utc FROM `erudite-gate-405305.BQ_sample.Sample_table` where rank <= ?"""
query_parameters=[
    bigquery.ScalarQueryParameter("None","INT64",20)
]
job_config=bigquery.QueryJobConfig(
    query_parameters=query_parameters
)
qry_job=client.query(sql_query,job_config=job_config)
df=pd.DataFrame(qry_job)
print(df)