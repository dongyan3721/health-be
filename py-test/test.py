"""
@author David Antilles
@description 
@timeSnapshot 2024/2/1-21:57:39
"""
import rsa
import base64

print('==========================================================')


# 生成公钥和私钥
(pubkey, privkey) = rsa.newkeys(1024)

# 原始消息
message = "Hello, RSA!"

# 将消息转换为字节
message_bytes = message.encode('utf-8')

# 使用公钥加密消息
encrypted_bytes = rsa.encrypt(message_bytes, pubkey)

# 将加密后的字节转换为Base64编码的字符串
encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')

# 打印加密后的Base64字符串
print(f"Encrypted message (Base64): {encrypted_base64}")

# 将Base64编码的字符串转换回字节
decrypted_bytes = base64.b64decode(encrypted_base64.encode('utf-8'))

# 使用私钥解密消息
decrypted_message = rsa.decrypt(decrypted_bytes, privkey).decode('utf-8')

# 打印解密后的消息
print(f"Decrypted message: {decrypted_message}")
