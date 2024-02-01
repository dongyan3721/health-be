"""
@author David Antilles
@description 基础库，共有一些属性
@timeSnapshot 2024/1/29-19:56:16
@official https://tortoise-orm.readthedocs.io/en/latest/index.html
"""
import datetime

from tortoise.models import Model
from CustomizedTableFields import *
from utils.table.SnowflakeGenerator import SnowflakeIDGenerator
from tortoise import fields


class BaseModel(Model):
    create_by = fields.CharField(max_length=64, description='创建人')
    create_time = fields.DatetimeField(default=datetime.datetime.now(), description='创建时间')
    modify_by = fields.CharField(max_length=64, description='修改人')
    modify_time = fields.DatetimeField(description='修改时间')
    remark = fields.CharField(max_length=500, description='备注')

    class Meta:
        abstract = True


class SnowFlakeIDModel(BaseModel):
    # 这里的ID要用自定义算法生成，generated为False
    id = SnowflakeField(pk=True, generated=False, description='snowflake-id')

    @classmethod
    async def create(cls, **kwargs):
        kwargs["id"] = await SnowflakeIDGenerator(cls).generate_id()
        return await super().create(**kwargs)

    class Meta:
        abstract = True
