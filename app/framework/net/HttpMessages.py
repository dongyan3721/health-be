"""
@author David Antilles
@description 通用属性-消息传输
@timeSnapshot 2024/2/1-22:07:57
"""
from framework.net.HttpStatus import HttpStatus


class AjaxResult:
    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg

    @staticmethod
    def ok():
        return AjaxResult(HttpStatus.OK, "success")

    @staticmethod
    def error():
        return AjaxResult(HttpStatus.INTERNAL_SERVER_ERROR, "error")

    @staticmethod
    def ok_extended(**kv):
        kv["code"] = HttpStatus.OK
        kv["msg"] = "success"
        return kv


class TableData(AjaxResult):
    def __init__(self, code: int, msg: str, rows: list, total: int):
        super().__init__(code, msg)
        self.rows = rows
        self.total = total
