from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..schemas.schemas import CreateEvent, CreateArt
from ..crud import create_event, list_events, create_art, list_arts

event_router = APIRouter()
art_router = APIRouter()

@event_router.post("/events/")
def create_event_view(event: CreateEvent, db: Session = Depends(get_db)):
    return create_event(db, event)

@event_router.get("/events/")
def list_events_view(db: Session = Depends(get_db)):
    return list_events(db)

@art_router.post("/arts/")
def create_art_view(art: CreateArt, db: Session = Depends(get_db)):
    return create_art(db, art)

@art_router.get("/arts/")
def list_arts_view(db: Session = Depends(get_db)):
    return list_arts(db)
