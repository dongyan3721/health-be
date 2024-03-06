"""
@author David Antilles
@description 医院相关访问类
@timeSnapshot 2024/3/5-11:53:36
重要：BaseModel只重写了create方法，所以继承自UUIDModel、SnowflakeModel的模型类新增一定要用create
"""

# filter可以指定的对象：
#
# not
# in ：检查字段的值是否在传递列表中
# not_in
# gte：大于或等于传递的值
# gt：大于传递值
# lte：低于或等于传递的值
# lt：低于通过值
# range：介于和给定两个值之间
# isnull：字段为空
# not_isnull：字段不为空
# contains：字段包含指定的子字符串
# icontains：不区分大小写contains
# startswith：如果字段以值开头
# istartswith：不区分大小写startswith
# endswith：如果字段以值结尾
# iendswith：不区分大小写endswith
# iexact：不区分大小写等于
# search：全文搜索


from fastapi import APIRouter
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from app.entity.raw import *
from app.framework.net.HttpMessages import TableData, AjaxResult
from app.model.models import *

hospital_route = APIRouter()


# async def test():
#     return pydantic_model_creator(Hospital)


# 一定要把list放在上面
@hospital_route.get("/hospital_query/list")
async def hospitalQuery(
        skip: int = 0,
        limit: int = 10
):
    hospital_queryset_pydantic_instance = pydantic_queryset_creator(Hospital, exclude=('find_hospital_raise_doctors',))
    result = (await hospital_queryset_pydantic_instance.from_queryset(
        Hospital.all().offset(skip * limit).limit(limit))).model_dump()
    return TableData.success(result, len(result))


# 雷点：只支持异步上下文，同步初始化的Pydantic模型类没有用，不大费周章专门搞一个地方放Pydantic模型类
# 总结：想着MVC架构还是洗洗睡吧，把这个类当变量用得了
@hospital_route.get("/hospital_query/{hospital_id}")
async def hospitalQueryDetail(hospital_id: str):
    # resource = await PydanticModelHospital.from_tortoise_orm(await Hospital.filter(id=hospital_id).first())
    # threee = await (await test()).from_tortoise_orm(await Hospital.filter(id=hospital_id).first())
    # exclude：这是干什么，太丑了吧
    hospital_pydantic_instance = pydantic_model_creator(Hospital, exclude=('find_hospital_raise_doctors',))
    result = await hospital_pydantic_instance.from_tortoise_orm(await Hospital.get(id=hospital_id))
    return AjaxResult.ok_extended(data=result.model_dump())


@hospital_route.post("/hospital_add")
async def addHospital(hopital: HospitalEntity):
    # 继承的子类，不会出问题
    inserted_hospital: Hospital = await Hospital.create(  # type: ignore
        hospital_name=hopital.hospital_name,
        address=hopital.address,
        herd_towards_enthusiasm=hopital.herd_towards_enthusiasm
        # proficiency_tags=hopital.proficiency_tags
    )
    initial_tags = await HospitalTags.filter(id__in=hopital.proficiency_tags)
    await inserted_hospital.proficiency_tags.add(*initial_tags)
    return AjaxResult.ok()


@hospital_route.put("/hospital_update")
async def updateHospital(hospital: HospitalEntity):
    params = hospital.model_dump(exclude_unset=True)
    params.pop('id')
    tag_ids = params.pop("proficiency_tags")
    affected = await Hospital.filter(id=hospital.id).update(**params)
    tags = await HospitalTags.filter(id__in=tag_ids)
    selected_hospital: Hospital = await Hospital.get(id=hospital.id)
    await selected_hospital.proficiency_tags.clear()
    await selected_hospital.proficiency_tags.add(*tags)
    if affected:
        return AjaxResult.ok()
    else:
        return AjaxResult.error("修改的对象不存在！")

# 删除？不许！

