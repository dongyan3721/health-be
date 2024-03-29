"""
@author David Antilles
@description 供请求体中访问
@timeSnapshot 2024/3/5-00:51:33
"""
import datetime
from typing import List, Optional, Union

from pydantic import BaseModel, field_validator


class KVEntity(BaseModel):
    # id = fields.IntField(pk=True, generated=True)
    # 事实上由label和key构成联合主键
    label: str
    key: int
    # 删除时为可选参数
    value: Optional[str] = None

    # 可选 courses: List[int] = []


class HospitalEntity(BaseModel):
    id: Optional[str] = None
    hospital_name: str
    address: str
    herd_towards_enthusiasm: Union[float, None] = None
    # 传递过来的医院特色id列表
    proficiency_tags: List[str] = []
    # 传递过来的医院医生列表
    # find_hospital_raise_doctors: List[str] = []


class UserEntity(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    user_type: Optional[str] = None
    phone: str
    avatar: Optional[str] = None
    password: str
    grade: Optional[int] = None
    grade_accumulate: Optional[int] = None
    self_description: Optional[str] = None
    ip_region: Optional[str] = None
    urgent_contact: Optional[str] = None
    tags: List[int] = []


class UserPasswordModifyEntity(BaseModel):
    id: int
    original_password: str
    new_password: str


class UserMedicineHistoryEntity(BaseModel):
    id: Optional[int] = None
    illness_name: str
    begin_time: datetime.date
    duration: Optional[str] = None
    medicine: Optional[str] = None
    user_id_id: Optional[int] = None


class UserPhysicalEntity(BaseModel):
    id: Optional[int] = None
    rel_name: str
    gender: str
    birthday: datetime.datetime
    identity_card: str
    address: Optional[str] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    blood_type: Optional[str] = None
    user_id_id: int
