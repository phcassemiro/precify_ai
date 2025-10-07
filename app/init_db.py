from app.database import Base, engine

def criar_banco():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    criar_banco()
