import unittest
from decimal import Decimal

from devispora.ovo_auth.model.helpers.dynamodb_token_converter import token_from_dynamodb


class DynamoDBTokenConvertTest(unittest.TestCase):

    def test_token_conversion(self):
        dynamo_response = {
            'groups': 'Test',
            'extra_reps': {
                Decimal('241254536346')
            },
            'discord_id': Decimal('241254536342'),
            'token_id': 'LostInTest5'
        }
        result = token_from_dynamodb(dynamo_response)
        self.assertEqual('241254536346', result.extra_reps[0])
        self.assertEqual('241254536342', result.discord_id)
