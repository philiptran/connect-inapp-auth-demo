import os
import jwt
from datetime import datetime, timedelta

JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 500
CONNECT_SECRET = os.environ['CONNECT_SECRET']
CONNECT_WIDGET_ID = os.environ['CONNECT_WIDGET_ID']

def lambda_handler(event, context):    
    # Retrieve the current logged in user and formulat the payload with the contact attributes
    # for sending to Amazon Connect. Below is hard-coded caller info for demo purpose.
    payload = {
        'sub': CONNECT_WIDGET_ID,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS),
        'attributes': {'customerName': 'Demo User', 'userid': 'demo01'}
    }
    header = {
        'typ': "JWT",
        'alg': 'HS256'
    }
    encoded_token = jwt.encode((payload), CONNECT_SECRET, algorithm=JWT_ALGORITHM, headers=header)
    print(encoded_token)
    
    # TODO implement
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET"
        },
        'body': encoded_token
    }
