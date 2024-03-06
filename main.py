import uvicorn
from starlette.middleware.cors import CORSMiddleware

from app.framework.config.ApplicationProperties import APPLICATION_PROPERTIES
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.controller.KVController import kv
from app.controller.HospitalController import hospital_route
from app.controller.UserController import user_router
from app.controller.common.StaticResourceAccessController import static_resource_access_controller
# 预计还要包括一个评论区相关

app = FastAPI()

# 注册数据库
register_tortoise(
    app=app,
    config=APPLICATION_PROPERTIES["database"]
)
# 注册中间件
app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=[
        'http://localhost',
        'http://localhost:8080',
    ],
    allow_credentials=True,
    # 一定要大写请求方法
    allow_methods=['GET', 'DELETE', 'PUT', 'POST'],
    allow_headers=['*']
)

# 注册路由
app.include_router(kv, prefix="/kv", tags=["键值对表"])
app.include_router(hospital_route, prefix="/hospital", tags=["医院相关"])
app.include_router(user_router, prefix="/user", tags=['用户相关'])
app.include_router(static_resource_access_controller, prefix='/static', tags=['静态资源读写相关'])


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='127.0.0.1',
        port=8080,
        reload=True,
        workers=1
    )
