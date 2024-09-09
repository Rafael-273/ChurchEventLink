from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database.database import Base


class Event(Base):
    __tablename__ = 'eventos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String, nullable=True)
    data_inicio = Column(DateTime, nullable=False)
    data_fim = Column(DateTime, nullable=True)
    arquivado = Column(Boolean, default=False)
    ministerio = Column(String, nullable=True)
    artes = relationship("Arte", back_populates="evento")


class Art(Base):
    __tablename__ = 'artes'

    id = Column(Integer, primary_key=True, index=True)
    nome_arquivo = Column(String, nullable=False)
    formato = Column(String, nullable=False)
    link_google_drive = Column(String, nullable=False)
    evento_id = Column(Integer, ForeignKey('eventos.id'))
    evento = relationship("Evento", back_populates="artes")
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
