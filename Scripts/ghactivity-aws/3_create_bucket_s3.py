import boto3

import os

s3_client = boto3.client('s3')

s3_client.list_buckets()


for bucket in s3_client.list_buckets()['Buckets']:
    print(bucket['Name'])
    continue

#create new bucket s3 in AWS

name_bucket = 'itversity-ghactivity'

s3_client.create_bucket(Bucket = name_bucket)



for bucket in s3_client.list_buckets()['Buckets']:
    print(bucket['Name'])
    continue




