import requests
import json
import boto3 #needed for DynamoDB
import time

def lambda_handler(event, context):
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    
    dbClient = boto3.resource('dynamodb')
    dbTable = dbClient.Table('ISShistory')
    
    lat = (data["iss_position"]["latitude"])
    long = (data["iss_position"]["longitude"])
    
    epochtime = time.time()
    
    dbTable.put_item(
            Item={
                'ID': str(epochtime),
                'latitude': lat,
                'longitude': long
            }
        
        ) 
    
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json" , "Access-Control-Allow-Origin": "*"},
        "body": "{\"latitude\" : " + lat + ", \"longitude\" : " + long + "}"
    }
