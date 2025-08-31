import duckdb as db
from flask import Flask, render_template
from coleta_dados import buscar_dados as bd

app = Flask(__name__)

indicadores = {
    'selic': 432,
    'dolar': 1,
    'ipca': 433
}


@app.route("/")
def pagina_principal():
   
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)