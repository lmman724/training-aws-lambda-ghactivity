import os
import boto3

#os.environ.setdefault('AWS_PROFILE', 'lmman724')


dynamo_client = boto3.client('dynamodb')

#check table current in aws

dynamo_client.list_tables()

dynamo_client.delete_table(TableName = 'jon_run_details')

response = dynamo_client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'job_id',
            'AttributeType': 'S'
        },
                {
            'AttributeName': 'job_run_time',
            'AttributeType': 'N'
        }
    ],
    TableName='job_run_details',
    KeySchema=[
        {
          'AttributeName': 'job_id',
          'KeyType': 'HASH'
        },
        {
          'AttributeName': 'job_run_time',
          'KeyType': 'RANGE'
        },        
    ],
    BillingMode='PAY_PER_REQUEST'
)

response

dynamo_client.describe_table(TableName = 'job_run_details')

dynamo_resource = boto3.resource('dynamodb')

job_details_table = dynamo_resource.Table('job_run_details')

import time

import datetime

time.mktime(datetime.datetime.now().timetuple())

# Time string 
# t = "14 Sep 2019 10:50:00"
# obj2 = time.strptime(t, "%d %b %Y %H:%M:%S")

# time_sec = time.mktime(obj2)


jrd_item = {
    'job_id': 'ghactivity_ingest',
    'job_run_time': int(time.mktime(datetime.datetime.now().timetuple())),
    'job_run_bookmark_details': {
        'processed_file_name': '2022-06-03-0.json.gz'
    }
}

job_details_table.put_item(
    Item = jrd_item
)