from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from api.routes import router

app = FastAPI()

origins = [

    "http://127.0.0.1:5500",

    "http://localhost:5500",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_headers = ["*"],
    allow_methods = ["*"],
    allow_credentials = True
)

app.include_router(router)