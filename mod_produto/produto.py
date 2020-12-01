#coding: utf-8
from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from mod_login.login import validaSessao
from mod_produto.produtoDB import Produtos
import base64

bp_produto = Blueprint('produto', __name__, url_prefix='/', template_folder='templates')

@bp_produto.route("/listaProduto", methods=['GET', 'POST'])
@validaSessao
def listaProduto():
        produto = Produtos()
        res = produto.selectALL()
        return render_template('formListaProduto.html', result=res, content_type='application/json')

@bp_produto.route("/formProduto", methods=['POST'])
@validaSessao
def formProduto():
     produto = Produtos()
     return render_template('formCadastroProduto.html', produto=produto, content_type='application/json')

@bp_produto.route('/formEditProduto', methods=['POST'])
@validaSessao
def formEditProduto():
     produto = Produtos()
     produto.id_produto = request.form['id_produto']
     produto.selectONE()
     return render_template('formCadastroProduto.html', produto=produto, content_type='application/json')

@bp_produto.route('/addProduto', methods=['POST'])
@validaSessao
def addProduto():   
        produto = Produtos()
        produto.id_produto = request.form['id_produto'] 
        produto.nome = request.form['nome']       
        produto.valor_unitario = request.form['valor_unitario']
        produto.descricao = request.form['descricao']
        #produto.imagem = "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode(request.files['imagem'].read()), "utf-8")
        produto.insert()
        return redirect(url_for('produto.listaProduto'))
        

@bp_produto.route('/editProduto', methods=['POST'])
@validaSessao
def editProduto():
        produto = Produtos()
        produto.id_produto = request.form['id_produto']
        produto.nome = request.form['nome']
        produto.descricao = request.form['descricao']
        produto.valor_unitario = request.form['valor_unitario']
        
        produto.update()
        if 'salvaEditaProdutoDB' in request.form:
            produto.update()
        elif 'salvaExcluiProdutoDB' in request.form:   
            produto.delete()

        return redirect(url_for('produto.listaProduto'))
