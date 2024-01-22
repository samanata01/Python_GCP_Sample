import os
from google.cloud import bigquery
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()

#ADD labels

#create table reference
dataset_ref= bigquery.DatasetReference(client.project,'BQ_sample')
table_ref= bigquery.TableReference(dataset_ref, 'Sample_table')

#label creation
labels={
    'type':'social_media',
    'category':'cloud_computing'
}
sampl_tabl=client.get_table(table_ref)
sampl_tabl.labels=labels
client.update_table(sampl_tabl,['labels'])

#add table to tablref
new_labels={
    'type':'software',
    'year': '2023'
}
table=client.get_table(table_ref)
table.labels=new_labels
client.update_table(table,['labels'])

#delete label
table=client.get_table(table_ref)
labels=table.labels
labels={k: None for k, v in labels.items()}
table.labels=labels
client.update_table(table,['labels'])

