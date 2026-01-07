from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from .models import models
from .database.database import engine,Base
from .routers import auth,Book
import time


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
    
)

@app.middleware("http")
async def process_time(request:Request,call_next):
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start
    response.headers["X-Process-Time"] = str(process_time)
    return response



app.include_router(auth.router)
app.include_router(Book.router)
