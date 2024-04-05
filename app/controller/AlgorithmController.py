"""
@author David Antilles
@description 算法控制层
@timeSnapshot 2024/4/5-12:46:56
"""
import fastapi
from app.framework.net.HttpMessages import TableData
from app.algorithm.keyword_extract import extract_noun

algorithm_router = fastapi.APIRouter()


@algorithm_router.get("/keyword-extract/{words}")
def keyword_extract(words: str):
    result = extract_noun(words)
    return TableData.success(result[0], len(result[0]))
