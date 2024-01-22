import os
import time
from google.cloud import bigquery
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()

#construct table entity ref
dataset_ref= bigquery.DatasetReference(client.project,'BQ_sample')
table_ref= bigquery.TableReference(dataset_ref, 'Sample_table')
my_table=client.get_table(table_ref)

#get snapshot of table schema
org_schema=my_table.schema
#print(org_schema)

#Add col
new_schema=org_schema[:]#create copy of schema
new_schema.append(bigquery.SchemaField("saved1","BOOLEAN", mode="NULLABLE"))
new_schema.append(bigquery.SchemaField("paramlink","STRING", mode="NULLABLE"))

#assign updated schema to bq table
my_table.schema=new_schema

#make api req to add col
client.update_table(my_table,['schema'])

#dlt col
query_job=client.query("""
Alter table BQ_sample.Sample_table
Drop column IF EXISTS saved1,
drop column IF EXISTS saved2,
drop column IF EXISTS paramlink
""")
while query_job.state !='DONE':
    print('waiting for job to finish...')
    time.sleep(3)
    query_job.reload()
print(query_job.result())
