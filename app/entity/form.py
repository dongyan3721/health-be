"""
@author David Antilles
@description 传输实体的FormData版本
@timeSnapshot 2024/3/6-14:18:27
"""
import datetime
from typing import Optional, List

from fastapi import Form


class UserModifyDependency:
    def __init__(
            self,
            id: Optional[int] = Form(-1),
            username: Optional[str] = Form(None),
            user_type: Optional[str] = Form(None),
            phone: Optional[str] = Form(None),
            password: Optional[str] = Form(None),
            grade: Optional[int] = Form(None),
            grade_accumulate: Optional[int] = Form(None),
            self_description: Optional[str] = Form(None),
            ip_region: Optional[str] = Form(None),
            urgent_contact: Optional[str] = Form(None)
    ):
        # 对不符合本次请求规范的数据赋空值
        self.id = id
        self.username = username
        self.user_type = None
        self.phone = phone
        self.password = None
        self.grade = None
        self.grade_accumulate = None
        self.self_description = self_description
        self.ip_region = None
        self.urgent_contact = urgent_contact

    def model_dump(self, exclude_none: bool = True):
        return {key: value for key, value in vars(self).items() if value} if exclude_none else {key: value for key, value in vars(self).items()}


class UserIntakeDependency:
    def __init__(
            self,
            user_id_id: str,
            id: Optional[str] = Form(None),
            calorie: Optional[float] = Form(None),
            recognized_object: Optional[str] = Form(None),
            upload_time: Optional[datetime.datetime] = Form(None),
    ):
        self.id = id
        self.calorie = calorie
        self.recognized_object = recognized_object
        self.upload_time = upload_time
        self.user_id = user_id_id

    def model_dump(self, exclude_none: bool = True):
        return {key: value for key, value in vars(self).items() if value} if exclude_none else {key: value for key, value in vars(self).items()}


