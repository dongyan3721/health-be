"""
@author David Antilles
@description 通用属性-消息传输
@timeSnapshot 2024/2/1-22:07:57
"""


class PlainMessage:
    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg
