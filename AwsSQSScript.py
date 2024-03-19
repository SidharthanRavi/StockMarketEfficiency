import boto3
import json
import requests

access_key = 'access_key'
secret_key = 'secret_key'
region= 'region'
sqs_url ='sqs_url'
api_url = 'api_url'


sqs = boto3.client('sqs',region_name=region,aws_access_key_id=access_key,aws_secret_access_key=secret_key)

response = requests.get(api_url)
data = response.text

data = json.loads(data)
#print(data)
#for _ in range(10):
    
for element in data.get("body", []):
    stock_symbol = element['symbol']
    stock_identifier = element['identifier']
    stock_open_price = element['open']
    stock_dayhigh_price = element['dayHigh']
    stock_daylow_price = element['dayLow']
    stock_last_price = element['lastPrice']
    stock_prev_close_price = element['previousClose']
    stock_change_price = element['change']
    stock_yearhigh_price = element['yearHigh']
    stock_yearlow_price = element['yearLow']
        
    print("Symbol:", stock_symbol)
    print("Identifier:", stock_identifier)
    print("Open Price:", stock_open_price)
    print("DayHigh Price:", stock_dayhigh_price)
    print("DayLow Price:", stock_daylow_price)
    print("Last Price:", stock_last_price)
    print("PreviousClose Price:", stock_prev_close_price)
    print("Change Price:", stock_change_price)
    print("YearHigh Price:", stock_yearhigh_price)
    print("YearLow Price:", stock_yearlow_price)

    sqs.send_message(QueueUrl=sqs_url,MessageBody=f"symbol:{stock_symbol},identifier:{stock_identifier},open:{stock_open_price},dayHigh:{stock_dayhigh_price},dayLow:{stock_daylow_price},lastPrice:{stock_last_price}, previousClose:{stock_prev_close_price},change:{stock_change_price},yearHigh:{stock_yearhigh_price},yearLow:{stock_yearlow_price}")