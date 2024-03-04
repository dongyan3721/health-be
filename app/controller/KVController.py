"""
@author David Antilles
@description 字典表访问
@timeSnapshot 2024/3/4-21:16:30
"""
from fastapi import APIRouter

from app.framework.net.HttpMessages import TableData, AjaxResult
from app.model.models import KeyValueData
from app.entity.entities import KVEntity

kv = APIRouter()

# 查全部-model.all()
# 限制查询-model.filter(**kwargs)，键对应数据库中的字段=>QuerySet
# get方式查询单个-model.get(**kwargs)，键对应数据库中的字段=>Model类
# 模糊查询column__gt >; column__lt <; column__in [iterable]; 作用于filter
# values查询 models.all/filter/.values(*args) args为数据库字段      相当于投影


@kv.get("/{dict_name}")
async def getSpecificDict(dict_name: str):
    selected_dict = await KeyValueData.filter(label=dict_name)
    return TableData.success(selected_dict, len(selected_dict))


@kv.post("/add")
async def insertIntoKVNewDict(kv_entity: KVEntity):
    received_student_dto = KeyValueData(label=kv_entity.label, key=kv_entity.key, value=kv_entity.value)
    exist_dict = await KeyValueData.filter(label=kv_entity.label, key=kv_entity.key)
    if len(exist_dict) == 0:
        await received_student_dto.save()
        return AjaxResult.ok()
    return AjaxResult.error("键重复！")


