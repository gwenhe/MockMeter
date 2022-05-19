"""
解决循环导入问题
"""
from fastapi import FastAPI

app = FastAPI(docs_url=None, redoc_url=None)


@app.get('/', include_in_schema=False)
async def hello():
    return 'Hello,MockMeter'
