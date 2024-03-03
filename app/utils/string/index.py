"""
@author David Antilles
@description 封装常用字符串工具函数
@timeSnapshot 2024/3/3-13:35:22
"""


# 模式匹配
import io
import re


# 字符串模式匹配
def matches(original: str, pattern: str):
    return re.match(pattern, original)


# 用规定的字符补足到指定的长度
def complement(original, size, c):
    sb = io.StringIO()

    if original is not None:
        length = len(original)
        if length <= size:
            for i in range(size - length):
                sb.write(c)
            sb.write(original)
        else:
            return original[length - size:]
    else:
        for i in range(size):
            sb.write(c)

    return sb.getvalue()


# 工具类，构建字符串，获取完字符串后生命周期结束
class StringBuilder:
    def __init__(self):
        self.sb = io.StringIO()

    # 元素添加
    def add(self, val):
        self.sb.write(val if isinstance(val, str) else str(val))
        return self

    # 转字符串
    def toString(self) -> str:
        ret = self.sb.getvalue()
        self.sb.close()
        return ret
