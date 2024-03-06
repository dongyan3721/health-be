"""
@author David Antilles
@description 用户相关
@timeSnapshot 2024/3/5-20:50:14
"""
import uuid

from fastapi import APIRouter, File, Depends, UploadFile
from starlette.requests import Request
from tortoise.contrib.pydantic import pydantic_model_creator

from app.entity.form import UserModifyDependency
from app.entity.raw import UserEntity
from app.framework.config.FileConfig import getAvatarUploadPath, getFileExtension, calculateRelativeUrlPattern, \
    generate_default_avatar
from app.framework.net.HttpMessages import AjaxResult
from app.framework.net.HttpStatus import HttpStatus
from app.model.models import Users, UserTags
from app.utils.JwtUtils import JwtUtils
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
    params['avatar'] = generate_default_avatar()
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
        # 比较密码和的解密的密码
        if params['password'] == await RSAUtil.decrypt(selected_user['password']):
            # 无误，更新用户的ip归属地
            new_ip = await get_ip_info_async(request.client.host)
            await Users.filter(phone=params['phone']).update(ip_region=new_ip)
            # 排除不需要给到前端的字段
            selected_user.pop('password')
            # 修正的ip地址直接给回前端
            selected_user['ip_region'] = new_ip
            # 用手机号签名，生成token
            return AjaxResult.ok_extended(data=selected_user, token=JwtUtils.sign(params.get('phone')))
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
