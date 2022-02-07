import json
import MySQLdb
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # moneybutton ID check
    mb_user_id = event["queryStringParameters"]["mb_user_id"]
    
    #connecting to database to check MB user payment
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('paid_users')
    
    response = table.query(
        KeyConditionExpression=Key('mb_user_id').eq(mb_user_id)
    )
    
    #MB buttons swiped 
    buttons_swiped = []
    for item in response['Items']:
        buttons_swiped.append(item['button_id'])
    
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(buttons_swiped)
    }