import uvicorn
from app.framework.config.ApplicationProperties import APPLICATION_PROPERTIES
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

register_tortoise(
    app=app,
    config=APPLICATION_PROPERTIES["database"]
)

# print(APPLICATION_PROPERTIES)


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='127.0.0.1',
        port=8080,
        reload=True,
        workers=1
    )
