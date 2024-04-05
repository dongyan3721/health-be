"""
@author David Antilles
@description 数据库表映射类-全部
@timeSnapshot 2024/1/29-19:46:13
"""
# from model.CustomBase import BaseModel, SnowFlakeIDModel, UUIDModel
from tortoise import fields
from app.utils.random.index import generate_random_string
from app.model.CustomBase import SnowFlakeIDModel, BaseModel, UUIDModel


# 字典表，一一对应
class KeyValueData(BaseModel):
    id = fields.IntField(pk=True, generated=True)
    # 事实上由label和key构成联合主键
    label = fields.CharField(max_length=64, description='标签', null=False)
    key = fields.CharField(max_length=2, description='键，数字', null=False)
    value = fields.CharField(max_length=64, description='值，数字代表的含义', null=False)

    class Meta:
        table = "b_kv"


# 用户标签表
class UserTags(SnowFlakeIDModel):
    tag_name = fields.CharField(max_length=64, description='用户标签', null=False, default='请填入')

    # 反向查找该标签被哪些用户持有
    find_tag_belong_user: fields.ReverseRelation["Users"]

    class Meta:
        table = "b_user_tags"


# 用户表
class Users(SnowFlakeIDModel):
    username = fields.CharField(null=False, max_length=64, description="用户名", default="用户" + generate_random_string(4))
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

    tags = fields.ManyToManyField("models.UserTags", related_name="find_tag_belong_user")

    # 用户生理信息反向查找
    find_user_bind_physic: fields.ReverseRelation["UserPhysical"]
    # 用户病史反向查找
    find_user_bind_medicine_history: fields.ReverseRelation["UserMedicineHistory"]
    # 用户上传摄入量反向查找
    find_user_bind_uploaded_intake: fields.ReverseRelation["UserUploadedInTake"]
    # 用户体检数据反向查找
    find_user_bind_physical_examination: fields.ReverseRelation["UserPhysicalExamination"]

    class Meta:
        table = "b_user"


# 用户生理信息表
class UserPhysical(SnowFlakeIDModel):
    rel_name = fields.CharField(max_length=256, null=False, description='真实姓名')
    gender = fields.CharField(null=False, description='用户性别0男1女2未知', default='0', max_length=1)
    birthday = fields.DateField(null=False, description='出生年月日')
    identity_card = fields.CharField(max_length=20, description='身份证号', null=False)
    address = fields.CharField(max_length=256, description='居住地', null=True)
    weight = fields.DecimalField(max_digits=6, decimal_places=2, description='体重/kg', null=True)
    height = fields.DecimalField(max_digits=6, decimal_places=2, description='身高/cm', null=True)
    blood_type = fields.CharField(max_length=1, description='血型0A1B2AB3O', null=True)

    user_id = fields.ForeignKeyField('models.Users', related_name='find_user_bind_physic')

    class Meta:
        table = "b_user_physical"


# 用户用药史表
class UserMedicineHistory(SnowFlakeIDModel):
    illness_name = fields.CharField(max_length=256, null=False, description='病名')
    begin_time = fields.DateField(null=False, description='生病开始时间')
    duration = fields.CharField(max_length=1, null=True, description='持续时间0一个月内1一到三个月2三至半年4半年至一年5一年至三年6三年以上')
    medicine = fields.CharField(max_length=256, null=True, description='用药情况')

    user_id = fields.ForeignKeyField('models.Users', related_name='find_user_bind_medicine_history')

    class Meta:
        table = "b_user_medicine_history"


# 医院特色标签表
class HospitalTags(UUIDModel):
    tag_name = fields.CharField(max_length=64, description='医院标签', null=False, default='请填入')

    # 反向查找哪些医院使用了本标签
    find_hospital_tag_bind_hospital: fields.ReverseRelation["Hospital"]

    class Meta:
        table = "b_hospital_tags"


