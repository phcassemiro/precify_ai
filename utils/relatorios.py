from app.database import Simulacao


def gerar_relatorio_produto(produto_id, db):
    simulacoes = db.query(Simulacao).filter_by(produto_id=produto_id).all()
    if not simulacoes:
        return {"mensagem": "Nenhuma simulação encontrada"}

    total_lucro = sum(s.lucro_estimado for s in simulacoes)
    margem_media = sum(s.margem for s in simulacoes) / len(simulacoes)

    return {
        "lucro_total": round(total_lucro, 2),
        "margem_media": round(margem_media, 2),
        "simulacoes": len(simulacoes)
    }
