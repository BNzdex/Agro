from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import excel_reader
from banco_de_dados import SessionLocal
from models import User
import auth

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class UserIn(BaseModel):
    nome: str
    email: str
    senha: str

@app.post("/register")
def register(user: UserIn):
    db = SessionLocal()
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Usuário já existe")
    db_user = User(nome=user.nome, email=user.email, senha=user.senha)
    db.add(db_user)
    db.commit()
    return {"msg": "Usuário criado"}

@app.post("/login")
def login(user: UserIn):
    db = SessionLocal()
    db_user = db.query(User).filter(User.email == user.email, User.senha == user.senha).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"msg": "Login bem-sucedido"}

@app.get("/recomendacoes")
def recomendacoes(cultura: str, solo: str):
    resultado = excel_reader.get_recommendation(cultura, solo)
    return resultado