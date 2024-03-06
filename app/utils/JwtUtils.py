"""
@author David Antilles
@description 
@timeSnapshot 2024/3/6-19:21:48
"""

import jwt
from datetime import datetime, timedelta
from app.framework.config.ApplicationProperties import APPLICATION_PROPERTIES


class JwtUtils:
    """
    JWT Utility class for token generation, verification, and expiration check.
    """

    EXPIRE_TIME = APPLICATION_PROPERTIES.get('jwt').get('expired')

    TOKEN_SECRET = APPLICATION_PROPERTIES.get('jwt').get('sign')

    ALGORITHM = APPLICATION_PROPERTIES.get('jwt').get('algorithm')

    @classmethod
    def sign(cls, user_name):
        """
        Generate JWT token.
        :param user_name: User name
        :return: Token
        """
        expire_time = datetime.utcnow() + timedelta(minutes=cls.EXPIRE_TIME)
        token_payload = {
            'sub': user_name,
            'exp': expire_time
        }
        token = jwt.encode(token_payload, cls.TOKEN_SECRET, cls.ALGORITHM)
        return token

    @classmethod
    def verify(cls, token):
        """
        Verify JWT token and return the user name.
        :param token: Token to verify
        :return: User name
        """
        try:
            decoded_token = jwt.decode(token, cls.TOKEN_SECRET, cls.ALGORITHM)
            return decoded_token['sub']
        except jwt.ExpiredSignatureError:
            raise Exception("Time expired")
        except jwt.InvalidTokenError:
            raise Exception("Token error")

    @classmethod
    def is_need_update(cls, token):
        """
        Check if the token needs to be updated.
        :param token: Token to check
        :return: True if the token needs to be updated, False otherwise
        """
        try:
            decoded_token = jwt.decode(token, cls.TOKEN_SECRET, cls.ALGORITHM)
            expires_at = decoded_token['exp']
            return expires_at - datetime.now().timestamp() < 60 * cls.EXPIRE_TIME / 2
        except jwt.ExpiredSignatureError:
            return True
        except jwt.InvalidTokenError:
            return False
