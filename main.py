from fastapi import FastAPI
from app.views.computeview import router
from app.helpers.middleware import LogMiddleware
app = FastAPI()
app.add_middleware(LogMiddleware)
app.include_router(router, tags=['Compute'], prefix='')
