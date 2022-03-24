import boto3
from boto3.dynamodb.conditions import Key
from devispora.ovo_auth.model.token import token_table_name, Token

dynamodb = boto3.resource('dynamodb')


class DynamoDBService:
    pass


def retrieve_token(redeem_code: str):
    table = dynamodb.Table(token_table_name)
    expression = Key('redeem_code').eq(redeem_code)
    response = table.query(
        IndexName='redeem_code-index',
        KeyConditionExpression=expression
    )
    return response['Items']


def invalidate_token(token: Token):
    table = dynamodb.Table(token_table_name)
    response = table.update_item(
        Key={
            'token_id': token.token_id,
            'discord_id': int(token.discord_id)
        },
        UpdateExpression="set enabled=:e",
        ExpressionAttributeValues={
            ':e': False
        },
        ReturnValues="UPDATED_NEW")
    response_code = response['ResponseMetadata']['HTTPStatusCode']
    if response_code != 200:
        print(response)
        print(f'response code: {response_code}')
        print(f'Warn: Did not manage to disable token: {token.token_id}')
