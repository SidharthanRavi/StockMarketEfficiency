import boto3
import json
from datetime import datetime

# Specify the AWS region and your SQS queue URL
access_key = 'access_key'
secret_key = 'secret_key'
region= 'region'
sqs_url ='sqs_url'

# Initialize a Boto3 SQS client
sqs = boto3.client('sqs', region_name=region,aws_access_key_id=access_key,aws_secret_access_key=secret_key)
dynamodb=boto3.client('dynamodb',region_name=region)
dynamodb_table= "Stock"

def processor(event, context):
    timestamp = str(datetime.now())
    
    # Receive messages from the queue (up to 10 messages at a time)
    response = sqs.receive_message(
        QueueUrl=sqs_url,
        AttributeNames=[
            'All'
        ],
        MaxNumberOfMessages=10,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=20
        )
    messages = response.get('Messages',[])
   
    for message in messages:
        #message = messages[0]
        message_body = message['Body']
        
        attributes = message_body.split(',')
        symbol = attributes[0].split(':')[1]
        identifier = attributes[1].split(':')[1]
        open = attributes[2].split(':')[1]
        dayHigh = attributes[3].split(':')[1]
        dayLow = attributes[4].split(':')[1]
        lastPrice = attributes[5].split(':')[1]
        previousClose = attributes[6].split(':')[1]
        change = attributes[7].split(':')[1]
        yearHigh = attributes[8].split(':')[1]
        yearLow = attributes[9].split(':')[1]
        
        dynamodb.put_item(
        TableName=dynamodb_table,
        Item={
            'Symbol': {'S': symbol},
            'Identifier': {'S': identifier},
            'Open': {'N': open},
            'DayHigh': {'N': dayHigh},
            'DayLow': {'N': dayLow},
            'LastPrice': {'N': lastPrice},
            'PreviousClose': {'N': previousClose},
            'Change': {'N': change},
            'YearHigh': {'N': yearHigh},
            'YearLow': {'N': yearLow},
            'Timestamp':{'S':timestamp}
        }
    )
        
    return {
        'statusCode': 200,  
        'body': json.dumps({
            'processed_message':len(messages)})
         
     }