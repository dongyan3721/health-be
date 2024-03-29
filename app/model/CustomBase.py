"""
@author David Antilles
@description 基础库，共有一些属性
@timeSnapshot 2024/1/29-19:56:16
@official https://tortoise-orm.readthedocs.io/en/latest/index.html
"""
import uuid

from tortoise.models import Model
from app.model.CustomizedTableFields import *
from app.utils.table.SnowflakeGenerator import SnowflakeIDGenerator
from tortoise import fields


class BaseModel(Model):
    del_flag = fields.CharField(max_length=1, description='删除标记0存在1删除', default='0')
    create_by = fields.CharField(max_length=64, description='创建人', null=True)
    create_time = fields.DatetimeField(auto_now=True, null=True, description='创建时间')
    modify_by = fields.CharField(max_length=64, description='修改人', null=True)
    modify_time = fields.DatetimeField(description='修改时间', null=True)
    remark = fields.CharField(max_length=500, description='备注', null=True)

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


class UUIDModel(BaseModel):
    # 这里的ID要用自定义算法生成，generated为False
    id = fields.CharField(max_length=36, description='UUID', pk=True, generated=False)

    @classmethod
    async def create(cls, **kwargs):
        kwargs["id"] = uuid.uuid1()
        return await super().create(**kwargs)

    class Meta:
        abstract = True
