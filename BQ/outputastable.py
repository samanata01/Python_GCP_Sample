import os
import time
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()

qry="""SELECT * FROM BQ_sample.Sample_table where rank<20"""

#prepare variable
proj_id='erudite-gate-405305'
dest_dataset_id='BQ_second'
dest_table_id='secondary'

#destination table ref
dataset_ref=client.dataset(dest_dataset_id,proj_id)
dest_dataset=client.get_dataset(dataset_ref)

table_ref=dataset_ref.table(dest_table_id)

#Query job config
query_job_config=bigquery.QueryJobConfig()
query_job_config.destination=table_ref

#run sql qyery
query_job=client.query(qry, location=dest_dataset.location, job_config=query_job_config)

#wait for job to complete
while query_job.state !='Done':
    print('waiting')
    time.sleep(3)
    query_job.reload()
print(f'result saved to{table_ref.dataset_id}.{table_ref.table_id}')
