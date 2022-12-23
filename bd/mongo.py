from pymongo import MongoClient

def inicia_conexao():

    client = MongoClient('localhost', 27020)
    db = client['puc']
    col = db.recomendacoes
    return col

def consulta_recomendacoes(usuario, conexao):

    recomendacoes = list(conexao.find({"userId": usuario}))
    list_rec = []
    for rec in recomendacoes:
        list_rec.append((rec['movieId'],rec['rating']))

    return {'Recomendações': list_rec}