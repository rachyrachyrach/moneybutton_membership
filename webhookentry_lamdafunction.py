import json
import MySQLdb
import boto3

def lambda_handler(event, context):
    
    debug = False
    
    json_body = json.loads(event['body'])
    
      if json_body['secret'] != "Your Secret Webhook number":
    
       return {
           'statusCode': 403,
          'body': json.dumps('Unauthorized')
     }
    
    #connecting to database to check MB user payment
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('paid_users')

    if debug:
        print("DEBUG ")
    #    print(json_body['secret'])
        print(json_body['payment']['buttonId'])
        print(json_body['payment']['userId'])
    response = table.put_item(
       Item={
            'mb_user_id': json_body['payment']['userId'],
            'button_id': json_body['payment']['buttonId'],
            'payload' : json_body['payment']
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }