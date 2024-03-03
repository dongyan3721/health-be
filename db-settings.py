"""
@author David Antilles
@description 数据库配置项
@timeSnapshot 2024/3/3-20:22:33
"""

DATABASE_PROPERTIES = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": "47.101.34.15",
                "port": 3306,
                "user": "root",
                "password": "9G%ZN##Vu8^T6Pn",
                "database": "health",
                "minsize": 1,
                "maxsize": 5,
                "charset": "utf8mb4",
                "echo": True
            }
        }
    },
    "apps": {
        "models": {
            "models": [
                "app.model.models",
                "aerich.models"
            ],
            "default_connection": "default"
        }
    },
    "use_tz": "False",
    "timezone": "Asia/Shanghai"
}
