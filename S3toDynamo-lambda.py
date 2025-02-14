# Lambda function to fetch .json file items from s3 bucket and write them into DynamoDB table


import json
import boto3

s3Client = boto3.client('s3')
dynamodbResource = boto3.resource('dynamodb')
bucket_name = 'sampledatadynamodb001'

def lambda_handler(event, context):

# TO GET THE OBJECT FROM THE S3 BUCKET
    s3_response = s3Client.get_object(
        Bucket=bucket_name, 
        Key='sampledata.json'
    )

# TO CONVERT THE OBJECT INTO BYTES->STR->DICT    
    s3_body_string = s3_response['Body'].read().decode('utf-8')
    s3_body_dict = json.loads(s3_body_string)
    print(s3_body_dict)
    print(type(s3_body_dict))

# TO PUT THE OBJECT INTO THE DYNAMODB TABLE
    dynamdb_table = dynamodbResource.Table('s3sampledatafile')
    dynamdb_table.put_item(Item=s3_body_dict)
    return {
        'statusCode': 200,
        'body': json.dumps('Values inserted into the table')
    }
