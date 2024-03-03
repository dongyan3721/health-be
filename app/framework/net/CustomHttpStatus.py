"""
@author David Antilles
@description 定制的Http状态码
@timeSnapshot 2024/3/3-13:37:39
"""


class CustomHttpStatus:

    # 核验jwt令牌，核验结果为不需要更新的返回值
    NO_NEED_TO_FLUSH = 1000

    # 数据库设置为unique的字段发生重复
    VALUE_REPEATED = 2000
