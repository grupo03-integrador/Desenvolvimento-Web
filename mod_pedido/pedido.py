#coding: utf-8
from flask import Blueprint, render_template , request

bp_pedido = Blueprint('pedido', __name__, url_prefix="/pedido", template_folder='templates')

@bp_pedido.route("/", methods=['GET', 'POST'])

def formListaPedido():
    return render_template("formListaPedido.html")

@bp_pedido.route("/formPedido", methods=['POST'])

def formPedido():
    return render_template("formPedido.html") 