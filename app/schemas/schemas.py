from pydantic import BaseModel
from datetime import datetime

class CreateEvent(BaseModel):
    nome: str
    descricao: str
    data_inicio: datetime
    data_fim: datetime
    ministerio: str = None


class Event(CreateEvent):
    id: int

    class Config:
        orm_mode = True


class CreateArt(BaseModel):
    nome_arquivo: str
    formato: str
    link_google_drive: str
    evento_id: int


class Art(CreateArt):
    id: int
    criado_em: datetime

    class Config:
        orm_mode = True
