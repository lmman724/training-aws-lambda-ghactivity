import boto3
from datetime import datetime as dt

from datetime import timedelta as td

# import os

# os.environ.setdefault('AWS_PROFILE', 'lmman724')

dynamodb = boto3.resource('dynamodb')

job_details_table = dynamodb.Table('jobs')

job_details_table.delete_item(
    Key = {
        'job_id':'ghactivity_ingest'
    }
)


job_details = {
    'job_id': 'ghactivity_ingest',
    'job_description': 'Ingest ghactivity data to s3',
    'is_active': 'Y',
    'baseline_days': 3
}

job_details_table.put_item(Item = job_details)

#create function 

def get_job_details(job_name):
    dynamodb = boto3.resource('dynamodb')
    job_table = dynamodb.Table('jobs')
    job_details = job_table.get_item(Key = {'job_id': job_name})['Item']
    return job_details

job_details = get_job_details('ghactivity_ingest')

# job_details_table.get_item(Key = {'job_id':'ghactivity_ingest'})['Item']

'''
{'job_description': 'Ingest ghactivity data to s3',
 'is_active': 'Y',
 'job_id': 'ghactivity_ingest',
 'baseline_days': Decimal('3')}
'''


baseline_days = job_details['baseline_days']

start_time = dt.now().date() - td(days = int(baseline_days))

#file_name with start time

start_file = f"{dt.strftime(start_time,'%Y-%m-%d')}-0.json.gz"

job_details = {
    'job_id': 'ghactivity_ingest',
    'job_description': 'Ingest ghactivity data to s3',
    'is_active': 'Y',
    'baseline_days': 3,
    'job_run_bookmark_details': {
        'last_run_file_name': start_file,
    }
}

job_details_table.put_item(Item = job_details)

'''
{'job_description': 'Ingest ghactivity data to s3',
 'is_active': 'Y',
 'job_id': 'ghactivity_ingest',
 'baseline_days': Decimal('3'),
 'job_run_bookmark_details': {'last_run_file_name': '2022-12-14-0.json.gz'}}
'''

job_run_bookmark_details = get_job_details('ghactivity_ingest')['job_run_bookmark_details']

dt_part = job_run_bookmark_details['last_run_file_name'].split('.')[0]

next_file = f"{dt.strftime(dt.strptime(dt_part,'%Y-%m-%d-%H')+ td(hours= 1),'%Y-%m-%d-%H')}.json.gz"

import requests

res = requests.get(f"https://data.gharchive.org/{next_file}")

file = open(f"C:/Users/lmman/Documents/GIT/AWS/Lambda/training-aws-lambda-ghactivity/Scripts/ghactivity-aws/data/{next_file}",'wb')

file.write(res.content)

file.close()