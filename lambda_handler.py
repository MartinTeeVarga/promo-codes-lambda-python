from __future__ import print_function

import json

import boto3
from botocore.exceptions import ClientError


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    if not 'game' in event:
        return respond(ValueError('Missing game parameter.'))
    elif not 'code' in event:
        return respond(ValueError('Missing code parameter.'))

    code = event['code']
    game = event['game']

    code_table = boto3.resource('dynamodb').Table('Code')

    try:
        response = code_table.get_item(Key={
            'gameId': game,
            'codeId': code
        })
    except ClientError as e:
        return respond(ValueError('Error fetching code. ' + e.message))
    else:
        item = response['Item']
        print("GetItem succeeded:")
        print(json.dumps(item, indent=4))
        return respond(None, item)
