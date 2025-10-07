from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Caminho do banco SQLite
DATABASE_URL = "sqlite:///./precify.db"

# Conexão e sessão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()

# Tabela de produtos
class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    custo = Column(Float)
    estoque = Column(Integer)
    demanda = Column(Integer)
    preco_concorrente = Column(Float)
    preco_sugerido = Column(Float)

# Tabela de simulações
class Simulacao(Base):
    __tablename__ = "simulacoes"
    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer)
    preco_sugerido = Column(Float)
    margem = Column(Float)
    lucro_estimado = Column(Float)
    data = Column(DateTime, default=datetime.utcnow)

# Tabela de usuários (para login e planos)
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String)
    plano = Column(String, default="gratuito")  # gratuito, premium, parceiro
