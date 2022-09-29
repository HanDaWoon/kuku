from option import *

from config import Config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import user
import board.free
import board.qna


app = FastAPI(title="kuku-api")
app.include_router(user.router)
app.include_router(board.free.router)
app.include_router(board.qna.router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello!! fastapi"}

if __name__ == "__main__":
    import uvicorn

    print("port -> ", Config.HTTP["port"])
    uvicorn.run("main:app", host="127.0.0.1", port=Config.HTTP["port"], reload=True)
