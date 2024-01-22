import os
import io
import requests
import time
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()

csv_url='https://filesamples.com/samples/document/csv/sample4.csv'
table_id="erudite-gate-405305.BQ_sample.webtobq"

job_config=bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading_rows = 1
job_config.autodetect=True

response=requests.get(csv_url)
if response.status_code !=200:
    print(response.reason)
else:
    content_byte=response.content
    bytes_io=io.BytesIO(content_byte)
    job=client.load_table_from_file(bytes_io,table_id,job_config=job_config)

    while job.state !='DONE':
        time.sleep(3)
        job.reload()
        print(job.state)

    job.result()

    """table= client.get_table(table_id)"""