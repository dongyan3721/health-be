"""
@author David Antilles
@description 关键词提取
@timeSnapshot 2024/4/5-12:42:39
"""
import jieba.posseg as pseg


def extract_noun(user_input: str):
    words = pseg.cut(user_input)
    return [[word.word for word in words if word.flag.startswith('n')]]

