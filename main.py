from fastapi import FastAPI
from app.views.computeview import router
app = FastAPI()
app.include_router(router, tags=['Compute'], prefix='')
