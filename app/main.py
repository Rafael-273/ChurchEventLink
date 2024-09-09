from fastapi import FastAPI
from .database.database import init_db
from .routers.routers import event_router, art_router

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(event_router)
app.include_router(art_router)
