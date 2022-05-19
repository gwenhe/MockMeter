import uvicorn
from common import initialization
from common.ext import app

from apps.project import routers as project
# from apps.interface import routers as interface

app.include_router(project.router)
# app.include_router(interface.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
