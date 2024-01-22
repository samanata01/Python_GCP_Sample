from google.cloud import bigquery
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client = bigquery.Client()

table_ref = client.dataset('BQ_second').table('gcstobq')


#table_ref = client.dataset('BQ_second').table('gcstobq')
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading_rows = 1
job_config.schema = [
    bigquery.SchemaField('name', 'STRING'),
    bigquery.SchemaField('code', 'STRING'),
    bigquery.SchemaField('rank', 'INTEGER'),
]
with open('sample_json.csv', 'rb') as source_file:
    job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
    job.result()  # Wait for the job to complete
    table = client.get_table(table_ref)
    print(table)#print table id




