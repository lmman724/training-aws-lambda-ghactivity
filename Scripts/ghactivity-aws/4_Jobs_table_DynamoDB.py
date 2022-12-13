import boto3

dynamodb_client = boto3.client('dynamodb')

type(dynamodb_client)

dynamodb_client.list_tables()

tables = dynamodb_client.list_tables()['TableNames']

#check table name 'jobs' is existed in table 

'jobs' in tables

if 'jobs' not in tables:
    response = dynamodb_client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'job_id',
                'AttributeType': 'S'
            }
        ],
        TableName='jobs',
        KeySchema=[
            {
              'AttributeName': 'job_id',
              'KeyType': 'HASH'
            },
        ],
        BillingMode='PAY_PER_REQUEST'
    )
    print(response)


#Check info from table in dynamoDB

dynamodb_client.list_tables()
'''
{'TableNames': ['jobs'],
 'ResponseMetadata': {'RequestId': 'R4T27URR5M3UEA34NFUIR9JIEFVV4KQNSO5AEMVJF66Q9ASUAAJG',
  'HTTPStatusCode': 200,
  'HTTPHeaders': {'server': 'Server',
   'date': 'Sun, 11 Dec 2022 13:57:26 GMT',
   'content-type': 'application/x-amz-json-1.0',
   'content-length': '23',
   'connection': 'keep-alive',
   'x-amzn-requestid': 'R4T27URR5M3UEA34NFUIR9JIEFVV4KQNSO5AEMVJF66Q9ASUAAJG',
   'x-amz-crc32': '312962171'},
  'RetryAttempts': 0}}
'''

dynamodb_client.describe_table(TableName ='jobs')

'''
{'Table': {'AttributeDefinitions': [{'AttributeName': 'job_id',
    'AttributeType': 'S'}],
  'TableName': 'jobs',
  'KeySchema': [{'AttributeName': 'job_id', 'KeyType': 'HASH'}],
  'TableStatus': 'ACTIVE',
  'CreationDateTime': datetime.datetime(2022, 12, 11, 20, 54, 41, 888000, tzinfo=tzlocal()),
  'ProvisionedThroughput': {'NumberOfDecreasesToday': 0,
   'ReadCapacityUnits': 0,
   'WriteCapacityUnits': 0},
  'TableSizeBytes': 0,
  'ItemCount': 0,
  'TableArn': 'arn:aws:dynamodb:us-east-1:705598528158:table/jobs',
  'TableId': '8e95af43-97f1-4aad-9028-b7afbf5be93d',
  'BillingModeSummary': {'BillingMode': 'PAY_PER_REQUEST',
   'LastUpdateToPayPerRequestDateTime': datetime.datetime(2022, 12, 11, 20, 54, 41, 888000, tzinfo=tzlocal())}},
 'ResponseMetadata': {'RequestId': 'ITGDB16RQMLFR7F0LMBQ6L9PBNVV4KQNSO5AEMVJF66Q9ASUAAJG',
  'HTTPStatusCode': 200,
  'HTTPHeaders': {'server': 'Server',
   'date': 'Sun, 11 Dec 2022 13:56:55 GMT',
   'content-type': 'application/x-amz-json-1.0',
   'content-length': '695',
   'connection': 'keep-alive',
   'x-amzn-requestid': 'ITGDB16RQMLFR7F0LMBQ6L9PBNVV4KQNSO5AEMVJF66Q9ASUAAJG',
   'x-amz-crc32': '2708518795'},
  'RetryAttempts': 0}}
'''

dynamodb_resources = boto3.resource('dynamodb')

#type(dynamodb_resources)

job_details_table = dynamodb_resources.Table('jobs')

type(job_details_table)

job_details = {

    'job_id': 'ghactivity_ingest',
    'job_description': 'Ingest ghactivity data to s3',
    'is_active': 'Y'
}

job_details_table.put_item(
    Item = job_details
)

job_details_table.scan()

job_details_table.get_item(Key ={'job_id': 'ghactivity_ingest'})


jobs_details_2 = {
    'job_id': 'ghactivity_ingest',
    'job_description': 'Ingest ghactivity data to s3',
    'is_active': 'Y',
    'baseline_days': 3
}

job_details_table.put_item(
    Item = jobs_details_2
)

job_details_table.get_item(Key = {'job_id': 'ghactivity_ingest'})
'''
{'Item': {'job_description': 'Ingest ghactivity data to s3',
  'is_active': 'Y',
  'job_id': 'ghactivity_ingest',
  'baseline_days': Decimal('3')},
 'ResponseMetadata': {'RequestId': 'BR986NG3JACHUH63UOEU6P4VO3VV4KQNSO5AEMVJF66Q9ASUAAJG',
  'HTTPStatusCode': 200,
  'HTTPHeaders': {'server': 'Server',
   'date': 'Sun, 11 Dec 2022 14:18:44 GMT',
   'content-type': 'application/x-amz-json-1.0',
   'content-length': '148',
   'connection': 'keep-alive',
   'x-amzn-requestid': 'BR986NG3JACHUH63UOEU6P4VO3VV4KQNSO5AEMVJF66Q9ASUAAJG',
   'x-amz-crc32': '908240578'},
  'RetryAttempts': 0}}
'''