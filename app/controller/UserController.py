"""
@author David Antilles
@description 用户相关
@timeSnapshot 2024/3/5-20:50:14
"""
import uuid

from fastapi import APIRouter, UploadFile, File, Depends
# from starlette.responses import JSONResponse # 支持自定义响应体和响应头
from starlette.requests import Request

from app.entity.form import UserModifyDependency
from app.entity.raw import UserEntity
from app.framework.config.FileConfig import getAvatarUploadPath, getFileExtension, calculateRelativeUrlPattern
from app.framework.net.HttpMessages import AjaxResult
from app.framework.net.HttpStatus import HttpStatus
from app.model.models import Users, UserTags
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from app.utils.cryptor.RSAUtil import RSAUtil
from app.utils.ipUtils import get_ip_info_async

user_router = APIRouter()


@user_router.post("/user/add")
async def registerUser(user_entity: UserEntity, request: Request):

    params = user_entity.model_dump(exclude_unset=True)

    # 优先判断有没有重复手机号
    if await Users.filter(phone=params['phone']).first().values('phone'):
        return AjaxResult.error('重复注册！')

    # 获取ip归属地信息
    params['ip_region'] = await get_ip_info_async(request.client.host)
    params['password'] = await RSAUtil.encrypt(params['password'])
    # TODO 做上默认头像
    if user_entity.tags:
        tags = await UserTags.filter(id__in=params.pop('tags'))
        created_user: Users = await Users.create(**params)  # type: ignore
        await created_user.tags.add(*tags)
        return AjaxResult.ok()
    await Users.create(**params)  # type: ignore
    return AjaxResult.ok()


# 至多包含2次数据库读写操作和1次网络请求、一次RSA1024解密
# 获取ip地址的网络请求大约耗时2秒
@user_router.post('/user/login')
async def loginUser(user_entity: UserEntity, request: Request):
    params = user_entity.model_dump(exclude_unset=True)

    # 创建用户模型的pydantic实例
    user_pydantic_instance = pydantic_model_creator(Users, exclude=('find_user_bind_medicine_history',
                                                                    'find_user_bind_physic', 'find_user_bind_uploaded_intake'))
    selected_user = (await user_pydantic_instance.from_tortoise_orm(await Users.get(phone=params['phone']))).model_dump()
    if selected_user:
        if params['password'] == await RSAUtil.decrypt(selected_user['password']):
            # 登录无误，更新用户的ip归属地
            ip_region = await get_ip_info_async(request.client.host)
            # ip_region = await get_ip_info_async('1.1.1.2')
            await Users.filter(phone=params['phone']).update(ip_region=ip_region)
            selected_user.pop('password')
            selected_user['ip_region'] = ip_region
            # TODO 返回token
            return AjaxResult.ok_extended(data=selected_user)
        return AjaxResult(HttpStatus.FORBIDDEN, '账号或密码错误')
    return AjaxResult(HttpStatus.FORBIDDEN, '账号或密码错误')


@user_router.put('/user/update')
async def updateUser(avatar: UploadFile = File(None), user: UserModifyDependency = Depends(UserModifyDependency)):
    values = user.model_dump(exclude_none=True)
    if values.get('id') < 0:
        return AjaxResult.error('修改失败，检查请求参数！')
    if avatar:
        full_storage_path = getAvatarUploadPath() + str(uuid.uuid1()) + getFileExtension(avatar.filename)
        contents = await avatar.read()
        with open(full_storage_path, "wb+") as f:
            f.write(contents)
        values['avatar'] = calculateRelativeUrlPattern(full_storage_path)
    values.pop('id')
    count = await Users.filter(id=user.id)
    if len(count):
        await Users.filter(id=user.id).update(**values)
        return AjaxResult.ok()
    return AjaxResult.error('修改失败，检查请求参数！')
