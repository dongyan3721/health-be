"""
@author David Antilles
@description 静态资源访存类
@timeSnapshot 2024/3/4-21:12:27
"""
from fastapi import APIRouter
from starlette.responses import FileResponse
from app.framework.config.ApplicationProperties import APPLICATION_PROPERTIES
from app.framework.config.FileConfig import getFileExtension
from app.utils.file.ContentTypeAutoInference import auto_inference

static_resource_access_controller = APIRouter()


@static_resource_access_controller.get('/{file_path:path}')
async def resource_get(file_path: str):
    return FileResponse(
        APPLICATION_PROPERTIES['file-upload'] + file_path,
        media_type=auto_inference(getFileExtension(file_path))
    )


@static_resource_access_controller.post('/{file_path:path}')
async def resource_post(file_path: str):
    return FileResponse(
        APPLICATION_PROPERTIES['file-upload'] + file_path,
        media_type=auto_inference(getFileExtension(file_path))
    )
