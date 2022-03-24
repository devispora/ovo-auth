from devispora.ovo_auth.exception.exceptions import RequestException, RequestExceptionMessage
from devispora.ovo_auth.model.constants import Constants
from devispora.ovo_auth.model.helpers.dynamodb_token_converter import token_from_dynamodb
from devispora.ovo_auth.model.responses import error_response, generic_response
from devispora.ovo_auth.model.token_result import TokenResult
from devispora.ovo_auth.service.dynamodb_service import retrieve_token
from devispora.ovo_auth.service.jwt_generator import generate_jwt


constants = Constants()


def process_token(token_id: str):
    token_result = retrieve_token_information(token_id)
    if token_result.accepted:
        target = token_from_dynamodb(token_result.token_info)
        if target.enabled is True:
            generated_jwt = generate_jwt(constants, target)
            return generic_response({
                'jwt': generated_jwt
            })
    # else
    return error_response(401, RequestException(RequestExceptionMessage.CodeNoLongerValid))


def retrieve_token_information(token_id: str) -> []:
    token_result = retrieve_token(token_id)
    if token_result:
        return TokenResult(True, token_result[0])
    else:
        return TokenResult(False)
