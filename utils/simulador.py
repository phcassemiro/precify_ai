def simular_impacto(preco, custo, demanda):
    margem = preco - custo
    lucro_total = margem * demanda
    return margem, lucro_total
