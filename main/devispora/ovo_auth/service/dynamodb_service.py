import boto3
from boto3.dynamodb.conditions import Key
from devispora.ovo_auth.model.token import token_table_name

dynamodb = boto3.resource('dynamodb')


class DynamoDBService:
    pass


def retrieve_token(token_id: str):
    table = dynamodb.Table(token_table_name)
    expression = Key('token_id').eq(token_id)
    response = table.query(KeyConditionExpression=expression)
    return response['Items']
