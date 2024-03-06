"""
@author David Antilles
@description 文件上传下载配置
@timeSnapshot 2024/3/6-17:35:54
"""
import shutil
import uuid

from app.framework.config.ApplicationProperties import APPLICATION_PROPERTIES
from app.utils.string.index import StringBuilder


def getAvatarUploadPath():
    return APPLICATION_PROPERTIES["file-upload"] + 'avatar/'


def getFileExtension(original_filename: str):
    return '.'+original_filename.split('.')[-1]


def calculateRelativeUrlPattern(full_file_path: str):
    return f"static/{full_file_path.replace(APPLICATION_PROPERTIES['file-upload'], '')}"


def generate_default_avatar():
    file_storage_path = StringBuilder().add(getAvatarUploadPath()).add(uuid.uuid1()).add('.png').toString()
    shutil.copy(getAvatarUploadPath()+'ikun.png', file_storage_path)
    return calculateRelativeUrlPattern(file_storage_path)
