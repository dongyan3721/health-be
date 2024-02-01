"""
@author David Antilles
@description 数据库表映射类-全部
@timeSnapshot 2024/1/29-19:46:13
"""
from BaseModel import BaseModel, SnowFlakeIDModel
from tortoise import fields


# 字典表，一一对应
class KeyValueData(BaseModel):
    id = fields.IntField(pk=True, generated=True)
    # 事实上由label和key构成联合主键
    label = fields.CharField(max_length=64, description='标签', null=False)
    key = fields.CharField(max_length=2, description='键，数字', null=False)
    value = fields.CharField(max_length=64, description='值，数字代表的含义', null=False)


# 用户标签表
class Tags(SnowFlakeIDModel):
    tag_name = fields.CharField(max_length=64, description='用户标签', null=False, default='请填入')


# 用户表
class Users(SnowFlakeIDModel):
    username = fields.CharField(null=False, max_length=64, description="用户名")
    user_type = fields.CharField(null=False, max_length=1, description='0表示普通用户, 1表示管理员', default='0')
    phone = fields.CharField(null=False, max_length=14, description='注册手机号', default='')
    password = fields.CharField(null=False, max_length=200, description='密码，经过Base64加密')
    # 注册的时候生成一个
    avatar = fields.CharField(null=False, max_length=1024, description='用户头像地址', default='')
    grade = fields.IntField(null=False, default=1, description='用户等级')
    grade_accumulate = fields.IntField(null=False, default=0, description='用户积分/经验')
    gender = fields.CharField(null=False, description='用户性别0男1女2未知', default='0', max_length=1)
    status = fields.CharField(null=False, description='停用状态0正常1停用', default='0', max_length=1)
    self_description = fields.CharField(null=False, description='个人简介', default='这个人很懒，还没有介绍...', max_length=300)
