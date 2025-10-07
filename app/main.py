from fastapi import FastAPI
from pydantic import BaseModel
from app.database import SessionLocal, Produto, Simulacao
from utils.relatorios import gerar_relatorio_produto
from models.modelo_precificacao import prever_preco
from utils.simulador import simular_impacto
from app.auth import criar_usuario, verificar_senha
from app.database import Usuario
from fastapi import HTTPException

app = FastAPI(title="Precify.AI")

# Modelo de entrada da API
class Entrada(BaseModel):
    preco_concorrente: float
    estoque: int
    demanda: int
    custo: float

class UsuarioEntrada(BaseModel):
    nome: str
    email: str
    senha: str

@app.post("/prever")
def prever(entrada: Entrada):
    preco = prever_preco([[entrada.preco_concorrente, entrada.estoque, entrada.demanda, entrada.custo]])
    margem, lucro = simular_impacto(preco, entrada.custo, entrada.demanda)

    db = SessionLocal()
    produto = Produto(
        nome="Produto X",
        custo=entrada.custo,
        estoque=entrada.estoque,
        demanda=entrada.demanda,
        preco_concorrente=entrada.preco_concorrente,
        preco_sugerido=preco
    )
    db.add(produto)
    db.commit()

    simulacao = Simulacao(
        produto_id=produto.id,
        preco_sugerido=preco,
        margem=margem,
        lucro_estimado=lucro
    )
    db.add(simulacao)
    db.commit()
    db.close()

    return {
        "preco_sugerido": round(preco, 2),
        "margem": round(margem, 2),
        "lucro_estimado": round(lucro, 2)
    }

@app.post("/cadastro")
def cadastro(usuario: UsuarioEntrada):
    db = SessionLocal()
    if db.query(Usuario).filter_by(email=usuario.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    novo = criar_usuario(db, usuario.nome, usuario.email, usuario.senha)
    db.close()
    return {"mensagem": "Usuário criado com sucesso", "id": novo.id}

@app.post("/login")
def login(usuario: UsuarioEntrada):
    db = SessionLocal()
    user = db.query(Usuario).filter_by(email=usuario.email).first()
    db.close()
    if not user or not verificar_senha(usuario.senha, user.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"mensagem": "Login bem-sucedido", "plano": user.plano}


@app.get("/relatorio/{produto_id}")
def relatorio(produto_id: int):
    db = SessionLocal()
    relatorio = gerar_relatorio_produto(produto_id, db)
    db.close()
    return relatorio