import os
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()

qry="""SELECT * FROM `erudite-gate-405305.BQ_sample.Sample_table` LIMIT 3"""
job_config=bigquery.QueryJobConfig(dry_run=True,use_query_cache=False)
query_job=client.query(qry,job_config=job_config)
print(query_job.total_bytes_processed)
