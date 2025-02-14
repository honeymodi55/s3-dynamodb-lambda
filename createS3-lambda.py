# This code has a lambda function that creates S3 bucket and uploads sampledata.json file into it

import json
import boto3

client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'sampledatadynamodb001'
    response_list_bucket = client.list_buckets(
       BucketRegion = 'us-west-2'
    )
    existing_buckets = [bucket['Name'] for bucket in response_list_bucket['Buckets']]

    if bucket_name not in existing_buckets:
        response = client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'us-west-2',
            },
        )
        print(f"Bucket {bucket_name} Created Successfully!!")
        #return {
        #    'statusCode': 200,
        #    'body': json.dumps(f"Bucket {bucket_name} created!")
        #}
    else:
        print(f"Bucket already exists!!")
        #return {
        #    'statusCode': 400,
        #    'body': json.dumps("Bucket already exists! Try a different Name")
        #}
    client.upload_file('sampledata.json', bucket_name, 'sampledata.json')
    return {
        'statusCode': 200,
        'body': json.dumps(f"File uploaded successfully to {bucket_name}!")
    }

    
    
   
