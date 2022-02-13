from datetime import datetime, timedelta

import jwt

from devispora.ovo_auth.model.auth import AuthAudience
from devispora.ovo_auth.model.constants import Constants
from devispora.ovo_auth.model.token import Token


def generate_jwt(constants: Constants, claims: Token) -> str:
    ovo_secret = bytes(constants.ovo_secret, 'utf-8')
    start_time = datetime.utcnow()
    expiry_time = start_time + timedelta(minutes=30)

    payload = {
        'iat': start_time,
        'exp': expiry_time,
        'ovo_claims': claims,
        'aud': AuthAudience.OvO.value

    }
    return jwt.encode(
        payload=payload,
        key=ovo_secret,
        algorithm='HS512'
    )
