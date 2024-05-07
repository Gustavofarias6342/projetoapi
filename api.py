from flask import blueprint, jsonify, request

bp = blueprint("api", __name__)


#Daqui pra baixo as rotas

@bp.route('/')
def index():
    return jsonify({"status": 200, "message": "API do Gustavo Da silva Castro Farias"})
@bp.route("/aleatorios")
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route("/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})