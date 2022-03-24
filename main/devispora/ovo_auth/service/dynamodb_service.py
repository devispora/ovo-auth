import boto3
from boto3.dynamodb.conditions import Key
from devispora.ovo_auth.model.token import token_table_name

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
