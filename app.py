from flask import Flask

app = Flask(__name__)

FLAG = "FLAG{rota_admin_sem_protecao}"


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


@app.route("/admin")
def admin():
    return f"<h1>Painel do Admin</h1><p>{FLAG}</p>"


if __name__ == "__main__":
    app.run()