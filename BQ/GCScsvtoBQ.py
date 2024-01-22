import os
from google.cloud import bigquery
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()
table_ref = client.dataset('BQ_second').table('gcstobq')
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading_rows = 1
source_url=[
    "gs://my_bucket_0012/sample_json.csv"
]
job_config.schema=[
    bigquery.SchemaField("name","STRING"),
    bigquery.SchemaField("code","STRING"),
    bigquery.SchemaField("rank","INT64"),
]
load_job=client.load_table_from_uri(
    source_url,
    table_ref,
    location="US",
    job_config=job_config,
)


















"""load_job.result()
dest_table=client.get_table(table_ref)
print(dest_table)"""