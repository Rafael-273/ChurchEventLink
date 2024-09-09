from sqlalchemy.orm import Session
from .models.models import Event, Art
from .schemas.schemas import CreateEvent, CreateArt

def create_event(db: Session, evento: CreateEvent):
    db_evento = Event(**evento.dict())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento

def list_events(db: Session):
    return db.query(Event).all()

def create_art(db: Session, arte: CreateArt):
    db_arte = Art(**arte.dict())
    db.add(db_arte)
    db.commit()
    db.refresh(db_arte)
    return db_arte

def list_arts(db: Session):
    return db.query(Art).all()
