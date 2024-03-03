"""
@author David Antilles
@description 常用随机函数
@timeSnapshot 2024/3/3-13:31:13
"""

import random
import string


def generate_random_string(length) -> str:
    # 从字母和数字中生成随机字符串
    characters = string.ascii_letters + string.digits
    # 使用random模块生成指定长度的随机字符串
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
