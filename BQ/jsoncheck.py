import time
import json
import os
import io
from google.cloud import bigquery
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()
dataset_ref= bigquery.DatasetReference(client.project,'BQ_second')
#file_path= 'sample_json.json'
#flatten json records
#json_data = json.load(open('sample_json.json'))
#print(json.dumps(json_data ,indent=1))
file_path= 'check_json.json'
"""def format_schema(schema):
    formatted_schema = []
    for row in schema :
            formatted_schema.append(bigquery.SchemaField(row['name'], row['code'], row['rank']))
    return formatted_schema"""
#Construct table ref
table_id='erudite-gate-405305.BQ_second.jsontobq'

#json schema representation
table_schema= {
    'name' : 'name',
    'type' : 'STRING',
    'mode' : 'REQUIRED'
},{
    'name' : 'code',
    'type' : 'STRING',
    'mode' : 'NULLABLE'
},{
    'name' : 'rank',
    'type' : 'INTEGER',
    'mode' : 'NULLABLE'
}

#Table schema
job_config=bigquery.LoadJobConfig()
#job_config.field_delimiter=','
job_config.write_disposition=bigquery.WriteDisposition.WRITE_APPEND
#job_config.schema= format_schema(table_schema)
job_config.source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON

job_config.schema=[
        bigquery.SchemaField('_name_','STRING'),
        bigquery.SchemaField('code','STRING'),
        bigquery.SchemaField('rank','INTEGER'),
    ]

#job=client.load_table_from_json(json_data,table_id,job_config=job_config)
#with open(file_path,"rb") as source_file :
json_data = json.loads(open(file_path))
print(json_data)
job=client.load_table_from_json(json_data,table_id,job_config=job_config)
print(job.result())
#job=client.load_table_from_file(source_file,table_id,job_config=job_config)
    #source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    #write_Disposition='WRITE_APPEND' #(Write_truncate,write_append,write_empty)
#upload json to bq
#with open(file_path,"rb") as source_file :
"""job=client.load_table_from_json(json_data,table_id,job_config=job_config)
    print(job.result())"""
   # print("{0}  &  {1}  &  {2}".format(job.output_rows,dataset_ref,table_id))
"""while job.state != 'DONE':
    job.reload()
    time.sleep(2) #check status every 2 sec"""




