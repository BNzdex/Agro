from flask import Flask, render_template, request, redirect
import sqlite3
# flask sqlalchemy
# flask wtf forms

app = Flask(__name__)

def conectar():
    return sqlite3.connect('banco_de_dados/banco_agro.db')

@app.route('/salvar', methods=['POST'])
def salvar():
    dados = request.form  # Ou request.get_json() se usar JS/AJAX
    # Aqui você processa e salva no banco
    return redirect('/')


@app.route("/")
def pagina_login():
    """Rota principal que renderiza a página de login do site."""
    return render_template("front-end/index.html")

@app.route("/dashboard")
def dashboard():
    """Página inicial de dentro so site com as opções de escolhas"""
    return render_template("front-end/dashboard.html")


if __name__ == "__main__":
    app.run()
