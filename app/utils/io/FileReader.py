"""
@author David Antilles
@description 常见数据文件读取器
@timeSnapshot 2024/1/29-21:08:58
"""

import json
from typing import Any
import yaml

import chardet

import os


def print_absolute_path(relative_path):
    absolute_path = os.path.abspath(relative_path)
    print(absolute_path)


class JsonReader:
    def __init__(self, file_path):
        self._file_path = file_path
        with open(self._file_path, 'rb') as file:
            rawdata = file.read()
            result = chardet.detect(rawdata)
            encoding = result['encoding']
            self._data = json.load(file, encoding=encoding)

    def read(self, key: Any):
        return self._data[key]

    @property
    def original_data(self):
        return self._data


class YamlReader:
    def __init__(self, file_path):
        self._file_path = file_path
        # print_absolute_path(file_path)
        encoding = 'UTF-8'
        with open(self._file_path, 'rb') as file:
            rawdata = file.read()
            result = chardet.detect(rawdata)
            encoding = result['encoding']

        with open(self._file_path, 'r', encoding=encoding) as file:
            self._data = yaml.safe_load(file)

    def read(self, key: Any):
        return self._data[key]

    @property
    def original_data(self):
        return self._data

    @classmethod
    def test(cls):
        print(os.curdir)
