from google.cloud import bigquery
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='erudite-gate-405305-97944dafc53d.json'
client=bigquery.Client()

view_id="erudite-gate-405305.BQ_second.sample_view"

view= bigquery.Table(view_id)

view.view_query=f"select * from `erudite-gate-405305.BQ_sample.sample_table` where rank<15"

job=client.create_table(view)












"""
BQ can export 1 million events per day for batch export
if we want to export large amount of data from BQ

EXPORT DATA OPTIONS(
    uri=``
    format='CSV',
    overwrite=true,
    header=true,
    field_delimeter=','
    )AS

    select * from `` TABLESAMPLE system (10 percent)
"""