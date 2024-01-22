import os
from google.cloud import bigquery
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()
qry="""
SELECT _name_ FROM `erudite-gate-405305.BQ_sample.Sample_table` where rank<10
"""
qry_job=client.query(qry)
for i in qry_job.result():
    print(i)
print(qry_job)

"""json_data=json.load(open('./faculty.json'))

data_file_path='json_upload.json'
with open(data_file_path,'w')as _f:
    _f.write('\n'.join(json.dumps(row)for row in json_data))


client=bigquery.Client()

table_id='erudite-gate-405305.BQ_sample.jsontobq'


job_config=bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id","INT64"),
        bigquery.SchemaField("FirstName","STRING"),
        bigquery.SchemaField("LastName","STRING"),
        bigquery.SchemaField("Email","STRING"),
        bigquery.SchemaField("Mobile","NUMERIC"),
        bigquery.SchemaField("Education","STRING"),
        bigquery.SchemaField("Address","STRING"),
        bigquery.SchemaField("Pincode","NUMERIC"),
        bigquery.SchemaField("Salary","NUMERIC"),
        bigquery.SchemaField("Designation","STRING"),
    ],
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    write_Disposition='WRITE_APPEND' #(Write_truncate,write_append,write_empty)
)

#upload json to bq
with open(data_file_path,"rb")as source_file:
    job=client.load_table_from_file(source_file,table_id,job_config=job_config)

while job.create != 'DONE':
    job.reload()
    time.sleep(2) #check status every 2 sec

    print(job.result())"""


