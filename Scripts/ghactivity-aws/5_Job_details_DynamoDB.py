import os
import boto3

os.environ.setdefault('AWS_PROFILE', 'ghactivity')

dynamo_client = boto3.client('dynamodb')

#check table current in aws

dynamo_client.list_table()

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