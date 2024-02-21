"""
@author David Antilles
@description 数据库表映射类-全部
@timeSnapshot 2024/1/29-19:46:13
"""
from BaseModel import BaseModel, SnowFlakeIDModel, UUIDModel
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
    # gender = fields.CharField(null=False, description='用户性别0男1女2未知', default='0', max_length=1)
    status = fields.CharField(null=False, description='停用状态0正常1停用', default='0', max_length=1)
    self_description = fields.CharField(null=False, description='个人简介', default='这个人很懒，还没有介绍...', max_length=300)
    ip_region = fields.CharField(max_length=256, null=False, default='未知', description='ip归属地')
    urgent_contract = fields.CharField(null=False, max_length=14, description='紧急联系人手机号', default='')


class UserPhysical(SnowFlakeIDModel):
    rel_name = fields.CharField(max_length=256, null=False, description='真实姓名')
    gender = fields.CharField(null=False, description='用户性别0男1女2未知', default='0', max_length=1)
    birthday = fields.DateField(null=False, description='出生年月日')
    identity_card = fields.CharField(max_length=20, description='身份证号', null=False)
    address = fields.CharField(max_length=256, description='居住地')
    weight = fields.DecimalField(max_digits=6, decimal_places=2, description='体重/kg')
    height = fields.DecimalField(max_digits=6, decimal_places=2, description='身高/cm')
    blood_type = fields.CharField(max_length=1, description='血型0A1B2AB3O')

    user_id = fields.ForeignKeyField('Models.Users', related_name='find_physic_bind_user')


class UserPhysicalExamination(SnowFlakeIDModel):
    pass


class UserMedicineHistory(SnowFlakeIDModel):
    illness_name = fields.CharField(max_length=256, null=False, description='病名')
    begin_time = fields.DateField(null=False, description='生病开始时间')
    duration = fields.CharField(max_length=1, null=False, description='持续时间0一个月内1一到三个月2三至半年4半年至一年5一年至三年6三年以上')

    user_id = fields.ForeignKeyField('Models.Users', related_name='find_medicine_history_bind_user')


class Hospital(UUIDModel):
    hospital_name = fields.CharField(max_length=256, description='医院名称', null=False)
    address = fields.CharField(max_length=512, description='医院地址', null=False)


"""
//个人生理情况表，包括真实姓名，性别，出生年月，居住地，身高体重，血型，紧急联系人，外键打到Users
个人体检报告表，包括有的体检项目和体检时间，外键打到Users
个人用药史表，包括病名、用药情况、生病时间、持续时长，外键打到Users
医院信息表-名称、地址、特色、热点指数
医师表-姓名、科室、主治方向、联系方式
静态表-各项体检数据正常值和正常波动范围
静态表-膳食指南
个人饮食量表-热量、照片、识别到的物品名、录入时间
<<扩展>>个人运动量表-运动时间、可能的运动类型、消耗情况、运动时长
<<扩展>>健康计划表-放健康计划
<<扩展>>用户健康计划完成表-
智能诊断-此处主要收集用户行为

"""
