import uvicorn

from app.routers import mock, interface

from fastapi import FastAPI

app = FastAPI()
app.include_router(mock.router)
app.include_router(interface.router)


@app.get("/")
async def root():
    return {"message": "Hello MockMeter!"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
