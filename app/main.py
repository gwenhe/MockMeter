import uvicorn
from app import app
from app.routers import mock, interface

app.include_router(mock.router)
app.include_router(interface.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
