from flask import Flask, render_template, jsonify
from coleta_dados import buscar_dados_bcb

app = Flask(__name__)

indicadores = {
    'selic': 432,
    'dolar': 1,
    'ipca': 433
}

@app.route("/")
def pagina_principal():
    return render_template("index.html")


@app.route("/api/dados/<nome_ativo>/<int:num_dias>")
def api_dados(nome_ativo, num_dias):
    if nome_ativo not in indicadores:
        return jsonify({"erro": "Ativo não encontrado"}), 404

    codigo_ativo = indicadores[nome_ativo]

    dados = buscar_dados_bcb(codigo_ativo, nome_ativo, num_dias)

    if dados is not None and not dados.empty:
  
        dados_json = dados.to_json(orient='records', date_format='iso')
        return dados_json
    else:
        return jsonify([]) 

if __name__ == "__main__":
    app.run(debug=True)