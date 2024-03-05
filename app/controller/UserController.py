"""
@author David Antilles
@description 用户相关
@timeSnapshot 2024/3/5-20:50:14
"""
from fastapi import APIRouter
# from starlette.responses import JSONResponse # 支持自定义响应体和响应头
from starlette.requests import Request

from app.entity.entities import UserEntity
from app.framework.net.HttpMessages import AjaxResult
from app.model.models import Users, UserTags
# from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from app.utils.cryptor.RSAUtil import RSAUtil
from app.utils.ipUtils import get_ip_info_async

user_router = APIRouter()


@user_router.post("/user/add")
async def registerUser(user_entity: UserEntity, request: Request):

    params = user_entity.model_dump(exclude_unset=True)
    # 获取ip归属地信息
    params['ip_region'] = await get_ip_info_async(request.client.host)
    params['password'] = await RSAUtil.encrypt(params['password'])
    # TODO 做上默认头像
    tags = await UserTags.filter(id__in=params.pop('tags'))
    created_user: Users = await Users.create(**params)  # type: ignore
    await created_user.tags.add(*tags)
    return AjaxResult.ok()
