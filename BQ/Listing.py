import pandas as pd
from google_apis import create_service

bq_service=create_service(
    'erudite-gate-405305-97944dafc53d.json',
    'bigquery',#service use
    'v2',#version
    ['https://www.googleapis.com/auth/bigquery']
)
#________________________Incomplete____________