"""
解决循环导入问题
"""
from fastapi import FastAPI

app = FastAPI(docs_url=None, redoc_url=None)


@app.get('/', include_in_schema=False)
async def hello():
    return 'Hello,MockMeter'


from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
