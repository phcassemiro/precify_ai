from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.database import Usuario

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash: str) -> bool:
    return pwd_context.verify(senha, hash)

def criar_usuario(db: Session, nome: str, email: str, senha: str):
    usuario = Usuario(
        nome=nome,
        email=email,
        senha_hash=gerar_hash(senha),
        plano="gratuito"
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario