from sqlalchemy import Column, Integer, String, Numeric, Date, Identity, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from flask_login import UserMixin


class Usuario(Base, UserMixin):
    __tablename__ = "usuarios"

    id = Column(Integer, Identity(start=1), primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)

    transacoes = relationship("Transacao", back_populates="usuario")


class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, Identity(start=1), primary_key=True)
    descricao = Column(String(100))
    valor = Column(Numeric(10, 2), nullable=False)
    data = Column(Date, nullable=False)
    tipo = Column(String(10), nullable=False)  # "receita" ou "despesa"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    usuario = relationship("Usuario", back_populates="transacoes")