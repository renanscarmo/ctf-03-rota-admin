import os
import secrets

from flask import Flask, abort, redirect, request, session
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)

ADMIN_USER = "admin"
SENHA_HASH = os.environ.get("ADMIN_SENHA_HASH", "")
FLAG = "FLAG{rota_admin_com_protecao}"

FORMULARIO = """
<h1>Login do Admin</h1>
<form method="post">
  <input name="usuario" placeholder="usuario">
  <input name="senha" type="password" placeholder="senha">
  <button type="submit">Entrar</button>
</form>
"""


@app.route("/")
def home():
    return """
    <h1>Loja do Renan</h1>
    <p>Bem-vindo! Veja nossos produtos.</p>
    <a href="/produtos">Ver produtos</a>
    """


@app.route("/produtos")
def produtos():
    return "<h1>Produtos</h1><p>Camiseta, caneca e bone.</p>"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        senha = request.form.get("senha", "")
        if usuario == ADMIN_USER and check_password_hash(SENHA_HASH, senha):
            session["admin"] = True
            return redirect("/admin")
        return FORMULARIO + "<p>Usuario ou senha incorretos.</p>"
    return FORMULARIO


@app.route("/admin")
def admin():
    if not session.get("admin"):
        abort(403)
    return f"<h1>Painel do Admin</h1><p>{FLAG}</p><a href='/logout'>Sair</a>"


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run()