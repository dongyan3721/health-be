"""
@author David Antilles
@description RSA密钥生成器
@timeSnapshot 2024/2/2-00:04:09
"""
import rsa


def generate_key_pair():
    # 生成RSA密钥对
    (public_key, private_key) = rsa.newkeys(1024)  # 512表示密钥长度，可以根据需求选择合适的长度

    # 将公钥和私钥转换为字符串形式
    public_key_str = public_key.save_pkcs1().decode()
    private_key_str = private_key.save_pkcs1().decode()

    return public_key_str, private_key_str


def load_key_from_string(key_str, is_private=True):
    # 根据是否为私钥，选择加载公钥或私钥
    if is_private:
        key = rsa.PrivateKey.load_pkcs1(key_str.encode())
    else:
        key = rsa.PublicKey.load_pkcs1(key_str.encode())

    return key


# 生成RSA密钥对并获取其字符串形式
public_key_str, private_key_str = generate_key_pair()

# 输出公钥和私钥字符串
print("公钥字符串: ", public_key_str)
print("私钥字符串: ", private_key_str)

# 加载公钥和私钥
loaded_public_key = load_key_from_string(public_key_str, is_private=False)
loaded_private_key = load_key_from_string(private_key_str, is_private=True)

# 输出加载的公钥和私钥
print("加载的公钥: ", loaded_public_key)
print("加载的私钥: ", loaded_private_key)
