"""
@author David Antilles
@description 读取配置信息
@timeSnapshot 2024/1/29-20:56:15
@warning 禁止在本文件内格式化代码
"""

from app.utils.io.FileReader import YamlReader

APPLICATION_PROPERTIES = YamlReader('C:/Users/29145/Desktop/Programming/health-be/resource/application.yaml').original_data

