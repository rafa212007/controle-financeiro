import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, redirect, url_for
from database import SessionLocal
from models import Transacao, Usuario
from datetime import datetime
from sqlalchemy import func
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    db = SessionLocal()
    usuario = db.query(Usuario).filter(Usuario.id == int(user_id)).first()
    db.close()
    return usuario

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        db = SessionLocal()

        senha_criptografada = generate_password_hash(request.form["senha"])

        novo_usuario = Usuario(
            nome=request.form["nome"],
            email=request.form["email"],
            senha_hash=senha_criptografada
        )
        db.add(novo_usuario)
        db.commit()
        db.close()

        return redirect(url_for("login"))

    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        db = SessionLocal()
        usuario = db.query(Usuario).filter(Usuario.email == request.form["email"]).first()
        db.close()

        if usuario and check_password_hash(usuario.senha_hash, request.form["senha"]):
            login_user(usuario)
            return redirect(url_for("index"))

        return render_template("login.html", erro="E-mail ou senha incorretos")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/")
@login_required
def index():
    db = SessionLocal()

    query = db.query(Transacao).filter(Transacao.usuario_id == current_user.id)

    data_inicio = request.args.get("data_inicio")
    data_fim = request.args.get("data_fim")

    if data_inicio:
        query = query.filter(Transacao.data >= datetime.strptime(data_inicio, "%Y-%m-%d"))
    if data_fim:
        query = query.filter(Transacao.data <= datetime.strptime(data_fim, "%Y-%m-%d"))

    transacoes = query.order_by(Transacao.data.desc()).all()

    html = render_template("index.html", transacoes=transacoes, data_inicio=data_inicio, data_fim=data_fim)
    db.close()
    return html


@app.route("/nova-transacao", methods=["POST"])
@login_required
def nova_transacao():
    db = SessionLocal()

    nova = Transacao(
        descricao=request.form["descricao"],
        valor=float(request.form["valor"]),
        data=datetime.strptime(request.form["data"], "%Y-%m-%d"),
        tipo=request.form["tipo"],
        usuario_id=current_user.id
    )
    db.add(nova)
    db.commit()
    db.close()

    return redirect(url_for("index"))

@app.route("/excluir-transacao/<int:id>")
@login_required
def excluir_transacao(id):
    db = SessionLocal()
    transacao = db.query(Transacao).filter(Transacao.id == id, Transacao.usuario_id == current_user.id).first()
    if transacao:
        db.delete(transacao)
        db.commit()
    db.close()
    return redirect(url_for("index"))


@app.route("/editar-transacao/<int:id>", methods=["GET", "POST"])
@login_required
def editar_transacao(id):
    db = SessionLocal()
    transacao = db.query(Transacao).filter(Transacao.id == id, Transacao.usuario_id == current_user.id).first()

    if request.method == "POST":
        transacao.descricao = request.form["descricao"]
        transacao.valor = float(request.form["valor"])
        transacao.data = datetime.strptime(request.form["data"], "%Y-%m-%d")
        transacao.tipo = request.form["tipo"]
        db.commit()
        db.close()
        return redirect(url_for("index"))

    html = render_template("editar.html", transacao=transacao)
    db.close()
    return html


@app.route("/relatorio")
@login_required
def relatorio():
    db = SessionLocal()

    receitas = db.query(func.sum(Transacao.valor)).filter(Transacao.tipo == "receita", Transacao.usuario_id == current_user.id).scalar() or 0
    despesas = db.query(func.sum(Transacao.valor)).filter(Transacao.tipo == "despesa", Transacao.usuario_id == current_user.id).scalar() or 0
    saldo = receitas - despesas

    db.close()
    return render_template("relatorio.html", receitas=receitas, despesas=despesas, saldo=saldo)


if __name__ == "__main__":
    app.run(debug=True)