#coding: utf-8
import os

from datetime import timedelta 
from flask import Flask, session

from mod_login.login import bp_login
from mod_home.home import bp_home
from mod_cliente.cliente import bp_cliente
from mod_produto.produto import bp_produto
from mod_pedido.pedido import bp_pedido
from mod_erro.erro import bp_erro


app = Flask(__name__)

app.secret_key = os.urandom(12).hex()

@app.before_request 
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

app.register_blueprint(bp_login)
app.register_blueprint(bp_home)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_produto)
app.register_blueprint(bp_pedido)



if __name__ == "__main__":
    app.run()