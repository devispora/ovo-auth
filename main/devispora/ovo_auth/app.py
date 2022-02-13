import json

from devispora.ovo_auth.service.token_exchanger import process_token


def lambda_handler(event, context):
    raw_body = event['body']
    body = json.loads(raw_body)
    return process_token(body['code'])
