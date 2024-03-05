"""
@author David Antilles
@description RSA加密解密器
@timeSnapshot 2024/2/2-00:32:39
"""
import rsa
from app.framework.config.ApplicationProperties import APPLICATION_PROPERTIES
import base64


def load_key_from_string(key_str, is_private=True):
    # 根据是否为私钥，选择加载公钥或私钥
    if is_private:
        key = rsa.PrivateKey.load_pkcs1(key_str.encode('utf-8'))
    else:
        key = rsa.PublicKey.load_pkcs1(key_str.encode('utf-8'))

    return key


class RSAUtil:
    private_key: rsa.PrivateKey = load_key_from_string(APPLICATION_PROPERTIES["keys"]['private'], True)
    public_key: rsa.PublicKey = load_key_from_string(APPLICATION_PROPERTIES['keys']['public'], False)

    @classmethod
    async def encrypt(cls, text: str):
        return base64.b64encode(rsa.encrypt(text.encode('utf-8'), cls.public_key)).decode('utf-8')

    @classmethod
    async def decrypt(cls, encrypted_message):
        return rsa.decrypt(base64.b64decode(encrypted_message), cls.private_key).decode('utf-8')
