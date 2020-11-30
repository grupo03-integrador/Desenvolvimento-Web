#coding: utf-8
from flask import Blueprint, render_template, request, jsonify
from mod_produto.produtoDB import Produtos

bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

# FormListaProduto
@bp_produto.route("/", methods=['GET', 'POST'])
def formListaProduto():
    produto = Produtos()
    res = produto.selectALL()
    return render_template('formListaProduto.html', result=res, content_type='application/json')

# FormCadastroProduto
@bp_produto.route("/formCadastroProduto", methods=['POST'])
def formCadastroProduto():
    return render_template("formCadastroProduto.html")

#-----------------------------------------------------------------------------------