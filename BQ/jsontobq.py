"""import time
import json
import os
from google.cloud import bigquery
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()
dataset_ref= bigquery.DatasetReference(client.project,'BQ_second')
#file_path= 'sample_json.json'
#flatten json records
json_data = json.load(open('sample_json.json'))

file_path= 'upload.json'
with open(file_path,'w')as _f:
     _f.write('\n'.join(json.dumps(row)for row in json_data))

#Construct table ref
table_id='erudite-gate-405305.BQ_second.jsontobq'

#Table schema
job_config=bigquery.LoadJobConfig(
    #autodetact=True,
    job_config.source_format='json'
    job_config.write_Disposition = bigquery.WriteDisposition.WRITE_APPEND
    jo
    job_config.schema=[
        bigquery.SchemaField("_name_","STRING"),
        bigquery.SchemaField("code","STRING"),
        bigquery.SchemaField("rank","STRING"),
    ],
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    #
)

#upload json to bq
with open(file_path,"rb") as source_file :
    job=client.load_table_from_file(source_file,table_id,job_config=job_config)
   # print(job.result())
    print("Loaded values".format(job.output_rows,dataset_ref,table_id))
while job.state != 'DONE':
    job.reload()
    time.sleep(2)""" 
    #check status every 2 sec
    


from google.cloud import bigquery
import os
import json
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()

file_path='upload.json'
"""with open(file_path,'w')as _f:
     _f.write('\n'.join(json.dumps(row)for row in json_data))"""
table_ref = client.dataset('BQ_second').table('jsontobq')


#table_ref = client.dataset('BQ_second').table('gcstobq')
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON.removeprefix("[").removesuffix("]")
#job_config.skip_leading_rows = 1
job_config.autodetect=True
"""job_config.schema = [
    bigquery.SchemaField('name', 'STRING'),
    bigquery.SchemaField('code', 'STRING'),
    bigquery.SchemaField('rank', 'INTEGER'),
]"""
with open(file_path, 'rb') as source_file:
    print(type(source_file))
    job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
    """job.result()  # Wait for the job to complete
    table = client.get_table(table_ref)
    print(table)#print table id"""