from fastapi import FastAPI
from uvicorn import run

from api.handlers import router

app = FastAPI()

app.include_router(router=router)


if __name__ == '__main__':

    run(
        app=app,
        host="0.0.0.0",
        port=80,
        use_colors=True
    )
