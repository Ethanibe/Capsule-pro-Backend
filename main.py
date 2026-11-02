from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import db 
from routes import auth, products


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()
app = FastAPI(lifespan = lifespan) 

app.include_router(auth.router, prefix="/auth")
app.include_router(products.router, prefix="/products")

@app.get("/")
def read_root():
    return {"message": "welcome to capsule pro"}
