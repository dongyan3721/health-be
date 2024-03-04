"""
@author David Antilles
@description 
@timeSnapshot 2024/3/5-00:51:33
"""
from typing import List

from pydantic import BaseModel, field_validator


class KVEntity(BaseModel):
    # id = fields.IntField(pk=True, generated=True)
    # 事实上由label和key构成联合主键
    label: str
    key: int
    value: str

    # 可选 courses: List[int] = []

    @field_validator("key")
    def validate_key(cls, value: str):
        assert value.isalnum(), "键只允许为数字！"
        return value
