#coding: utf-8
from flask import Blueprint, render_template, request

bp_comanda = Blueprint('comanda', __name__, url_prefix="/comanda", template_folder='templates')

# FormListaComandas
@bp_comanda.route("/", methods=['GET', 'POST'])
def formListaComandas():
    return render_template("formListaComandas.html") 

# FormAbrirComanda
@bp_comanda.route("/formAbrirComanda", methods=['GET','POST'])
def formAbrirComanda():
    return render_template("formAbrirComanda.html")

# FormFinalizarComanda
@bp_comanda.route("/formFinalizarComanda", methods=['GET','POST'])
def formFinalizarComanda():
    return render_template("formFinalizarComanda.html")

# FormPagamento
@bp_comanda.route("/formPagamento", methods=['GET','POST'])
def formPagamento():
    return render_template("formPagamento.html")   
#-----------------------------------------------------------------------------------