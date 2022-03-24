from decimal import Decimal

from devispora.ovo_auth.model.token import Token


def token_from_dynamodb(dynamodb_token: dict) -> Token:
    new_token = Token(
        token_id=dynamodb_token['token_id'],
        enabled=dynamodb_token['enabled'],
        redeem_code=dynamodb_token['redeem_code'],
        discord_id=decimal_to_string(dynamodb_token['discord_id']),
        groups=dynamodb_token['groups']
    )
    if 'extra_reps' in dynamodb_token:
        new_token.extra_reps = convert_dynamo_list(dynamodb_token['extra_reps'])
    return new_token


def convert_dynamo_list(extra_reps: {}):
    new_list = []
    for rep in extra_reps:
        new_list.append(decimal_to_string(rep))
    return new_list


def decimal_to_string(decimal: Decimal) -> str:
    return str(decimal.__int__())