# 医院表
class Hospital(UUIDModel):
    hospital_name = fields.CharField(max_length=256, description='医院名称', null=False)
    address = fields.CharField(max_length=512, description='医院地址', null=False)
    herd_towards_enthusiasm = fields.DecimalField(max_digits=8, decimal_places=2, description='大众对医院的热度', null=True)

    # 医院特色标签
    proficiency_tags = fields.ManyToManyField("models.HospitalTags", related_name="find_hospital_tag_bind_hospital")

    # 反向查找本医院有哪些医生
    find_hospital_raise_doctors: fields.ReverseRelation["HospitalDoctors"]

    class Meta:
        table = "b_hospital"


# 医生标签表
class HospitalDoctorProficiencyTags(UUIDModel):
    tag_name = fields.CharField(max_length=64, description='医生专长标签', null=False, default='请填入')

    # 反向查找哪些医生使用了本标签
    find_doctor_tags_bind_doctors: fields.ReverseRelation["HospitalDoctors"]

    class Meta:
        table = "b_hospital_doctor_tags"


# 医生表
class HospitalDoctors(UUIDModel):
    doctor_name = fields.CharField(max_length=24, description='医师姓名', null=False)
    contact = fields.CharField(max_length=16, description='联系方式(手机)', null=False)

    # 多对多-医生的主治方向标签
    tag_name = fields.ManyToManyField("models.HospitalDoctorProficiencyTags",
                                      related_name="find_doctor_tags_bind_doctors")
    # 外键-医生归属的医院
    hospital_belong = fields.ForeignKeyField("models.Hospital", related_name="find_hospital_raise_doctors")

    class Meta:
        table = "b_hospital_doctors"


# 静态表-体检数据正常值
class StaticRecommendedPerform(SnowFlakeIDModel):
    exam_item = fields.CharField(max_length=255, description='体检项目名称', null=False)
    exam_recommended_perform = fields.DecimalField(max_digits=10, decimal_places=2, description='数据表现', null=False)
    exam_metric = fields.CharField(max_length=32, description='数据单位', null=False)
    find_bind_exam_users: fields.ReverseRelation["UserPhysicalExamination"]

    class Meta:
        table = "b_static_recommended_perform"


# 用户体检数据表
class UserPhysicalExamination(SnowFlakeIDModel):
    exam_item = fields.CharField(max_length=255, description='体检项目名称', null=False)
    exam_perform = fields.DecimalField(max_digits=10, decimal_places=2, description='数据表现', null=False)
    exam_metric = fields.CharField(max_length=32, description='数据单位', null=False)
    exam_recommended_perform = fields.DecimalField(max_digits=10, decimal_places=2, description='正常数据表现', null=False)

    exam_standard = fields.ForeignKeyField("models.StaticRecommendedPerform",
                                           related_name="find_bind_exam_users")

    user_id = fields.ForeignKeyField('models.Users', related_name='find_user_bind_physical-examination')

    class Meta:
        table = "b_user_physical_examination"


# 静态表-膳食指南
class StaticRecommendedNutritionInTake(UUIDModel):
    in_take_case_name = fields.CharField(max_length=32, null=False, description='摄入项目')
    recommended_lower_limit = fields.DecimalField(max_digits=8, decimal_places=2, description='建议摄入最小值')
    recommended_upper_limit = fields.DecimalField(max_digits=8, decimal_places=2, description='建议摄入最大值')
    metric = fields.CharField(max_length=10, null=False, description='计量单位')

    class Meta:
        table = 'b_recommended_nutrition_in_take'


# 用户上传的摄入表
class UserUploadedInTake(SnowFlakeIDModel):
    calorie = fields.DecimalField(max_digits=10, decimal_places=2, null=False, description='摄入热量，单位cal')
    uploaded_image = fields.CharField(max_length=1024, null=False, description='用户上传的食物图片')
    recognized_object = fields.CharField(max_length=512, null=False, description='识别到的照片的内容', default='')
    upload_time = fields.DatetimeField(auto_now=True, description='上传时间')

    user_id = fields.ForeignKeyField("models.Users", related_name="find_user_bind_uploaded_intake")

    class Meta:
        table = 'b_user_in_take'


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
