"""
@author David Antilles
@description 定制化表格列
@timeSnapshot 2024/1/29-20:25:54
"""
from typing import Any

from tortoise import fields


# 雪花算法ID列
class SnowflakeField(fields.BigIntField):
    SQL_TYPE = "BIGINT UNSIGNED"
    allows_generated = True

    def __init__(self, pk: bool = False, **kwargs: Any) -> None:
        if pk:
            kwargs["generated"] = bool(kwargs.get("generated", True))
        super().__init__(pk=pk, **kwargs)

    @property
    def constraints(self) -> dict:
        return {
            "ge": 1 if self.generated or self.reference else 0,
            "le": 9223372036854775807,
        }

    class _db_mysql:
        GENERATED_SQL = "BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT"
