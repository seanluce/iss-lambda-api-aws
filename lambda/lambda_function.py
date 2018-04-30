import requests
import json

def lambda_handler(event, context):
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    lat = (data["iss_position"]["latitude"])
    long = (data["iss_position"]["longitude"])
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json" , "Access-Control-Allow-Origin": "*"},
        "body": "{\"latitude\" : " + lat + ", \"longitude\" : " + long + "}"
    }
